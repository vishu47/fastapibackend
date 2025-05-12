from fastapi import FastAPI
from typing import List
from pydantic import BaseModel


app = FastAPI()


# add modal here or schema
class Tea(BaseModel):
    id : int
    name : str
    content : str
    
# for storing the data
teas: List[Tea] = [] 


@app.get("/")
def Landing_Home():
    return {"Welcome to the Teas house"}

@app.get("/teas")
def get_Teas():
    return teas

@app.post("/teas/")
def add_Teas(tea : Tea):
    teas.append(tea)
    return { "msg" : "added successfully" , "data" : tea}
    

@app.put("/teas/{tea_id}")
def update_Teas(tea_id : int , tea_data : Tea):
    for index , tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = tea_data
            return { "msg" : "updated successfully" , "data" : tea_data}
    
    return { "msg" : "data not found"}
    
    

@app.delete("/teas/{tea_id}")
def delete_Teas(tea_id : int):
    for index , tea in enumerate(teas):
        if tea.id == tea_id:
            deleted = teas.pop(index)
            return { "msg" : "deleted successfully" , "data" : deleted}
    
    return { "msg" : "data not found"}
    


    
