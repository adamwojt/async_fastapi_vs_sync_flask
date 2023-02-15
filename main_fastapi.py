from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/")
async def root():
    await asyncio.sleep(1)
    return {"message": "Hello World"}
