import pytesseract
import vertexai
from vertexai.language_models import TextGenerationModel

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/workspaces/python/google_service.json"


image_path = "/workspaces/python/struk7.jpeg"
text = pytesseract.image_to_string(image_path, lang="ind")

vertexai.init(project="gits-datawarehouse", location="us-central1")
parameters = {
    # "candidate_count": 1,
    "max_output_tokens": 256,
    "temperature": 0.2,
    "top_p": 0.8,
    "top_k": 40
}
model = TextGenerationModel.from_pretrained("text-bison@001")
response = model.predict(
  f"""
  Kamu adalah seorang developer senior,
  Menerjemahkan struk belanja menjadi JSON.

  Args:
    text: {text}

  Returns:
    Objek JSON yang berisi hasil terjemahan.
  """,
  **parameters
  )

print(f"Response from Model: {response.text}")