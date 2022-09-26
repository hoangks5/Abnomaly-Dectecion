from fastapi import FastAPI, File, UploadFile
import pandas as pd
import matplotlib.pyplot as plt
import csv
app = FastAPI()


@app.post("/upload")
def upload(file: UploadFile = File(...)):
    x = []
    contents = file.file.read().splitlines()
    for line in contents[1:]:
        line.split(',')[1]
  