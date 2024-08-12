import google.generativeai as genai

class CallingGemini:
    def __init__(self) -> None:
        GOOGLE_API_KEY='AIzaSyAMXx8dgR60VY7rO2BcSN-RymAomxfksco'
        genai.configure(api_key=GOOGLE_API_KEY)
        self.model = genai.GenerativeModel('models/gemini-pro')

    def creating_response(self, ques):
        try:
            tunned_ques = f"Answer conditions: 1. Do not reveal that you are an AI in your response 2. Keep all answers within one sentence | Question: '{ques}'"
            response = self.model.generate_content(tunned_ques)
            candidate = response._result.candidates[0]
            part = candidate.content.parts[0]
            text = part.text
            return text
        except IndexError:
            return "Please use beautiful and kind words."