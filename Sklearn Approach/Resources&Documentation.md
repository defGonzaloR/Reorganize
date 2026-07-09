Because I believe in learning through reading extensively on a subject first before any application, heres what I found to be particularly useful for this, and will probably be using for future reference:

practical explanation of tfidf vectorizer https://www.codelessgenie.com/blog/understanding-text-feature-extraction-tfidfvectorizer-in-python-scikit-learn/
Section 8.2.3 of https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction
documentation for tfidf vectorizer https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html

Notes: 
To master TfidfVectorizer, you must understand the order in which it processes text. Misunderstanding this can lead to unexpected results (e.g., stop words appearing in n-grams or lowercase terms being tokenized incorrectly). Here’s the exact sequence:

Preprocessing: Applies preprocessor (custom or default). The default preprocessor lowercases text if lowercase=True (default).
Tokenization: Splits preprocessed text into tokens (words/characters) using tokenizer (custom or default). The default splits on whitespace/punctuation (e.g., "quick brown" → ["quick", "brown"]).
Stop Word Removal: Filters out tokens in the stop_words list (if enabled).
N-Gram Generation: Creates n-grams from remaining tokens using ngram_range (e.g., unigrams, bigrams).
Term Frequency (TF) Counting: Counts occurrences of each n-gram in each document.
IDF Calculation: Computes IDF weights for n-grams using use_idf, smooth_idf, and sublinear_tf.
Normalization: Scales TF-IDF scores using norm (L1, L2, or None).
