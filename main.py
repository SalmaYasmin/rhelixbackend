from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from models import HealthSurvey
from motor.motor_asyncio import AsyncIOMotorClient
import os

app = FastAPI()

MONGO_DETAILS = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGO_DETAILS)
db = client.health_survey_db
collection = db.surveys

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify your frontend URL(s)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"Incoming request: {request.method} {request.url}")
    response = await call_next(request)
    return response

@app.post("/submit")
async def submit_survey(survey: HealthSurvey):
    survey_dict = survey.dict()
    print("Received survey data:", survey_dict)
    result = await collection.insert_one(survey_dict)
    if result.inserted_id:
        return {"message": "Survey submitted successfully!"}
    raise HTTPException(status_code=500, detail="Failed to submit survey")
