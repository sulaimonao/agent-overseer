from . import fs_read, sys_info, logs_query, plan_exec

TOOLS = {
    "fs_read.read_text": fs_read.read_text,
    "sys_info.snapshot": sys_info.snapshot,
    "logs_query.search": logs_query.search,
    "plan_exec.plan":   plan_exec.plan,
    "plan_exec.execute": plan_exec.execute,
}
