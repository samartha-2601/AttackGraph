from fastapi import FastAPI

app = FastAPI(
    title="AttackGraph AI",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "message": "AttackGraph AI API Running"
    }