# Reorganize
Bringing the company into the current age, providing a way to efficiently organize thousands of old, scanned documents

This is my first ever machine learning-based project, and I will be using this repo as a way to document along the way

The purpose of this project is to take 5000+ files that hold engineering drawings and reorganize them in a way that the current and future plant engineers will be able to easily find appropriate drawings. The current state of this system is that there will be a folder full of drawings and alongside this is an Excel sheet that has drawing names and their related descriptive code. This is of course very time-consuming as opposed to most search systems. Wouldn't it be easier if they were grouped in relation to their system? (i.e boiler-related drawings grouped with other boiler-related drawings)

I took a machine-learning based approach because 1) I didn't want to bore myself to death with going through all 5000 entries and 2) I wanted to leave some kind of impact on the engineering department here.

# The Process
This was my first time programming in Python, but with C/C++ experience from class I didn't think itd be too hard. I tried not to rely on AI for any code writing, and simply used it as a means of navigation through the organization of this project and what topics were useful
I came across Lbl2Vec, which seemed to be the perfect library for this project, as it generates embedded vectors of each text entry and compares them to manually defined keywords, then generates each entry's similiarities to each keyword vector

# Complications (As of right now)
Whether it's due to poor keyword choice on my part, or maybe "word fluff" in the file names, as they have the format of "Title Code - Descriptive Title" and the title code ends up throwing it off (I kept the title code as it'd allow for those who use the spreadsheet to still be able to use it in the new system, call it a transition period), I've kind of run into a wall as the cosine similarity calculations are all really weird, and the assigned categories to the text entries are mostly incorrect. So I might ditch Lbl2Vec, as convenient as it is, and look into using sci-kit.
<img width="1390" height="364" alt="image" src="https://github.com/user-attachments/assets/6ec50865-1634-40f7-96e6-d34b8d08b71e" />
As you can see here, the numbers are either negative, super close to 1, or just a random number between 0 and 1 (the other two are more common, however)
