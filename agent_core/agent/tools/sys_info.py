import platform, socket, psutil, json
from .. import runtime
from ...storage import db

def snapshot() -> dict:
    info = {}
    info["os_name"] = platform.system()
    info["os_version"] = platform.version()
    info["hostname"] = socket.gethostname()

    users = [{"name": u.name, "terminal": u.terminal, "host": u.host} for u in psutil.users()]
    cpu = {"count": psutil.cpu_count(logical=True), "percent": psutil.cpu_percent(interval=0.2)}
    vm = psutil.virtual_memory()
    mem = {"total": vm.total, "available": vm.available, "percent": vm.percent}
    disks = []
    for part in psutil.disk_partitions(all=False):
        try:
            usage = psutil.disk_usage(part.mountpoint)
            disks.append({"device": part.device, "mount": part.mountpoint, "total": usage.total, "percent": usage.percent})
        except Exception:
            pass
    net = {"if_addrs": {k:[s.address for s in v] for k,v in psutil.net_if_addrs().items()},
           "if_stats": {k:{"isup":v.isup, "speed":v.speed} for k,v in psutil.net_if_stats().items()}}
    procs = []
    for p in psutil.process_iter(attrs=["pid","name","username","cpu_percent"]):
        if len(procs) >= 50: break
        procs.append(p.info)

    db.insert_snapshot(
        os_name=info["os_name"],
        os_version=info["os_version"],
        hostname=info["hostname"],
        users_json=json.dumps(users),
        cpu_json=json.dumps(cpu),
        mem_json=json.dumps(mem),
        disks_json=json.dumps(disks),
        net_json=json.dumps(net),
        procs_sample_json=json.dumps(procs)
    )
    return {"ok": True, "snapshot": {"os": info, "cpu": cpu, "mem": mem, "disks": disks, "net": net, "procs_sample": procs}}
