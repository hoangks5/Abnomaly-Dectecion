import adtk.data
import pandas as pd

s_train = pd.read_csv("./BTC_USD.csv", index_col="Datetime", parse_dates=True, squeeze=True)

s_train = validate_series(s_train)
>>> print(s_train)