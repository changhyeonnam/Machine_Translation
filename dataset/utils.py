import pandas as pd
from sklearn import tra
def split_dataset(df:pd.DataFrame):
    '''
    split dataset in to train, valid, testset.
    default ratio : 1400,000 : 199,000 : 1000
    :return: [train, valid, test]
    '''


df = pd.read_csv('total_dataset.csv')
print(df.head(50))