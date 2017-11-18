import os
from io import BytesIO
from flask import Flask, request, jsonify

from cutouter import Cutouter
from docomo import ImageRecognition

KEY = os.environ.get("CUTOUTER_KEY")
ALLOWED_EXTENSIONS = set(["jpg", "jpeg", "png"])

app = Flask(__name__)

def valid_key(key):
    return key == KEY

def allowed_file(filename):
    return "." in filename and \
        filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/", methods=["POST"])
def upload_file():
    if not valid_key(request.form["key"]):
        return "Invalid key..."
    if "file" not in request.files:
        return "No file part..."
    file = request.files["file"]

    if file.filename == "":
        return "No selected file..."
    if file and allowed_file(file.filename):
        image_bin = BytesIO(file.read())
        images = Cutouter(image_bin).main()
        res =  ImageRecognition(images).main()
        return jsonify(res)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
