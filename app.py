import os
from io import BytesIO
from flask import Flask, request

from cutouter import Cutouter
from docomo import ImageRecognition

ALLOWED_EXTENSIONS = set(["jpg", "jpeg", "png"])

app = Flask(__name__)

def allowed_file(filename):
    return "." in filename and \
        filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "No file part..."
    file = request.files["file"]

    if file.filename == "":
        return "No selected file..."
    if file and allowed_file(file.filename):
        image_bin = BytesIO(file.read())
        images = Cutouter(image_bin).main()
        ImageRecognition(images).main()
        return "Success!"


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
