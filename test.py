from fastapi import FastAPI, File, UploadFile
import pandas as pd
import matplotlib.pyplot as plt
app = FastAPI()


@app.post("/upload")
def upload(file: UploadFile = File(...)):
    contents = file.file.read()

    contents.to_csv('GeeksforGeeks.csv', 
                  index = None)
    return contents.splitlines()[1]
  