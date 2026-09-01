from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def read_root():
    return{"status": "ok", "message": "API and bot are activated"}

@router.get("/status")
async def check_status():
    return {"bot_active": True}