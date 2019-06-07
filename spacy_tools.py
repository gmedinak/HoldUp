import spacy
nlp = spacy.load("en_core_web_sm")

def tokenize_spacy(tweet):
    doc = nlp(tweet)
    return [token.text for token in doc]

def tokenize_stemming_spacy(tweet):
    doc = nlp(tweet)
    return [token.lemma_ for token in doc]

def pos_basic_spacy(tweet):
    doc = nlp(tweet)
    return [token.pos_ for token in doc]

def pos_detailed_spacy(tweet):
    doc = nlp(tweet)
    return [token.tag_ for token in doc]

def full_spacy(tweet):
    doc = nlp(tweet)
    return [ [token.text, token.lemma_, token.pos_, token.tag_] for token in doc]

if __name__=="__main__":
    s = "flying is a cool way to see the Earth."
    print(tokenize_spacy(s))
    print(tokenize_stemming_spacy(s))
    print(pos_basic_spacy(s))
    print(pos_detailed_spacy(s))
    print(full_spacy(s))