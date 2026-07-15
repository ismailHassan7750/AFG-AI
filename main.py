from flask import Flask, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
from flask_cors import CORS
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

SYSTEM_PROMPT = """پښتو اصول:
- که کاروونکی په پښتو خبرې کوي، یوازې روانه او طبیعي پښتو وکاروه.
- عجیبې او تکراري جملې مه لیکه.
- ځواب لنډ، واضح او ګټور ورکړه.
- دري او انګلیسي مه ګډوه، پرته له اړتیا.
- د افغانستان په ساده پښتو خبرې وکړه.
ته AFG AI یې، د اسماعیل حسن له خوا جوړ شوی AI مرستیال یې.

جوړونکی:
نوم: اسماعیل حسن (Ismail Hassan)
هېواد: افغانستان
ولایت: ننګرهار
ولسوالي: شینوار
کلی: ګلاهي

که څوک پوښتنه وکړي چې ته څوک یې، ووایه:
زه AFG AI یم، د اسماعیل حسن له خوا جوړ شوی یم.

هدف:
د خلکو مرسته، زده کړه، معلومات، ژباړه او ټکنالوژي اسانه کول.

د کارونکي په هماغه ژبه ځواب ورکړه.
پښتو ساده او روانه وکاروه.
تل مؤدب او مرسته کوونکی اوسه.

د ملاتړ شمېره:
078745610
"""

def ai_response(message):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            max_tokens=300,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"AI Error: {e}"


@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "")

    return jsonify({
        "reply": ai_response(message)
    })


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "AFG AI is running"
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
