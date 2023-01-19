from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishtofrench")
def englishtofrench():
    textToTranslate = request.args.get('textToTranslate')
    # print("English to French" + textToTranslate)
    frenchText=translator.englishtofrench(textToTranslate)
    return "Translated text to French: " + frenchText

@app.route("/frenchtoenglish")
def frenchtoenglish():
    textToTranslate = request.args.get('textToTranslate')
	# print("French to English" + textToTranslate)
    englishToFrench = translator.frenchtoenglish(textToTranslate)
    return "Translated text to English: " + englishToFrench

@app.route("/")
def renderIndexPage():
    # Write the code to render template
	return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
