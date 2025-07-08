import requests

text = """Your long article or paragraph goes here. Make sure it has enough content to be summarized effectively by the model."""
res = requests.post("http://127.0.0.1:5000/summarize", json={"text": text})
print("Summary:", res.json())
