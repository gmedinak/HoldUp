from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold, GridSearchCV
from sklearn.pipeline import Pipeline


def gridSearch_learn(features_M, df):
   x = pd.DataFrame(features_M)
   y = df['class'].astype(int)
   
   # Get test and training sets
   x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.1)
   
   # I don't really know what this is...
   pipe = Pipeline(
     [('select', SelectFromModel(LogisticRegression(class_weight='balanced',
                                               penalty="l1", C=0.01))),
     ('model', LogisticRegression(class_weight='balanced',penalty='l2'))])

   # Extra parameters, not entirely sure what this does
   param_grid = [{}]
   
   # I think this is the meat of the learning process, setting up the machine learning process (in this case it's grid search)
   grid_search = GridSearchCV(pipe, 
      param_grid,
      cv=StratifiedKFold(n_splits=5, 
                         random_state=42).split(X_train, y_train), 
      verbose=2)
      
   # Putting in the training data to the learning model
   model = grid_search.fit(x_train, y_train)
   
   # Getting the prediction values for particular test set
   y_predicts = model.predict(x_test)
   
   # Get a report of the results
   report = classification_report(y_test, y_predicts)
   
   return report