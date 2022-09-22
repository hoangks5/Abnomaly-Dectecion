import pandas as pd
s = pd.read_csv('./BTC_USD.csv', index_col="Date", parse_dates=True, squeeze=True)
from adtk.data import validate_series
s = validate_series(s)