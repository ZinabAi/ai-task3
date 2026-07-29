import cohere
import os
from dotenv import load_dotenv

load_dotenv()

co = cohere.Client(os.getenv("COHERE_API_KEY"))


def ask_llm(prompt):

    # إذا لم يلتقط Whisper كلامًا
    if not prompt.strip():
        return "I did not hear anything. Please try again."

    response = co.chat(
        model="command-r7b-12-2024",
        message=prompt
    )

    return response.text