import json
import os

FILE = "chat_history.json"

def save_chat(user, ai):
    data = []

    if os.path.exists(FILE):
        with open(FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

    data.append({
        "user": user,
        "ai": ai
    })

    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def get_history():
    if os.path.exists(FILE):
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    return []
