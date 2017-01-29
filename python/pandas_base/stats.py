from __future__ import print_function
import pandas as pd
import numpy as np

if __name__ == "__main__":
    df = pd.DataFrame({'col1':[1,2,3],
                       'col2':[0.1,np.nan,0.3],
                       'col3':[10,20,30]})

    print (df.max(), "\n")
    print(df['col1'].min(), "\n")
    print(df.mean(), "\n")
    print(df.shape, "\n")
    print(df['col2'].count(),"\n")
    print(df.sum(), "\n")
    print(df.clip(lower=1, upper=10), "\n")
    print(df.describe(), "\n")



