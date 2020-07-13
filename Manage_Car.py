import cv2
import numpy as np
import requests

face_classifier = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')


class Camera:
    instance_of_cameras = []

    def __init__(self, name):
        self.name = name
        Camera.instance_of_cameras.append(self)

    def __repr__(self):
        return f"Camera('{self.name}')"

    def __str__(self):
        return f"This is the '{self.name}'."

    @classmethod
    def count(cls):
        return len(cls.instance_of_cameras)

    @classmethod
    def list(cls):
        for i in cls.instance_of_cameras:
            print(i)

    def get_image(self, vid):
        check, normal_image = vid.read()
        return normal_image, cv2.cvtColor(normal_image, cv2.COLOR_BGR2GRAY)

    def check_for_object(self, frame, gray, output, classifier=face_classifier):
        # Classifier
        faces = classifier.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=20)

        # Iterate over the faces detected
        for (x, y, c, u) in faces:
            cv2.rectangle(frame, (x, y), (x + c, y + u), (0, 255, 255), 1)
            if output is True:
                width = gray.shape[0]
                if (width / 2 + 60 + c) < x:
                    print(f"{self.name}: Right")
                elif (width / 2 - 60) > x:
                    print(f"{self.name}: Left")

    # Output
    def show_img(self, frame):
        cv2.imshow(self.name, frame)
        pass

    def get_display(self, vid):
        print(repr(self))
        while True:
            frame, gray = self.get_image(vid)
            self.check_for_object(frame, gray, False)
            self.show_img(frame)
            if cv2.waitKey(1) == 32:
                break


class Cellphone(Camera):
    instances_of_cellphones = []

    def __init__(self, name, url):
        super().__init__(name)
        self.url = url
        Cellphone.instances_of_cellphones.append(self)

    def __repr__(self):
        return f"Cellphone('{self.name}', '{self.url}')"

    def __str__(self):
        return f"This is the '{self.name}' with URL '{self.url}'."

    def get_image(self):
        """
        Gets the image from the website
        and it returns it both as it is and in grayscale
        """
        img_requested = requests.get(self.url)
        img_arr = np.array(bytearray(img_requested.content), dtype=np.uint8)
        normal_image = cv2.imdecode(img_arr, -1)
        return normal_image, cv2.cvtColor(normal_image, cv2.COLOR_BGR2GRAY)

    def get_display(self, vid):
        print(repr(self))
        while True:
            frame, gray = self.get_image()
            self.check_for_object(frame, gray, False)
            self.show_img(frame)
            if cv2.waitKey(1) == 32:
                break


webcam = Camera('webcam')
motorola_one = Cellphone('moto_one', 'http://192.168.0.116:8080/shot.jpg')
samsung_edge = Cellphone('samsung_edge', 'http://192.168.0.2:8080/shot.jpg')

print(Camera.count())

objects = [print(obj) for obj in Camera.instance_of_cameras]

print("\n"
      "+-------------------------------------+\n"
      "|  Que dispositivo desea usar?        |\n"
      "+-------------------------------------+\n"
      "|   --> 0-Laptop's webcam (default)   |\n"
      "|   --> 1-Motorola_one                |\n"
      "|   --> 2-Samsung Edge                |\n"
      "|   --> 3-Otro                        |\n"
      "+-------------------------------------+\n")

device = int(input("Escriba aquí: "))

video = cv2.VideoCapture(0)
if device == len(Camera.instance_of_cameras):
    new_name = input("Nombre: ")
    new_url = input("URL: _")
    locals()[new_name] = Cellphone(new_name, new_url)
    Camera.list()
    print(locals()[new_name])
    cam = locals()[new_name]
else:
    try:
        cam = Camera.instance_of_cameras[device]
    except IndexError:
        cam = Camera.instance_of_cameras[0]

cam.get_display(video)

cv2.destroyAllWindows()
