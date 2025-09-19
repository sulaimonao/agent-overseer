import subprocess, shlex

def search(keyword: str, max_lines: int = 200):
    # macOS: unified logs often via `log show`; for portability we use grep on /var/log
    try:
        cmd = f"grep -iR --line-number --binary-files=without-match -m {max_lines} {shlex.quote(keyword)} /var/log 2>/dev/null"
        out = subprocess.check_output(cmd, shell=True, timeout=5_000).decode("utf-8", "replace")
        return {"ok": True, "matches": out.splitlines()[:max_lines]}
    except subprocess.CalledProcessError:
        return {"ok": True, "matches": []}
    except Exception as e:
        return {"ok": False, "error": str(e)}
