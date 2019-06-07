import pandas as pd
import Preprocess as pp
import learning as learn
import vectorization as vec


def get_features_basik(df):
   tweets = df.tweet
   
   variable_tfidf = vec.get_tfidf_vector(tweets, pp.tokenize, pp.preprocess)

   pos_ifidf, pos_vocab = vec.get_pos_tfidf_vector(tweets, pp.tokenize, pp.preprocess)
   
   other_features = vec.get_feature_array(tweets)
   
   M = np.concatenate([tfidf,pos,feats],axis=1)
   
   #Finally get a list of variable names
   variables = ['']*len(vocab)
   for k,v in vocab.items():
       variables[v] = k

   pos_variables = ['']*len(pos_vocab)
   for k,v in pos_vocab.items():
       pos_variables[v] = k

   feature_names = variables+pos_variables+other_features_names
   
   return (M, feature_names)

def get_features(preprocess, tokenize, baisc_tokenize):

   df = pd.read_csv("./labeled_data.csv")
   
   M, feature_names = get_features_basik(df)
   
   pass
   
   




if __name__ == '__main__':
   df = pd.read_csv("./labeled_data.csv")
   
   M, feature_names = get_features_basik(df)
   
   report = learn.gridSearch_learn(M, df)
   
   print(report)

   pass