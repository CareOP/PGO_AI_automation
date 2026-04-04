import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class SymptomAgent:
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        
        self.system_instruction = (
            "You are a professional Medical Information Assistant for the PharmaGO platform. "
            "1. ALWAYS start with a medical disclaimer: 'I am an AI, not a doctor.' "
            "2. If symptoms suggest an emergency (chest pain, breathing issues), urge immediate ER visit. "
            "3. Analyze symptoms and suggest potential topics for the user to discuss with a doctor. "
            "4. Never provide a final diagnosis."
        )
        
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=self.system_instruction
        )

    def get_assessment(self, symptoms: str):
        chat = self.model.start_chat(history=[])
        response = chat.send_message(f"User reports these symptoms: {symptoms}")
        return response.text

# Initialize a single instance to be used by the API
agent = SymptomAgent()