#import libraries
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
#this is for making custom stop words
from sklearn.feature_extraction._stop_words import ENGLISH_STOP_WORDS
#train test split for training and testing duh
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.svm import SVC
import numpy as np

#read csv files, give their columns titles
drawings = pd.read_csv(r"C:\Users\gramos1\OneDrive - Reworld\DrawingNames.csv",sep=',',header=0,names=['Drawing Title', 'Category'])
#Reading only the labeled drawings
drawings = drawings[drawings['Category'].notna()]

code_pattern = r'^[A-Za-z0-9]+[-_\s]?'
drawings['Drawing Title'] = drawings['Drawing Title'].str.replace(code_pattern, '', regex=True)

custom_stop_words = list(ENGLISH_STOP_WORDS) + ['sys',
                                                'installation',
                                                'detail',
                                               'schem',
                                               'diagram',
                                               'dwg',
                                               'diag',
                                               'plans',
                                               'layout',
                                               'details',
                                               'arrgt',]



#vect to bring in tfidf vectorizer
#stop words is to filter noise, english here to filter out generic english

vect = TfidfVectorizer(
     #trying to get rid of english and numbers
                       stop_words= custom_stop_words,
    #filter out anything not alphabetic
                        token_pattern=r'(?u)\b[a-zA-Z]+\b',
     #put this 1-2 so i can get bigrams, might need to increase? 1-3?
                      ngram_range=(1,3),
     #I want features to be words i think
                    analyzer = 'word',
      #min_df to try and filter out irrelevant words? usually drawings are in batches so if it's
        #Not important enough to be in a batch then dont count it
                     min_df=3,)

#fit_transform applied to drawing title names,
#Learn vocabulary and idf, return document-term matrix.
X = vect.fit_transform(drawings['Drawing Title'])

#output of feature names for transformation
#(texts turns into numerical features)
print(vect.get_feature_names_out()[:200])
#prints out matrix with feature values, many will be zero, presented in this way to save memory
#remember matrix is one row per document and one col per token
#value = tfidf score 0-1, and the score quantifies how important that word is to the title
print(X[:50])

#time to split up data
y = drawings['Category']
X_train, X_test, y_train,y_test = train_test_split(X,y,test_size = 0.33, random_state = 42)

# Initialize and train the classifier
clf = SVC(kernel='linear')
clf.fit(X_train, y_train)

#predict on test set
y_pred = clf.predict(X_test)

#evaluate performance
accuracy = accuracy_score(y_test,y_pred)
report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy:.4f}')
print('Classification Report:')
print(report)

def predict_category(text):

    text_vec = vect.transform([text])
    prediction = clf.predict(text_vec)
    return prediction[0]
    

# Next step is to fix this so it doesnt take the cut down version and actually sorts through all 5000 entries

alldrawings = drawings['Drawing Title'].astype(str)
completetfidf = vect.fit_transform(alldrawings)
completepredictions = clf.predict(completetfidf)
drawings['Prediction'] = completepredictions

drawings['Accurate?'] = np.where((drawings['Category'] == drawings['Prediction']),1,0)

drawingpredictions = pd.DataFrame(drawings[['Drawing Title','Category','Prediction','Accurate?']])
file_name = 'OutputPredictions.xlsx'
drawingpredictions.to_excel(file_name)
