from fastapi import FastAPI, File, UploadFile
import pandas as pd
import matplotlib.pyplot as plt
import csv
app = FastAPI()


@app.post("/upload")
def upload(file: UploadFile = File(...)):
    contents = file.file.read()
    for line in contents[1:]:
  