import os
import re
import shutil
import pandas as pd

EXCEL_PATH = r"C:\Users\gramos1\BulkRename\OutputPredictions.xlsx"
SOURCE_DIR = r"C:\Users\gramos1\OneDrive - Reworld\Reworld Essex - Engineering\Old Essex Drawing Folder"
BASE_DEST_DIR = r"C:\Users\gramos1\OneDrive - Reworld\Reworld Essex - Engineering\Reorganized Drawings"

def normalize_text(text):
    """Lowercase, strip extensions, convert dash variants, collapse whitespace."""
    if not text or pd.isna(text):
        return ""
    text = str(text).lower()
    text = re.sub(r'[\u2010-\u2015\u2212]', '-', text)
    text = re.sub(r'[^a-z0-9\- ]', ' ', text)
    return ' '.join(text.split())

def extract_drawing_id(text):
    """Extracts leading drawing number/ID like '675125' or 'DU-24-C-11257-2'."""
    norm = normalize_text(text)
    match = re.match(r'^([a-z0-9]+(?:-[a-z0-9]+)*)', norm)
    return match.group(1) if match else ""

def organize_all_23_categories():
    df = pd.read_excel(EXCEL_PATH)
    df.columns = df.columns.str.strip()

    # Step 1: Ensure ALL 23 category folders exist
    unique_categories = df["Prediction"].dropna().astype(str).str.strip().unique()
    for category in unique_categories:
        os.makedirs(os.path.join(BASE_DEST_DIR, category), exist_ok=True)
    
    print(f"Verified/Created all {len(unique_categories)} category directories.")

    # Step 2: Read physical source files
    available_files = os.listdir(SOURCE_DIR)
    success_count = 0

    # Step 3: Match and move each drawing
    for _, row in df.iterrows():
        if pd.isna(row["Drawing Title"]) or pd.isna(row["Prediction"]):
            continue

        raw_title = str(row["Drawing Title"]).strip()
        prediction = str(row["Prediction"]).strip()
        target_folder = os.path.join(BASE_DEST_DIR, prediction)

        title_norm = normalize_text(raw_title)
        title_id = extract_drawing_id(raw_title)

        matched_file = None

        for filename in available_files:
            name_without_ext, _ = os.path.splitext(filename)
            file_norm = normalize_text(name_without_ext)
            file_id = extract_drawing_id(name_without_ext)

            # Strategy A: Extracted Drawing ID Match ('675125' inside '675125.pdf' or '675125 - BELT CONVEYOR.dwg')
            if title_id and (title_id == file_id or title_id in file_norm):
                matched_file = filename
                break

            # Strategy B: Normalized full string match
            if title_norm == file_norm or (len(title_norm) > 5 and title_norm in file_norm):
                matched_file = filename
                break

        if matched_file:
            src_path = os.path.join(SOURCE_DIR, matched_file)
            dest_path = os.path.join(target_folder, matched_file)

            try:
                shutil.move(src_path, dest_path)
                print(f"Moved: '{matched_file}' -> '{prediction}'")
                available_files.remove(matched_file)
                success_count += 1
            except Exception as e:
                print(f"Error moving '{matched_file}': {e}")
        else:
            print(f"Not Found: '{raw_title}' (Looking for ID: '{title_id}')")

    print(f"\nProcessing Complete: Successfully moved {success_count} files into 23 category folders.")

if __name__ == "__main__":
    organize_all_23_categories()