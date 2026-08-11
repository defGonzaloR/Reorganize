# Reorganize
Bringing the company into the current age, providing a way to efficiently organize thousands of old, scanned documents

This is my first ever machine learning-based project, and I will be using this repo as a way to document along the way

The purpose of this project is to take 5000+ files that hold engineering drawings and reorganize them in a way that the current and future plant engineers will be able to easily find appropriate drawings. The current state of this system is that there will be a folder full of drawings and alongside this is an Excel sheet that has drawing names and their related descriptive code. This is of course very time-consuming as opposed to most search systems. Wouldn't it be easier if they were grouped in relation to their system? (i.e boiler-related drawings grouped with other boiler-related drawings)

I took a machine-learning based approach because 1) I didn't want to bore myself to death with going through all 5000 entries and 2) I wanted to leave some kind of impact on the engineering department here.

# The Process
This was my first time programming in Python, but with C/C++ experience from class I didn't think itd be too hard. I tried not to rely on AI for any code writing, and simply used it as a means of navigation through the organization of this project and what topics were useful
I came across Lbl2Vec, which seemed to be the perfect library for this project, as it generates embedded vectors of each text entry and compares them to manually defined keywords, then generates each entry's similiarities to each keyword vector. This approach was generally unsuccessful, as the naming and labeling conventions didn't necessarily align with Lbl2Vec's library. My alternative was using Scikit-Learn, a popular library used for machine learning in python, and with pandas integration I was successful in reorganizing the files.

# Reflection
Through this project I learned to navigate and use the Scikit-learn and Pandas libraries, as well as basic data structures and python programming and I/O. With a ~92% success rate across the 5000+ files, I'd label this mostly a success, and hope to hear back from my team in the future with any feedback. I'm aware not every single file is in the proper place, as unique naming conventions, typos, and rare titles generally get in the way of a project involving mass text classification like this. 

Attached to this directory is the scikit model as well as scripts to organize the files. Should this be replicated, any paths in the scripts would need to be changed out for whatever's appropriate for your project. This is far from perfect or expert programming but it's a project that has a physical impact, even if it's on such a scale as improving project workflow.
