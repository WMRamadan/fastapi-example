from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# In memory database
db = []

class Car(BaseModel):
    name: str

@app.get('/')
def index():
    return {'key' : 'value'}

@app.get('/cars')
def get_cars():
    return db

@app.get('/cars/{car_id}')
def get_car(car_id: int):
    return db[car_id-1]

@app.post('/cars')
def create_car(car: Car):
    db.append(car.dict())
    return db[-1]

@app.put('/cars/{car_id}')
def update_car(car_id: int, car: Car):
    db[car_id-1] = car.dict()
    return db

@app.delete('/cars/{car_id}')
def delete_car(car_id: int):
    db.pop(car_id-1)
    return db
