import os
import json

MEMORY_DIR = "memories"

os.makedirs(MEMORY_DIR, exist_ok=True)


def chat_file(owner_key):
    if not owner_key:
        owner_key = "guest"

    return os.path.join(MEMORY_DIR, f"{owner_key}_chat.json")

def load_chat(owner_key):
    file = chat_file(owner_key)

    if not os.path.exists(file):
        return []

    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)

            if isinstance(data, list):
                return data

            if isinstance(data, dict) and "memories" in data:
                return data["memories"]

            return []

    except:
        return []


def save_chat(owner_key, user, ai):
    history = load_chat(owner_key)

    history.append({
        "user": str(user),
        "ai": str(ai)
    })

    if len(history) > 200:
        history = history[-200:]

    with open(chat_file(owner_key), "w", encoding="utf-8") as f:
        json.dump({"memories": history}, f, ensure_ascii=False, indent=2)

def build_messages(system_prompt, history, message):
    messages = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]

    for item in history[-30:]:
        if isinstance(item, dict):
            messages.append({
                "role": "user",
                "content": item.get("user", "")
            })

            messages.append({
                "role": "assistant",
                "content": item.get("ai", "")
            })

    messages.append({
        "role": "user",
        "content": message
    })

    return messages
