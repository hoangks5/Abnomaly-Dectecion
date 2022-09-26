from fastapi import FastAPI, File, UploadFile
import pandas as pd
import matplotlib.pyplot as plt
import csv
import datetime as dt
app = FastAPI()


@app.post("/upload")
def upload(file: UploadFile = File(...)):
    x = []
    y = []
    contents = file.file.read()
    contents = contents.decode("utf-8").splitlines()
    
    for line in contents[1:]:
        x.append(float(line.split(',')[1]))
       
        y.append(line.split(',')[0])
        
    
    plt.plot(range(len(x)),x)
    plt.show()
  