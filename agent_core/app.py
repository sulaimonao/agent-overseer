import os, json, asyncio
from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from .storage import db
from .agent import runtime

load_dotenv()
db.init()

app = FastAPI(title="Agent Overseer Core")

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/agent/query")
async def agent_query(payload: dict = Body(...)):
    """
    payload: { "user": "text" }
    The model can either reply directly or emit a tool-call JSON.
    """
    user_text = payload.get("user","").strip()
    msgs = [{"role":"user","content":user_text}]
    data = await runtime.chat(msgs)
    content = data.get("message",{}).get("content","")
    maybe = runtime.maybe_handle_toolcall(content)
    if maybe:
        return JSONResponse(maybe)
    return {"reply": content}
