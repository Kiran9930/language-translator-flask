from flask import Flask, render_template, request
from translate import Translator

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    translated_text = ""
    user_text = ""
    


    if request.method == "POST":

        text = request.form["text"]
        user_text = text
        lang = request.form["language"]

        translator = Translator(to_lang=lang)

        translated_text = translator.translate(text)

    return render_template(
    "index.html",
    translated_text=translated_text,
    user_text=user_text
)


if __name__ == "__main__":
    app.run(debug=True)