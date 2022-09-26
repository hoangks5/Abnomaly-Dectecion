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
    s = pd.read_csv('./BTC_USD.csv', index_col="Date", parse_dates=True, squeeze=True)
    from adtk.data import validate_series
    s = validate_series(s)
    return {"Result": "OK"}
    
  