from ...storage import db

def plan(steps: list) -> dict:
    """
    steps: [{"cmd": "rm -rf ...", "why": "...", "risk": "low/med/high"}]
    Returns a confirm token (echoed back on execute).
    """
    token = "CONFIRM-"
    token += str(abs(hash(str(steps))))[:10]
    db.log_op("agent", "plan", detail=str(steps), confirmed=0)
    return {"ok": True, "confirm_token": token, "steps": steps}

def execute(confirm_token: str, steps: list) -> dict:
    # Starter: dry-run only. Wire real executor later with guards.
    db.log_op("user", "confirm", detail=confirm_token, confirmed=1)
    return {"ok": True, "executed": False, "note": "Starter repo runs dry-run only. Wire real executor later."}
