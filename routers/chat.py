from fastapi import APIRouter

from schemas import ChatRequest
from services.depo_store import search_products

router = APIRouter()

@router.options("/chat")
async def chat_options():
    return {}

@router.post("/chat")
async def chat(payload: ChatRequest):
    results = await search_products(payload.message)
    return {"message": results}
