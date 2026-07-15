from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def ai_response(message):
    text = message.lower()

    # د اسماعیل حسن ځانګړی پیغام (که پیغام د (. ) نښې سره پیل شي)
    if message.startswith("(.)"):
        clean_message = message[3:].strip()
        return f"ښه راغلاست اسماعیل حسن! 👋\nستاسو پیغام: {clean_message}"

    # سلام
    if "سلام" in text:
        return "وعلیکم سلام 👋 زه AFG AI یم، د اسماعیل حسن لخوا جوړ شوی یم. څنګه مرسته درسره وکړم؟"

    # نوم
    elif "نوم" in text:
        return "زه AFG AI یم، د اسماعیل حسن لخوا جوړ شوی یم."

    # د جوړونکي په اړه
    elif "اسماعیل حسن" in text or "ismail hassan" in text:
        return (
            "اسماعیل حسن یو خوش‌اخلاقه انسان دی.\n"
            "هغه د افغانستان د ننګرهار ولایت، د شینوارو ولسوالۍ، "
            "د ګلاهي کلي اوسېدونکی دی."
        )

    # د اړیکې معلومات
    elif "ستونزه" in text or "تماس" in text or "واتساپ" in text:
        return (
            "که کومه ستونزه لرئ، د واتساپ له لارې اړیکه ونیسئ:\n"
            "📱 0787845610"
        )

    # مننه
    elif "مننه" in text:
        return "ستاسو هم مننه ❤️"

    # نورې پوښتنې
    else:
        return (
            f"تاسو ولیکل: {message}\n\n"
            "زه AFG AI یم، د اسماعیل حسن لخوا جوړ شوی یم."
        )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    reply = ai_response(message)
    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
