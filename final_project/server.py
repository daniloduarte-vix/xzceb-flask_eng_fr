from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    english_text = request.form['text']
    french_text = translate_text(english_text, 'en', 'fr')
    return french_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    french_text = request.form['text']
    english_text = translate_text(french_text, 'fr', 'en')
    return english_text

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
