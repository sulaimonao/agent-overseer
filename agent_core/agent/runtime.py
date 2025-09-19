import os, httpx, json
from .prompts import SYSTEM_PROMPT, TOOL_POLICY
from .tools import TOOLS

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://127.0.0.1:11434")
MODEL_ID = os.getenv("MODEL_ID", "gpt-oss:20b-q4_0")

async def chat(messages, tools=None):
    """
    Minimal Ollama-compatible chat call.
    For tool-calls, we look for a JSON blob like {"tool":"sys_info.snapshot","args":{}} in assistant content.
    """
    prompt = SYSTEM_PROMPT + "\n\n" + TOOL_POLICY
    payload = {"model": MODEL_ID, "messages": [{"role":"system","content":prompt}] + messages}
    async with httpx.AsyncClient(timeout=120) as client:
        r = await client.post(f"{OLLAMA_HOST}/api/chat", json=payload)
        r.raise_for_status()
        data = r.json()
    return data

def maybe_handle_toolcall(text: str):
    try:
        obj = json.loads(text)
        tool = obj.get("tool"); args = obj.get("args",{})
        if tool in TOOLS:
            return {"tool_result": TOOLS[tool](**args)}
    except Exception:
        pass
    return None
