Currently have SciKitModel.ipynb in this folder, there I was able to import the drawing names, make that table look nice, then I go thru the preprocessing stage and run tfidfvectorizer to extract the features, resulting in the matrix that gives each feature/ terms important to each document

# Vectorization

<img width="1443" height="745" alt="image" src="https://github.com/user-attachments/assets/4f5d6b53-652e-465c-8070-06e38b54105c" />

This image above shows any features that were extracted, I tried to fine tune the stop words so it removes any common words like "diagrams", "schematics", etc. anything that will mess up the feature extraction

<img width="1472" height="775" alt="image" src="https://github.com/user-attachments/assets/87a5d170-20c4-4b68-ac83-65208dec9e4e" />

Here is the actual tfidf matrix that gives coordinate of a term and then its tfidf value, remember that quantifies its importance to the corpus/list of documents.

Now to just figure out where to move on from here!

# Training

Now with my text now being able to be inputted into a model, I came across Logistic Regression, a classification model that that models how likely an input belongs to a class or category. This sounds like exactly what I need at the moment, as I'm going for a supervised approach with my already-made csv file of keywords.
However what I didnt anticipate with supervised learning was needing to individually mark a bunch of drawings with categories, so I need to get on that.


My most recent publishing of the code is pretty good, so far it only runs through 1034 of the entries, as thats how many i manually labelled. After the weekend, I want to come back and run the process through all 5000 entries! Id say im on track for success right now.
