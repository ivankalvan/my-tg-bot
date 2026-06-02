import os
from pathlib import Path

env_path = Path(".") / ".env"


BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

BOT_NAME = ""
BOT_VERSION = "0.0.1"

ADMIN_ID = "5981112643"

DATABASE_NAME = ""

if not BOT_TOKEN:
    raise ValueError("NO BOT_TOKEN")
