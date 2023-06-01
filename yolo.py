import cv2, pafy
from PIL import Image
import pytesseract
from gtts import gTTS
import numpy as np

url = 'https://www.youtube.com/watch?v=FhG0tK7hQNU' #유튜브 영상 주소
video = pafy.new(url) #유튜브 받아오기

best  = video.getbest()
best.resolution, best.extension
capture = cv2.VideoCapture(best.url) 

  # yolo 이미지 처리 불러오기
net = cv2.dnn.readNet("C:\Mb_lwj\PythonOpencv\yolo_object_detection/yolov3.weights", "C:\Mb_lwj\PythonOpencv\yolo_object_detection/yolov3.cfg")
classes = []
with open("C:\Mb_lwj\PythonOpencv\yolo_object_detection\coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))


#영상 저장하기 위한 설정
w = round(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = capture.get(cv2.CAP_PROP_FPS)
codec = cv2.VideoWriter_fourcc(*'XVID')
delay = round(1000/fps)
out = cv2.VideoWriter('C:\Mb_lwj\youtube.avi', codec, fps, (w, h))

while(True):
    
    '''
    # Loading image
    img = cv2.imread("C:\Mb_lwj\lena.jpg")
    img = cv2.resize(img, None, fx=0.4, fy=0.4)
    height, width, channels = img.shape
    '''    
    check, frame = capture.read()
    height, width, channels = frame.shape
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,70,200)
   
   
    cv2.imshow('edges',edges)
    cv2.imshow('gray',gray)
    
   
    # 물체 찾기
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

    net.setInput(blob)
    outs = net.forward(output_layers)

    # 찾은 물체를 박스 처리 해서 이미지 표현
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                # 물체를 찾았을 때
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # 박스 처리하기 위한 크기
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    print(indexes)
    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[class_ids[i]]
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, label, (x, y + 30), font, 2, color, 2)

  
    out.write(frame)
    cv2.imshow('frame',frame)
    
    
    key = cv2.waitKey(delay)
    if key == 27: # Esc
        break

#cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()