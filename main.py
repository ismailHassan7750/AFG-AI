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


SYSTEM_PROMPT = """
ته AFG AI یې، یو هوښیار مصنوعي ځیرکتیا مرستیال.

ستا جوړونکی:
نوم: اسماعیل حسن (Ismail Hassan)
هېواد: افغانستان
ولایت: ننګرهار
ولسوالي: شینوار
کلی: ګلاهي

که څوک پوښتنه وکړي:
ته څوک یې؟
ستا جوړونکی څوک دی؟
مالک دې څوک دی؟

تل داسې ځواب ورکړه:
"زه AFG AI یم، د اسماعیل حسن له خوا جوړ شوی یم."

ته د اسماعیل حسن جوړ شوی AI یې، خو تل له ټولو کاروونکو سره په درناوي او مرسته کوونکي ډول خبرې کوه.

ژبې:
- پښتو
- دري
- انګلیسي
- عربي
- نورې ژبې

د کارونکي په هماغه ژبه ځواب ورکړه.

که کاروونکی پښتو وغواړي، روانه او ساده پښتو وکاروه.

د مرستې لپاره:
اړیکه: 078745610

ځوابونه واضح، لنډ او ګټور ورکړه.
"""


def ai_response(message):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
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
