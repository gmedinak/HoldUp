from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold, GridSearchCV
from sklearn.pipeline import Pipeline


def gridSearch_learn(features_M, df):
   x = pd.DataFrame(features_M)
   y = df['class'].astype(int)
   
   x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.1)
   
   pipe = Pipeline(
     [('select', SelectFromModel(LogisticRegression(class_weight='balanced',
                                               penalty="l1", C=0.01))),
     ('model', LogisticRegression(class_weight='balanced',penalty='l2'))])

   param_grid = [{}]
   
   grid_search = GridSearchCV(pipe, 
      param_grid,
      cv=StratifiedKFold(n_splits=5, 
                         random_state=42).split(X_train, y_train), 
      verbose=2)
      
   model = grid_search.fit(x_train, y_train)
   
   y_predicts = model.predict(x_test)
   
   report = classification_report(y_test, y_predicts)
   
   return report