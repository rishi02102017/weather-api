# Weather API - FastAPI Project

## Overview
A simple FastAPI-based weather API that fetches real-time weather data using OpenWeatherMap API.

## Features
- Get current weather by city name
- 5-day forecast (optional)
- Error handling for invalid inputs
- FastAPI + Uvicorn backend

## How to Run
1. Clone the repo:
   git clone https://github.com/rishi02102017/weather-api.git
2. Navigate to the project folder:
   cd weather-api
3. Install dependencies:
   pip install -r requirements.txt
4. Run the FastAPI server:
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
5. Access API Docs:
   Open: **http://127.0.0.1:8000/docs**
    
