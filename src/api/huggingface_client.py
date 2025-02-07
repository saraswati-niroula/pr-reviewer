import os
import time
import requests
from config import PR_REVIEW_MODEL, MAX_RESPONSE_TOKENS, MODEL_TEMPERATURE


class HuggingFaceClient:
    def __init__(self, model=PR_REVIEW_MODEL):
        self.model = model
        self.api_url = f"https://api-inference.huggingface.co/models/{model}"
        self.headers = {"Authorization": f"Bearer {os.getenv('HF_API_KEY')}"}

    def generate_review(self, prompt, max_retries=3):
        payload = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": MAX_RESPONSE_TOKENS,
                "temperature": MODEL_TEMPERATURE,
                "return_full_text": False
            }
        }

        for _ in range(max_retries):
            try:
                response = requests.post(
                    self.api_url,
                    headers=self.headers,
                    json=payload,
                    timeout=180
                )

                if response.status_code == 503:  # Model loading
                    time.sleep(10)
                    continue

                if response.status_code == 200:
                    try:
                        return response.json()[0]["generated_text"]
                    except (KeyError, IndexError):
                        return "Error: Unexpected response format."

            except requests.exceptions.Timeout:
                return "Error: Request timed out."

        return "Error: Failed to get valid response after retries"
