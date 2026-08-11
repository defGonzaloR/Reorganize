import os
import shutil

# Update paths to match your local setup
SOURCE_DIR = r"C:\Users\gramos1\OneDrive - Reworld\Reworld Essex - Engineering\Old Essex Drawing Folder"
BASE_DEST_DIR = r"C:\Users\gramos1\OneDrive - Reworld\Reworld Essex - Engineering\Reorganized Drawings"


def reset_to_baseline():
    if not os.path.exists(BASE_DEST_DIR):
        print(f"Destination folder '{BASE_DEST_DIR}' does not exist. Nothing to reset.")
        return

    # Ensure source directory exists
    os.makedirs(SOURCE_DIR, exist_ok=True)

    moved_count = 0

    # Walk through all subfolders in Labeled_Keywords
    for root, dirs, files in os.walk(BASE_DEST_DIR, topdown=False):
        for file in files:
            src_path = os.path.join(root, file)
            dest_path = os.path.join(SOURCE_DIR, file)

            # Handle duplicate filename collisions if necessary
            if os.path.exists(dest_path):
                name, ext = os.path.splitext(file)
                dest_path = os.path.join(SOURCE_DIR, f"{name}_restored{ext}")

            try:
                shutil.move(src_path, dest_path)
                print(f"Restored: '{file}' -> Unprocessed")
                moved_count += 1
            except Exception as e:
                print(f"Error moving '{file}': {e}")

        # Clean up empty category subfolders
        if root != BASE_DEST_DIR:
            try:
                if not os.listdir(root):
                    os.rmdir(root)
                    print(f"Removed empty directory: '{root}'")
            except Exception as e:
                print(f"Could not remove folder '{root}': {e}")

    print(f"\nReset Complete! Restored {moved_count} file(s) back to '{SOURCE_DIR}'.")

if __name__ == "__main__":
    reset_to_baseline()