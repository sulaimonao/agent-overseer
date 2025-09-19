from pathlib import Path

SAFE_MAX_BYTES = 200_000

def read_text(path: str) -> dict:
    p = Path(path).expanduser().resolve()
    # Basic guardrails
    if any(seg.startswith('.') for seg in p.parts[-2:]):
        return {"ok": False, "error": "Refusing to read hidden or dotfiles without explicit allow."}
    if not p.exists() or not p.is_file():
        return {"ok": False, "error": "File does not exist or not a regular file."}
    data = p.read_bytes()[:SAFE_MAX_BYTES]
    try:
        txt = data.decode('utf-8', errors='replace')
    except Exception as e:
        return {"ok": False, "error": f"Decode error: {e}"}
    return {"ok": True, "path": str(p), "text": txt, "truncated": len(data)==SAFE_MAX_BYTES}
