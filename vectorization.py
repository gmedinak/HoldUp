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

#Now get other features
sentiment_analyzer = VS()

def count_twitter_objs(text_string):
    """
    Accepts a text string and replaces:
    1) urls with URLHERE
    2) lots of whitespace with one instance
    3) mentions with MENTIONHERE
    4) hashtags with HASHTAGHERE

    This allows us to get standardized counts of urls and mentions
    Without caring about specific people mentioned.
    
    Returns counts of urls, mentions, and hashtags.
    """
    space_pattern = '\s+'
    giant_url_regex = ('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|'
        '[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    mention_regex = '@[\w\-]+'
    hashtag_regex = '#[\w\-]+'
    parsed_text = re.sub(space_pattern, ' ', text_string)
    parsed_text = re.sub(giant_url_regex, 'URLHERE', parsed_text)
    parsed_text = re.sub(mention_regex, 'MENTIONHERE', parsed_text)
    parsed_text = re.sub(hashtag_regex, 'HASHTAGHERE', parsed_text)
    return(parsed_text.count('URLHERE'),parsed_text.count('MENTIONHERE'),parsed_text.count('HASHTAGHERE'))

def other_features(tweet):
    """This function takes a string and returns a list of features.
    These include Sentiment scores, Text and Readability scores,
    as well as Twitter specific features"""
    sentiment = sentiment_analyzer.polarity_scores(tweet)
    
    words = preprocess(tweet) #Get text only
    
    syllables = textstat.syllable_count(words)
    num_chars = sum(len(w) for w in words)
    num_chars_total = len(tweet)
    num_terms = len(tweet.split())
    num_words = len(words.split())
    avg_syl = round(float((syllables+0.001))/float(num_words+0.001),4)
    num_unique_terms = len(set(words.split()))
    
    ###Modified FK grade, where avg words per sentence is just num words/1
    FKRA = round(float(0.39 * float(num_words)/1.0) + float(11.8 * avg_syl) - 15.59,1)
    ##Modified FRE score, where sentence fixed to 1
    FRE = round(206.835 - 1.015*(float(num_words)/1.0) - (84.6*float(avg_syl)),2)
    
    twitter_objs = count_twitter_objs(tweet)
    retweet = 0
    if "rt" in words:
        retweet = 1
    features = [FKRA, FRE,syllables, avg_syl, num_chars, num_chars_total, num_terms, num_words,
                num_unique_terms, sentiment['neg'], sentiment['pos'], sentiment['neu'], sentiment['compound'],
                twitter_objs[2], twitter_objs[1],
                twitter_objs[0], retweet]
    #features = pandas.DataFrame(features)
    return features

def get_feature_array(tweets):
    feats=[]
    for t in tweets:
        feats.append(other_features(t))
    return (np.array(feats), get_other_feature_names())

def import_from_csv(data_location):
   csv_data = pd.read_csv(data_location) 
   return data
   

def get_tf_vector(input):
   tf_vector = tf_vectorizor.fit_transform(input).toarray()
   return tf_vector
   
def get_other_feature_names():
   return ["FKRA", "FRE","num_syllables", "avg_syl_per_word", "num_chars",          
      "num_chars_total", \
      "num_terms", "num_words", "num_unique_words", "vader neg","vader pos","vader neu", \
      "vader compound", "num_hashtags", "num_mentions", "num_urls", "is_retweet"]
   
def get_pos_tfidf_vector(tweets, preprocess, tokenizer):
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
    
   tweet_tags = get_pos_vector(tweets, preprocess, tokenizer)
    
   # pos is the numerical tf matrix 
   pos = pos_vectorizer.fit_transform(pd.Series(tweet_tags)).to_array()
    
   # pos_vocab is the vocabulary dictionary that holds the possible parts of speech combos
   pos_vocab = {v:i for i, v in enumerate(pos_vectorizer.get_feature_names())}
    
   return (pos, pos_vocab)
   
   
# expects the tf vector as input, preprocess should be a defined function 
#  
def get_tfidf_vector(tweets, tokenize, preprocess):
   
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
    
   return (tfidf, vocab)
   
def get_pos_vector(tweets, preprocess, basic_tokenize):
   tweet_tags = []
   
   for tweet in tweets:
      tokens = basic_tokenize(preprocess(tweet))
      tags = nltk.pos_tag(tokens)
      tag_list = [x[1] for x in tags]
      tag_str = " ".join(tag_list)
      tweet_tags.append(tag_str)
   
   return tweet_tags
      
   
def get_pos_vector_spacy(tweets):
   tokens = []
   tweet_tags = []
   docs = []
   
   for tweet in tweets:
      doc = nlp(tweet)
      docs.append(doc)
         
      tag_list = [x.tag_ for x in doc]
      tag_str = "".join(tag_list)
      tweet_tags.append(tag_str)
      
   return tweet_tags
   
def get_training_features():
   vectorizer = CountVectorizer(stor_words = "english",
                                preprocessor = clean_text)
   training_features = vectorizer.fit_transform(train_data["text"])
   pass
   
   
def get_SVM_model(training_features, train_data):
   model = LinearSVC()
   model.fit(training_features, train_data["setiment"])
   return model
   
