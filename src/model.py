import pandas as pd
import lightgbm as lgb

from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

from functions import MultiColumnLabelEncoder
import config

import pickle

df = pd.read_csv('data/aug_train.csv')

X_aug_train = df.drop('target', axis = 'columns')
y = df['target']


cat_features = X_aug_train.select_dtypes(['object']).columns.to_list()

# use MultiColumnLabelEncoder to apply LabelEncoding on cat_features 
# uses NaN as a value , no imputation will be used for missing data
X_aug_train_transform = MultiColumnLabelEncoder(columns = cat_features).fit_transform(X_aug_train)


train_x, valid_x, train_y, valid_y = train_test_split(X_aug_train_transform.drop('enrollee_id',axis = 'columns'), y, test_size=0.2, shuffle=True, stratify=y, random_state=20210303)

train_data=lgb.Dataset(train_x,label=train_y, categorical_feature = cat_features)
valid_data=lgb.Dataset(valid_x,label=valid_y, categorical_feature = cat_features)

# Train model on selected parameters and number of iterations
lgbm = lgb.train(config.params,
                 train_data,
                 2500,
                 valid_sets=valid_data,
                 early_stopping_rounds= 30,
                 verbose_eval= 10)

try:
    pickle.dump(lgbm, open('hr_ds-lgbm-model.ml', 'wb'))
    print('---- Se pudo almacenar el modelo exitosamente ----')
except:
     print('---- No se pudo generar el modelo ----')