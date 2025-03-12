# **Weather API - FastAPI Project**

## **Overview**
A simple **FastAPI-based Weather API** that fetches real-time weather data using the **OpenWeatherMap API** and supports **CRUD operations** using an SQL database. The API is **deployed on Render**.

---

## **Features**
- ✅ Get **current weather** by city name.
- ✅ **5-day forecast** (optional).
- ✅ **Store user queries** in an SQL database.
- ✅ **CRUD operations** for stored weather data.
- ✅ **FastAPI + Uvicorn backend**.
- ✅ **Deployed on Render** for public access.

---

## **How to Run Locally**
1️⃣ **Clone the repository**:
   ```bash
   git clone https://github.com/rishi02102017/weather-api.git
   ```
   
2️⃣ **Navigate to the project folder**:
   ```bash
   cd weather-api
   ```
   
3️⃣ **Create & activate a virtual environment**:
   ```bash
   python -m venv env
   # Windows
   env\Scripts\activate
   # macOS/Linux
   source env/bin/activate
   ```

4️⃣ **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5️⃣ **Run the FastAPI server**:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

6️⃣ **Access API Docs**:
   - Open **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)** in your browser.

---

## **CRUD Operations for Stored Weather Data**
The API stores weather queries in an SQL database and supports **CRUD operations**:

- **Create:** Store a weather query.
- **Read:** Retrieve stored weather data.
- **Update:** Modify a stored query.
- **Delete:** Remove a stored query.

---

## **Deployment on Render**
The API is deployed on **Render**, making it accessible online.

### **How to Deploy on Render**
1. **Push all changes to GitHub**:
   ```bash
   git add .
   git commit -m "Updated API with CRUD operations"
   git push origin main
   ```

2. **Visit [Render](https://render.com)** and create a new web service.
3. **Connect the GitHub repository** and select the `main` branch.
4. **Set environment variables**:
   - `API_KEY`: Your OpenWeatherMap API key.
5. **Deploy & test the live API**.

---

## **Live API URL**
You can access the deployed API at:

```
https://your-weather-api-onrender.com
```

 **Test Endpoints:**
- **Docs:** [https://your-weather-api-onrender.com/docs](https://your-weather-api-onrender.com/docs)
- **Get Weather:** `https://your-weather-api-onrender.com/weather?city=Delhi`

---

## **Technologies Used**
- **FastAPI** - Backend framework
- **Uvicorn** - ASGI server
- **SQLAlchemy** - Database ORM
- **SQLite** - Local database storage
- **Render** - Cloud deployment

---

