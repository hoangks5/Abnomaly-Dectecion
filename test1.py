from fastapi import FastAPI, File, UploadFile
import pandas as pd
import matplotlib.pyplot as plt
import csv
import datetime as dt
import aiofiles
app = FastAPI()


@app.post("/")
async def post_endpoint(in_file: UploadFile=File(...)):
    # ...
    async with aiofiles.open('ok.csv', 'wb') as out_file:
        content = await in_file.read()  # async read
        await out_file.write(content)  # async write
    import pandas as pd
    s = pd.read_csv('./ok.csv', index_col="Date", parse_dates=True, squeeze=True)
    from adtk.data import validate_series
    s = validate_series(s)
    
    from adtk.detector import ThresholdAD
    threshold_ad = ThresholdAD(high=50000, low=30000)
    anomalies = threshold_ad.detect(s)
    from adtk.visualization import plot
    plot(s, anomaly=anomalies, ts_linewidth=1, ts_markersize=3, anomaly_markersize=5, anomaly_color='red', anomaly_tag="marker");
    plt.savefig('foo.png')
    return {"Result": "OK"}
    
  