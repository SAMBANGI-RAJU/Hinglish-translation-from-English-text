from flask import Flask, render_template, request
from translation_code import translate_sentence  # Import your translation function

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def translate():
    translated_result = ""
    if request.method == 'POST':
        english_sentence = request.form['english_sentence']
        translated_result = translate_sentence(english_sentence)
    return render_template('index.html', translated_result=translated_result)

if __name__ == '__main__':
    app.run(debug=True)
