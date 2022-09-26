from fastapi import FastAPI, File, UploadFile
import pandas as pd
import matplotlib.pyplot as plt
app = FastAPI()


@app.post("/upload")
def upload(file: UploadFile = File(...)):
    contents = file.file.read()
    t = contents.decode("utf-8")
    print(type(t))
    return 0
  