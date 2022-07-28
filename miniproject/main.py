import cv2
import defined

image_path=('/home/mukesh/Project/Data/testImg05')
image=cv2.imread(image_path)
image,size=defined.formatting(image)
omage=image.copy()
boundingBox=defined.boundingbox(image,size)
text=defined.textRecognition(omage,boundingBox)
# print(text)
