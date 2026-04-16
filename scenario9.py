import json
from google import genai

client = genai.Client(api_key="AQ.Ab8RN6I6zl9-oCrqCi6eyD1WCgnfxobABhS0gUtfyB0Nsxdhng")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Return only JSON with 3 benefits of Python for data science."
)

text = response.text.strip()

try:
    result = json.loads(text)
except:
    result = {
        "error": "Invalid JSON response",
        "raw_output": text
    }

print(result)