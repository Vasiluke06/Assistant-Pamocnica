from fastapi import FastAPI

from api.routes import router as api_router

app = FastAPI(title="Assistant Pamocnica API")

app.include_router(api_router)

#Start: uvicorn main:app --reload