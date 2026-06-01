from pathlib import Path

env_path = Path(".") / ".env"


BOT_TOKEN = "8644238592:AAEdvQqmMHfWdiPzfEW_jwJks366V_XrJKI"

BOT_NAME = ""
BOT_VERSION = "0.0.1"

ADMIN_ID = "5981112643"

DATABASE_NAME = ""

if not BOT_TOKEN:
    raise ValueError("NO BOT_TOKEN")