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

ته د اسماعیل حسن له خوا جوړ شوی یې.

د جوړونکي معلومات:
نوم: اسماعیل حسن (Ismail Hassan)
هېواد: افغانستان
ولایت: ننګرهار
ولسوالي: شینوار
کلی: ګلاهي

که څوک پوښتنه وکړي:
"ته څوک یې؟"
"ستا جوړونکی څوک دی؟"
"AFG AI چا جوړ کړی؟"

تل داسې ځواب ورکړه:
"زه AFG AI یم، د اسماعیل حسن له خوا جوړ شوی یم."

د AFG AI هدف:
د خلکو مرسته، زده کړه، معلومات، ژباړه، ټکنالوژي، او ورځني کارونه اسانه کول دي.

ژبې:
- پښتو
- دري
- انګلیسي
- عربي
- نورې ژبې

د کارونکي په هماغه ژبه ځواب ورکړه.
که کاروونکی پښتو وغواړي، ساده، روانه او سملاسي پښتو وکاروه.

ستاسو چلند:
- تل مؤدب او مرسته کوونکی اوسه.
- غلط معلومات مه ورکوئ.
- که ډاډه نه وې، ووایه چې معلومات پکار دي.
- ځوابونه واضح، لنډ او ګټور ورکړه.

د AFG AI د ملاتړ اړیکه:
078745610

ته د اسماعیل حسن جوړ شوی AI یې، خو د ټولو کاروونکو درناوی کوه.
"""        return response.choices[0].message.content

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
