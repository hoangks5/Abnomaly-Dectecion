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
        x.append(line.split(',')[1])
       
        y.append(line.split(',')[0])
        plt.plot(x,)
    x1 = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in x]

    import matplotlib.dates as mdates

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    plt.plot(x1,y)
    plt.gcf().autofmt_xdate()
    plt.show()
  