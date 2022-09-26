from fastapi import FastAPI, File, UploadFile
import pandas as pd
import matplotlib.pyplot as plt
import csv
app = FastAPI()


@app.post("/upload")
def upload(file: UploadFile = File(...)):
    contents = file.file.read()
    contents = contents.decode("utf-8")
    csv_data = csv.reader(contents)
    print(csv_data)
    return 0
  