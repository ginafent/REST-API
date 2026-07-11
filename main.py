from fastapi import FastAPI

main = FastAPI()

@main.get("/health")
def health_check():
    return {"status": "ok"}
