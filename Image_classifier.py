import cv2

def__init__(self, width, height, inter=cv2.INTER_AREA):
    self.width=width
    self.height=height
    self.inter=inter

def preproces(self, image):
    return cv2.resize(image, (self.width, self.height), interpolation=self.inter)


