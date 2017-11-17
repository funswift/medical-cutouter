from PIL import Image
import cv2, matplotlib
import numpy as np
import matplotlib.pyplot as plt

class Cutouter:
    def __init__(self, image_bin):
        self.image = Image.open(image_bin)


    def get_contours(self):
        img = np.asarray(self.image)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
        #ガウスブラーでボカす
        img_pre = cv2.GaussianBlur(img_gray, (5, 5), 0)
        #閾値を指定して二値化
        _, img_bin = cv2.threshold(img_pre, 150, 255, cv2.THRESH_BINARY) 
        #反転
        img_bin = cv2.bitwise_not(img_bin)
        #輪郭を抽出
        im2, contours, hierarchy = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        min_img_area = 60
        large_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_img_area]
        return large_contours

 
    def crop_image(self, large_contours):
        images = []
        for contour in large_contours:
            x, y, w, h = cv2.boundingRect(contour)
            crop_area = (x, y, x+w, y+h)
            crop_image = self.image.crop(crop_area)
            images.append(crop_image)
        return images


    def main(self):
        contours = self.get_contours()
        self.crop_image(contours)
