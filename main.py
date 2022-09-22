import pandas as pd
s = pd.read_csv('./BTC_USD.csv', index_col="Date", parse_dates=True, squeeze=True)
from adtk.data import validate_series
s = validate_series(s)

from adtk.detector import ThresholdAD
threshold_ad = ThresholdAD(high=50000, low=30000)
anomalies = threshold_ad.detect(s)
from adtk.visualization import plot
t = plot(s, anomaly=anomalies, ts_linewidth=1, ts_markersize=3, anomaly_markersize=5, anomaly_color='red', anomaly_tag="marker")
from matplotlib import pyplot as plt
plt.savefig('foo.png')