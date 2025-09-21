from fastapi import FastAPI , Query
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware


class BMI_output(BaseModel):
    bmi :float 
    message: str
# create app api 
app = FastAPI()


# FastAPI CORS snippet
app.add_middleware(
CORSMiddleware,
allow_origins=["*"],#"http://127.0.0.1:5500", "http://localhost:5500"
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)



#choose a path
@app.get('/calculate_bmi')
#function for a precedent path
def calculate_bmi(
    weight : float = Query(...,gt=20 ,lt=200, description="KG") ,
    height: float = Query(...,gt=1 ,lt=3, description="Metre")):
    bmi = weight /(height**2)
    if bmi < 18.5:
        message = "underweight" 
    elif 18.5 <= bmi < 30:
        message = "Normal Weight"
    elif 25 <= bmi < 30:
        message = "Overweight"
    elif 30 <= bmi < 35:
        message = "Obesity (Class I)"
    else:
        message = "Extreme Obesity (Class III)"
    return BMI_output(bmi = bmi , message = message)