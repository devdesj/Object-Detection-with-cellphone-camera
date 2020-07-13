import cv2
from cameras import Camera, Cellphone

motorola_one = Cellphone('moto_one', 'http://192.168.0.116:8080/shot.jpg')
samsung_edge = Cellphone('samsung_edge', 'http://192.168.0.2:8080/shot.jpg')
webcam = Camera('webcam')

print(Camera.count())
print("\n"
      "+-------------------------------------+\n"
      "|  Que dispositivo desea usar?        |\n"
      "+-------------------------------------+\n"
      "|   --> 1-Laptop's webcam (default)   |\n"
      "|   --> 2-Motorola_one                |\n"
      "|   --> 3-Samsung Edge                |\n"
      "|   --> 4-Otro                        |\n"
      "+-------------------------------------+\n")

device = input("Escriba aquí: ")
if device == "4":
    name = input("Enter the name of the Cellphone:")
    url = input("Paste the url of IP Webcam")
    new_phone = Cellphone(name, url)
    new_phone.get_display()
elif device == "3":
    samsung_edge.get_display()
elif device == "2":
    motorola_one.get_display()
elif device == "1":
    video = cv2.VideoCapture(0)
    webcam.get_display(video)
else:
    print(f"Since you did not write any of the given options, the default option will be used")
    video = cv2.VideoCapture(0)
    webcam.get_display(video)

cv2.destroyAllWindows()
