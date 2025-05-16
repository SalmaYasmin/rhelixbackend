from pydantic import BaseModel, Field
from typing import List, Optional

class HealthSurvey(BaseModel):
    name: str
    age_sex: str
    address: str
    occupation: str
    phone_number: str
    past_medical_history: List[str]
    other_medical_history: Optional[str] = ""
    past_medical_admissions: Optional[str] = ""
    past_surgical_history: Optional[str] = ""
    addictions: List[str]
    diet: List[str]
    disease_increase_opinion: Optional[str] = ""
    disease_increase_reason: Optional[str] = ""
    group_participation_interest: Optional[str] = ""
