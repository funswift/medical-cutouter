from io import BytesIO
import requests

class ImageRecognition:
    def __init__(self, images):
        self.images = images


    def main(self):
        for image in self.images:
            jpg_img = BytesIO()
            image.save(jpg_img, format="JPEG")
            url = "https://api.apigw.smt.docomo.ne.jp/imageRecognition/v1/concept/classify/"
            files = {
                "modelName": "food",
                "image": jpg_img,
            }
            r = requests.post(url, files=files)
            print(r.text)
