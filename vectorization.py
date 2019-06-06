import warnings
import pandas as pd
import numpy as np
import pickle
import sys
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.stem.porter import *
import string
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as VS
from textstat.textstat import *
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import classification_report
from sklearn.svm import LinearSVC
import matplotlib.pyplot as plt
import seaborn

import spacy

nlp = spacy.load('en_core_web_sm')

warnings.simplefilter(action='ignore', category=FutureWarning)



# Functions for feature extraction and learning process

def import_from_csv(data_location):
   csv_data = pd.read_csv(data_location) 
   return data
   
   

def get_wordFreq_vector():
   
   pass
   

def get_tf_vector(input):
   tf_vector = tf_vectorizor.fit_transform(input).toarray()
   return tf_vector
   
def get_features(csv_data):
   tweets = csv_data.tweet
   pass
   
def get_pos_tfidf_vector(tweet_tags):
   pos_vectorizer = TfidfVectorizer(
    tokenizer=None,
    lowercase=False,
    preprocessor=None,
    ngram_range=(1, 3),
    stop_words=None,
    use_idf=False,
    smooth_idf=False,
    norm=None,
    decode_error='replace',
    max_features=5000,
    min_df=5,
    max_df=0.75,
    )
    
    pos = pos_vectorizer.fit_transform(
   
   
#expects the tf vector as input, preprocess should be a defined function 
#  
def get_tfid_vector(tweets, tf_vector, tokenize, preprocess):
   
   tfidf_vectorizer = TfidfVectorizer(
    tokenizer=tokenize,
    preprocessor=preprocess,
    ngram_range=(1, 3),
    stop_words=stopwords,
    use_idf=True,
    smooth_idf=False,
    norm=None,
    decode_error='replace',
    max_features=10000,
    min_df=5,
    max_df=0.75
    )
    
   tfidf = tfidf_vectorizer.fit_transform(tweets).to_array()
   vocab = {v:i for i, v in enumerate(vectorizer.get_feature_names())}
   idf_values = vectorizer.idf_
   idf_dict = {i:idf_values[i] for i in vocab.values()}
    
   pass
   
def get_pos_vector(tweets, preprocess, basic_tokenize):
   tweet_tags = []
   
   for tweet in tweets:
      tokens = basic_tokenize(preprocess(tweet))
      tags = nltk.pos_tag(tokens)
      tag_list = [x[1] for x in tags]
      tag_str = " ".join(tag_list)
      tweet_tags.append(tag_str)
   
   return 
      
   pass
   
def get_pos_vector_spacy(tweets):
   tokens = []
   tweet_tags = []
   docs = []
   
   for tweet in tweets
      doc = nlp(tweet)
      docs.append(doc)
         
      tag_list = [x.tag_ for x in doc]
      tag_str = "".join(tag_list)
      tweet_tags.append(tag_str)
   
def get_training_features():
   vectorizer = CountVectorizer(stor_words = "english",
                                preprocessor = clean_text)
   training_features = vectorizer.fit_transform(train_data["text"])
   pass
   
   
def get_SVM_model(training_features, train_data):
   model = LinearSVC()
   model.fit(training_features, train_data["setiment"])
   return model
   pass
   
def get_ngram_model()
   
   pass