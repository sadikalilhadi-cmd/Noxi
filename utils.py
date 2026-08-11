import os
import json
import re
from datetime import datetime, timedelta

DATA_FILE = "moderation_data.json"


def load_data():
    if not os.path.exists(DATA_FILE):
        return {}

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}


data = load_data()


def save_data():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )


def get_user_data(user_id):
    user_id = str(user_id)

    if user_id not in data:
        data[user_id] = {
            "warns": [],
            "mutes": []
        }

    if "warns" not in data[user_id]:
        data[user_id]["warns"] = []

    if "mutes" not in data[user_id]:
        data[user_id]["mutes"] = []

    return data[user_id]


def current_date():
    return datetime.now().strftime("%d.%m.%Y %H:%M")


def parse_duration(duration):
    match = re.fullmatch(r"(\d+)(s|m|h|d)", duration.lower())

    if not match:
        return None

    amount = int(match.group(1))
    unit = match.group(2)

    if unit == "s":
        return timedelta(seconds=amount)

    if unit == "m":
        return timedelta(minutes=amount)

    if unit == "h":
        return timedelta(hours=amount)

    if unit == "d":
        return timedelta(days=amount)

    return None


def duration_text(delta):
    total = int(delta.total_seconds())

    if total < 60:
        return f"{total} saniye"

    if total < 3600:
        return f"{total // 60} dakika"

    if total < 86400:
        return f"{total // 3600} saat"

    return f"{total // 86400} gün"
