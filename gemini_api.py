
import os
from dotenv import load_dotenv

load_dotenv()from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# خپل مالک Key دلته بدل کړه
OWNER_KEY = "."


AI_INFO = """
ته AFG AI یې.

ستا جوړوونکی Ismail Hasan دی.

که څوک پوښتنه وکړي:
تا چا جوړ کړی؟
ځواب ورکړه:
زه AFG AI یم، د Ismail Hasan لخوا جوړ شوی یم.

د AFG AI معلومات:
نوم: AFG AI
جوړونکی: Ismail Hasan

د جوړوونکي معلومات:
افغانستان، ننګرهار ولایت، شینوارو ولسوالۍ، ګلاهي کلی.

اصول:
- د کارونکي په ژبه ځواب ورکړه.
- پښتو، دري، انګلیسي او نورې ژبې وپېژنه.
- واضح او ګټور ځواب ورکړه.
"""


# خپل Gemini API Key دلته واچوه
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

URL = (
    "https://generativelanguage.googleapis.com/"
    "v1beta/models/gemini-2.0-flash:generateContent?key="
    + GEMINI_KEY
)


@app.route("/chat", methods=["POST"])
def chat():

    data = request.json

    message = data.get("message", "")
    owner_key = data.get("owner_key", "")


    if owner_key == OWNER_KEY:
        owner_status = """
دا د AFG AI جوړوونکی Ismail Hasan دی.
د هغه پیغام ته د جوړوونکي په توګه درناوی وکړه.
"""
    else:
        owner_status = """
دا عادي کارونکی دی.
په عادي ډول مرسته ورسره وکړه.
"""


    prompt = (
        AI_INFO
        + "\n"
        + owner_status
        + "\n\nد کارونکي پیغام:\n"
        + message
    )


    try:

        response = requests.post(
            URL,
            json={
                "contents":[
                    {
                        "parts":[
                            {
                                "text": prompt
                            }
                        ]
                    }
                ]
            },
            timeout=30
        )


        result = response.json()


        answer = (
            result["candidates"][0]
            ["content"]
            ["parts"][0]
            ["text"]
        )


    except Exception as e:

        answer = "خطا: " + str(e)


    return jsonify({
        "reply": answer
    })


app.run(
    host="0.0.0.0",
    port=5000
)
