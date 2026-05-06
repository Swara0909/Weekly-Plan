from fastapi import FastAPI

app = FastAPI()

@app.get("/keywords")
def extract_keywords(text: str):
    words = text.lower().split()

    # remove common words
    stopwords = ["is", "the", "and", "a", "to"]
    keywords = [word for word in words if word not in stopwords]

    return {
        "keywords": keywords
    }