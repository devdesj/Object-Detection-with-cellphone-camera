import cv2
# For raspberry pi usb connection to an arduino
# import serial
# port = serial.Serial('/dev/ttyACM0', 9600)

classifier = cv2.CascadeClassifier('data/cascade4.xml')
classifier2 = cv2.CascadeClassifier('data/haarcascade_profileface.xml')
classifier4 = cv2.CascadeClassifier('data/haarcascade_frontalface_alt.xml')
classifier5 = cv2.CascadeClassifier('data/haarcascade_frontalface_alt2.xml')
classifier6 = cv2.CascadeClassifier('data/haarcascade_frontalface_alt_tree.xml')

url = "http://192.168.0.3:8080/shot.jpg"

frame = cv2.VideoCapture(0)

while True:

    # img_requested = requests.get(url)
    # img_arr = np.array(bytearray(img_requested.content), dtype=np.uint8)
    # frame = cv2.imdecode(img_arr, -1)

    check, video = frame.read()

    gray = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)

    faces = classifier.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=20)

    for (x, y, c, u) in faces:
        print(x)
        print(y)
        print(c)
        print(u)
        zone1 = gray[x:x + c, y:y + u]
        cv2.rectangle(video, (x, y), (x + c, y + u), (0, 255, 255), 1)

    # port.write(b'b')

    cv2.imshow('IP Webcam', video)
    if cv2.waitKey(30) == 32:
        break

frame.release()
cv2.destroyAllWindows()



