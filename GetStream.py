import numpy
import requests
import cv2

url = "http://192.168.0.3:8080/shot.jpg"

while True:
    img_requested = requests.get(url)
    img_arr = numpy.array(bytearray(img_requested.content), dtype=numpy.uint8)
    img = cv2.imdecode(img_arr, -1)
    cv2.imshow('Camera', img)
    if cv2.waitKey(1) == 32:
        break

cv2.destroyAllWindows()
