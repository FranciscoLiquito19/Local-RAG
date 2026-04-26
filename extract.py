import fitz  # pymupdf
import os

doc = fitz.open("docs/" + os.listdir("docs")[0])
text = ""
for page in doc:
    text += page.get_text()

with open("docs/documento.txt", "w") as f:
    f.write(text)

print(f"Extraído: {len(text)} caracteres")
print(text[:500])  # mostra os primeiros 500 chars
