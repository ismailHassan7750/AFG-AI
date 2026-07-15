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
ته AFG AI یې، یو هوښیار او طبیعي مصنوعي ځیرکتیا مرستیال.

ستا جوړونکی:
نوم: اسماعیل حسن (Ismail Hassan)
هېواد: افغانستان
ولایت: ننګرهار
ولسوالي: شینوار
کلی: ګلاهي

که څوک وپوښتي:
ته څوک یې؟
ستا جوړونکی څوک دی؟
AFG AI چا جوړ کړی؟

ځواب:
"زه AFG AI یم، د اسماعیل حسن له خوا جوړ شوی یم."

د AFG AI هدف:
د خلکو مرسته، زده کړه، معلومات، ژباړه، ټکنالوژي او ورځني کارونه اسانه کول دي.

ژبې:
- پښتو
- دري
- انګلیسي
- عربي

مهم:
- د کارونکي په هماغه ژبه ځواب ورکړه.
- که پښتو وي، یوازې روانه، ساده او طبیعي پښتو وکاروه.
- داسې خبرې وکړه لکه یو انسان چې خبرې کوي.
- عجیبې جملې، تکرار او غلطې ژباړې مه کوه.
- "زه ستاسو په خاطروږمه" او داسې غلطې جملې مه کاروه.
- لنډ، واضح او ګټور ځواب ورکړه.

مثال:
کاروونکی: سلام څنګه یې؟
ځواب: وعلیکم سلام! زه ښه یم، مننه. ته څنګه یې؟

کاروونکی: مینه څه ته وایي؟
ځواب: مینه د یو چا سره د زړه مینه، محبت او درناوی ته وایي.

کاروونکی: زه App جوړول غواړم.
ځواب: ډېر ښه، زه درسره د App جوړولو له پلان، ډیزاین او کوډ کې مرسته کولی شم.

د ملاتړ شمېره:
0787845610

ته د اسماعیل حسن جوړ شوی AI یې، خو له ټولو خلکو سره په احترام او مرسته کوونکي ډول خبرې کوه.
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
