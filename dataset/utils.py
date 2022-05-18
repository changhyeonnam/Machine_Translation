import pandas as pd
from sklearn.model_selection import train_test_split
def split_dataset(df:pd.DataFrame):
    '''
    split dataset in to train, valid, testset.
    default ratio : 1400,000 : 190,000 : 10000

    len(total_df):1602418
    len(train_df):1402115, len(test+val):200303
    len(val_df):190287, len(test_df):10016

    :return: [train, valid, test]
    '''
    train_df, tmp_df, _, _ = train_test_split(df, df['en'], test_size = 0.125, random_state = 42, shuffle=True)
    print(f'len(train_df):{len(train_df)}, len(test+val):{len(tmp_df)}')
    val_df, test_df, _, _ = train_test_split(tmp_df, tmp_df['en'], test_size = 0.05, random_state = 42, shuffle=True)
    print(f'len(val_df):{len(val_df)}, len(test_df):{len(test_df)}')

    return train_df,val_df,test_df


df = pd.read_csv('total_dataset.csv')
print(f'len(total_df):{len(df)}')
train_df,val_df,test_df = split_dataset(df)
train_df.to_csv('train_data.csv',index=False)
val_df.to_csv('val_data.csv',index=False)
test_df.to_csv('test_data.csv',index=False)