from mangum import Mangum 
from pydantic import BaseModel
from typing import List, Dict, Optional
from fastapi import FastAPI
import ml

app = FastAPI()
handler = Mangum(app)

@app.get("/")
def read_root():
    return {"message": 'Hey there'}


class Request(BaseModel):
    purple_data: Dict[str,float]
    sensor_id: str
    date_time: Optional[str]


@app.post("/correction")
def predict(req: Request):

    raw_purple_data = req.purple_data
    
    sensor_id = req.sensor_id
    date_time = req.date_time
    correction = ml.correct_rf(raw_purple_data,sensor_id)

    return {"correction": correction}

@app.post("/correct")
def predict():
    
    correction = ml.correct_rf_2()

    return {"correction": correction}