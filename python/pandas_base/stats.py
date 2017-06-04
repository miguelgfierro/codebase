from __future__ import print_function
import pandas as pd
import numpy as np

if __name__ == "__main__":
    df = pd.DataFrame({'col1':[1,2,3],
                       'col2':[0.1,np.nan,0.3],
                       'col3':[10,20,30]})

    print(df.max())
    print(df['col1'].min())
    print(df.mean())
    print(df.shape)
    print(df['col2'].count())
    print(df.sum())
    print(df.clip(lower=1, upper=10))
    print(df.describe())



