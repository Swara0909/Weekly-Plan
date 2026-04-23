from fastapi import FastAPI

app = FastAPI()

@app.get("/count")
def count_words(text: str):
    words = text.split()
    return {
        "text": text,
        "word_count": len(words)
    }