import os
import json

MEMORY_DIR = "memories"
LONG_MEMORY_FILE = "long_memory.json"

os.makedirs(MEMORY_DIR, exist_ok=True)


def chat_file(owner_key):
    if not owner_key:
        owner_key = "guest"

    return os.path.join(
        MEMORY_DIR,
        f"{owner_key}_chat.json"
    )


def load_chat(owner_key):
    file = chat_file(owner_key)

    if not os.path.exists(file):
        return []

    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)

        if isinstance(data, dict):
            return data.get("memories", [])

        if isinstance(data, list):
            return data

    except Exception as e:
        print("LOAD MEMORY ERROR:", e)

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
        json.dump(
            {
                "memories": history
            },
            f,
            ensure_ascii=False,
            indent=2
        )


def load_long_memory():

    if not os.path.exists(LONG_MEMORY_FILE):
        return {}

    try:
        with open(
            LONG_MEMORY_FILE,
            "r",
            encoding="utf-8"
        ) as f:
            return json.load(f)

    except:
        return {}


def save_long_memory(data):

    with open(
        LONG_MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=2
        )


def build_messages(system_prompt, history, message):

    messages = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]


    for item in history[-20:]:

        if not isinstance(item, dict):
            continue

        user_text = item.get(
            "user",
            ""
        )

        ai_text = item.get(
            "ai",
            ""
        )


        if user_text:

            messages.append(
                {
                    "role": "user",
                    "content": user_text
                }
            )


        if ai_text:

            messages.append(
                {
                    "role": "assistant",
                    "content": ai_text
                }
            )


    messages.append(
        {
            "role": "user",
            "content": message
        }
    )


    return messages
