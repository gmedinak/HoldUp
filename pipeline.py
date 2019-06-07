import preprocess.py


def get_features_basik(df):
   tweets = df.tweet
   
   variable_tfidf = get_tfid_vector(tweets, tokenize, preprocess)

   pos_ifidf, pos_vocab = get_pos_tfidf_vector(tweets, tokenize, preprocess)
   
   other_features = get_feature_array(tweets)
   
   M = np.concatenate([tfidf,pos,feats],axis=1)
   
   #Finally get a list of variable names
   variables = ['']*len(vocab)
   for k,v in vocab.items():
       variables[v] = k

   pos_variables = ['']*len(pos_vocab)
   for k,v in pos_vocab.items():
       pos_variables[v] = k

   feature_names = variables+pos_variables+other_features_names
   
   return M, feature_names

def get_features(preprocess, tokenize, baisc_tokenize, ):

   df = pd.read_csv("../data/labeled_data.csv")
   
   M, feature_names = get_features_basik(df)
   
   pass
   
   




if __name__ == '__main__':


   pass