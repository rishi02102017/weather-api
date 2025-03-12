from fastapi import FastAPI
import requests

app = FastAPI()

API_KEY = "15af3ee11bac5d595a022d0546641032"  

@app.get("/weather/")
def get_weather(city: str):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code != 200:
        return {"error": "Invalid city or API issue"}

    data = response.json()
    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "weather": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"]
    }
