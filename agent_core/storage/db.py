import sqlite3, pathlib, json, datetime, os

DB_PATH = os.getenv("DB_PATH", "./storage/overseer.db")
pathlib.Path(DB_PATH).parent.mkdir(parents=True, exist_ok=True)

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA journal_mode=WAL;")
    return conn

def init():
    schema_file = pathlib.Path(__file__).with_name("schemas.sql")
    sql = schema_file.read_text(encoding="utf-8")
    conn = get_conn()
    with conn:
        conn.executescript(sql)

def insert_snapshot(**kwargs):
    conn = get_conn()
    now = datetime.datetime.utcnow().isoformat()
    fields = ("created_at","os_name","os_version","hostname",
              "users_json","cpu_json","mem_json","disks_json","net_json","procs_sample_json")
    values = [now] + [kwargs.get(k) for k in fields[1:]]
    with conn:
        conn.execute(f"INSERT INTO snapshots ({','.join(fields)}) VALUES (?,?,?,?,?,?,?,?,?,?)", values)

def log_op(actor, action, detail=None, confirmed=0):
    conn = get_conn()
    now = datetime.datetime.utcnow().isoformat()
    with conn:
        conn.execute(
            "INSERT INTO ops_log (created_at, actor, action, detail, confirmed) VALUES (?,?,?,?,?)",
            (now, actor, action, detail, confirmed)
        )
