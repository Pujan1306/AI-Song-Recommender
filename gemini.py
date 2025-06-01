import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

class SongRecommender:
    def __init__(self):
        self.api_key = os.getenv("GOOGLE_API_KEY")
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def GenerateSong(self, prompt): 
        self.response = self.model.generate_content(prompt)
        return self.response.text