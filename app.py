from flask import Flask, render_template, Response, request, render_template_string


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/download_audio')
def download_audio():
    return render_template('download_audio.html')


if __name__ == '__main__':
    app.run(debug=True)
