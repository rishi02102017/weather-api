# from fastapi import FastAPI
# import requests

# app = FastAPI()

# API_KEY = "15af3ee11bac5d595a022d0546641032"  

# @app.get("/weather/")
# def get_weather(city: str):
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
#     response = requests.get(url)
    
#     if response.status_code != 200:
#         return {"error": "Invalid city or API issue"}

#     data = response.json()
#     return {
#         "city": data["name"],
#         "temperature": data["main"]["temp"],
#         "weather": data["weather"][0]["description"],
#         "humidity": data["main"]["humidity"]
#     }

# from fastapi import FastAPI
# import requests

# app = FastAPI()

# # Root path - Home Page
# @app.get("/")
# def home():
#     return {"message": "Weather API is up! Use /weather?city=Delhi"}

# # Weather API
# API_KEY = "15af3ee11bac5d595a022d0546641032"

# @app.get("/weather/")
# def get_weather(city: str):
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
#     response = requests.get(url)
    
#     if response.status_code != 200:
#         return {"error": "Invalid city or API issue"}

#     data = response.json()
#     return {
#         "city": data["name"],
#         "temperature": data["main"]["temp"],
#         "weather": data["weather"][0]["description"],
#         "humidity": data["main"]["humidity"]
#     }



from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import requests
import os

# Initialize FastAPI
app = FastAPI()

# Database Setup
DATABASE_URL = "sqlite:///./weather.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Weather Data Model
class Weather(Base):
    __tablename__ = "weather"
    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, index=True)
    temperature = Column(Float)
    weather = Column(String)
    humidity = Column(Integer)

# Create Database Tables
Base.metadata.create_all(bind=engine)

# Dependency to get DB Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# OpenWeatherMap API Key (Use Render Environment Variable)
API_KEY = os.getenv("15af3ee11bac5d595a022d0546641032")

# Root Route
@app.get("/")
def home():
    return {"message": "Weather API is up! Use /weather?city=Delhi"}

# Fetch & Store Weather Data
@app.get("/weather/")
def get_weather(city: str, db: Session = Depends(get_db)):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Invalid city or API issue")

    data = response.json()
    weather_data = Weather(
        city=data["name"],
        temperature=data["main"]["temp"],
        weather=data["weather"][0]["description"],
        humidity=data["main"]["humidity"]
    )

    # Store data in DB
    db.add(weather_data)
    db.commit()
    db.refresh(weather_data)

    return weather_data

# Get Stored Weather Data
@app.get("/weather/history/")
def get_weather_history(db: Session = Depends(get_db)):
    return db.query(Weather).all()

# Delete a Weather Record
@app.delete("/weather/delete/{city}")
def delete_weather(city: str, db: Session = Depends(get_db)):
    record = db.query(Weather).filter(Weather.city == city).first()
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    
    db.delete(record)
    db.commit()
    return {"message": f"Deleted weather record for {city}"}
