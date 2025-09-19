CREATE TABLE IF NOT EXISTS snapshots (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created_at TEXT NOT NULL,
  os_name TEXT,
  os_version TEXT,
  hostname TEXT,
  users_json TEXT,
  cpu_json TEXT,
  mem_json TEXT,
  disks_json TEXT,
  net_json TEXT,
  procs_sample_json TEXT
);

CREATE TABLE IF NOT EXISTS ops_log (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created_at TEXT NOT NULL,
  actor TEXT NOT NULL,  -- 'agent' or 'user'
  action TEXT NOT NULL,
  detail TEXT,
  confirmed INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS settings (
  key TEXT PRIMARY KEY,
  value TEXT
);
