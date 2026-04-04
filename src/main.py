from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.agent import agent

app = FastAPI(title="PharmaGO AI Assessment API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, replace with your frontend URL
    allow_methods=["*"],
    allow_headers=["*"],
)

class SymptomRequest(BaseModel):
    symptoms: str

@app.post("/assess")
async def assess_symptoms(request: SymptomRequest):
    if not request.symptoms:
        raise HTTPException(status_code=400, detail="Symptoms description is required")
    
    try:
        result = agent.get_assessment(request.symptoms)
        return {"assessment": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)