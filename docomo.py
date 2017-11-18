import os
from io import BytesIO
import requests

APIKEY = os.environ.get("DOCOMO_APIKEY")

class ImageRecognition:
    def __init__(self, images):
        self.images = images


    def main(self):
        for image in self.images:
            jpg_img = BytesIO()
            image.save(jpg_img, format="PNG")
            url = "https://api.apigw.smt.docomo.ne.jp/imageRecognition/v1/concept/classify/?APIKEY={0}".format(APIKEY)
            data = {
                "modelName": "food",
            }
            files = {
                "image": jpg_img.getvalue(),
            }
            r = requests.post(url, data=data, files=files)
            print(r.text)
