import nltk
import re
from nltk.stem.porter import *

stopwords=stopwords = nltk.corpus.stopwords.words("english")

other_exclusions = ["#ff", "ff", "rt"]
stopwords.extend(other_exclusions)

stemmer = PorterStemmer()

def tokenize_nltk(tweet):
   tokens = nltk.word_tokenize(tweet)
   return tokens

# Tokenize and converts each token into word stem
# Example of this - processing -> process
def tokenize_stemming(tweet):
   tweet_t = " ".join(re.split("[^a-zA-Z]*\s", tweet.lower())).strip()
   tokens = [stemmer.stem(t) for t in tweet_t.split()]
   return tokens
   
# No stemming
def tokenize_no_stemming(tweet):
   tweet_t = " ".join(re.split("[^a-zA-Z.,!?]*", tweet.lower())).strip()
   return tweet.split()
   
def preprocess(text_string):
   """
   Accepts a text string and replaces:
   1) urls with URLHERE
   2) lots of whitespace with one instance
   3) mentions with MENTIONHERE

   This allows us to get standardized counts of urls and mentions
   Without caring about specific people mentioned
   """
   space_pattern = '\s+'
   giant_url_regex = ('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|'
       '[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
   mention_regex = '@[\w\-]+'
   parsed_text = re.sub(space_pattern, ' ', text_string)
   parsed_text = re.sub(giant_url_regex, '', parsed_text)
   parsed_text = re.sub(mention_regex, '', parsed_text)
   return parsed_text