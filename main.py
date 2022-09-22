import pandas as pd
s = pd.read_csv('./BTC_USD.csv', index_col="Date", parse_dates=True, squeeze=True)
from adtk.data import validate_series
s = validate_series(s)

from adtk.detector import ThresholdAD
threshold_ad = ThresholdAD(high=50000, low=30000)
anomalies = threshold_ad.detect(s)