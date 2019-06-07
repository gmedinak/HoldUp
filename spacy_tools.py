import spacy
nlp = spacy.load("en_core_web_sm")

def tokenize_spacy(tweet):
    doc = nlp(tweet)
    return [token.text for token in doc]

def tokenize_stemming_spacy(tweet):
    doc = nlp(tweet)
    return [token.lemma_ for token in doc]

# see "POS" in https://spacy.io/api/annotation#pos-tagging
def pos_basic_spacy(tweet):
    doc = nlp(tweet)
    return [token.pos_ for token in doc]

# see "TAG" in https://spacy.io/api/annotation#pos-tagging
def pos_detailed_spacy(tweet):
    doc = nlp(tweet)
    return [token.tag_ for token in doc]

def named_entity_tokens_spacy(tweet):
    doc = nlp(tweet)
    return [token.ent_type_ for token in doc]

def named_entity_natural_spacy(tweet):
    doc = nlp(tweet)
    return [[token.text, token.label_] for token in doc.ents]

def full_spacy(tweet):
    doc = nlp(tweet)
    return [ [token.text, token.lemma_, token.pos_, token.tag_] for token in doc]

if __name__=="__main__":
    s  = "Pit Bulls Photographed As Lovely Fairy Tale Creatures  "
    ss = "Gucci Mane in jail and dropping mixtapes every month and you hoes can't even text back"
    print(tokenize_spacy(s))
    #print(tokenize_stemming_spacy(s))
    #print(pos_basic_spacy(s))
    #print(pos_detailed_spacy(s))
    print(named_entity_natural_spacy(ss))
    print(named_entity_tokens_spacy(ss))
    #print(full_spacy(s))