from fastapi import FastAPI
import json


app = FastAPI()

def GetJsonData():
    with open('data/data.json', 'r') as f:
        return json.load(f)


@app.get('/')
def getHome():
    return {"name" : "my name is vishnu"}

@app.get("/getdata")
def getData():
    data = GetJsonData()
    return data
    