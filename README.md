
# **Library**

- `pytesseract` untuk membaca teks dari gambar.
- `vertexai` untuk mengakses model bahasa Vertex AI.
- `TextGenerationModel` untuk menghasilkan teks menggunakan model bahasa Vertex AI.

# **Tools**

- Google Cloud Platform Console untuk mengelola sumber daya Vertex AI.
- Google Cloud SDK untuk menjalankan perintah Vertex AI dari terminal.

# **Code**

```
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

```

# **Penjelasan**

Skrip ini menggunakan model bahasa Vertex AI untuk menerjemahkan struk belanja menjadi JSON. Model bahasa Vertex AI dilatih pada dataset teks yang besar, sehingga dapat menghasilkan teks yang akurat dan informatif.

Untuk menggunakan skrip ini, Anda perlu menginstal library `pytesseract` dan `vertexai`. Anda juga perlu memiliki kredensial Google Cloud Platform yang valid dan proyek Vertex AI yang aktif.

Setelah Anda menginstal library yang diperlukan dan menyiapkan kredensial Google Cloud Platform, Anda dapat menjalankan skrip dengan perintah berikut:

```
python translate_receipt_to_json.py
```

Skrip akan meminta Anda untuk memasukkan path ke gambar struk belanja. Setelah Anda memasukkan path ke gambar, skrip akan menerjemahkan teks dari gambar menjadi JSON dan mencetaknya ke konsol.


```
{
  "tanggal": "2023-09-25",
  "toko": "Toko Sembako",
  "alamat": "Jl. Sudirman No. 1, Bandung",
  "item": [
    {
      "nama": "Beras",
      "harga": 10000,
      "jumlah": 1
    },
    {
      "nama": "Gula",
      "harga": 5000,
      "jumlah": 2
    },
    {
      "nama": "Minyak goreng",
      "harga": 12000,
      "jumlah": 1
    }
  ],
  "total": 37000
}
```
