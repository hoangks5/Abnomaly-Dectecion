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
    async with aiofiles.open(in_file.filename, 'wb',encoding='utf-8') as out_file:
        content = await in_file.read()  # async read
        await out_file.write(content)  # async write

    return {"Result": "OK"}
    
  