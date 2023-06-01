import cv2


cap = cv2.VideoCapture('C:/Mb_lwj/vtest.avi')

cv2.setTrackbarPos('Threshold', 'dst', 128)
    
while cap.isOpened():
    
    
    run, frame = cap.read()
    if not run:
        print("[프레임 수신 불가] - 종료합니다")
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   
    img_binary = cv2.adaptiveThreshold(gray, 150, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 29, 20)
    '''
    def on_threshold(pos):
        _, dst = cv2.threshold(frame, 150, 255, cv2.THRESH_BINARY)
        cv2.imshow('dst', dst)
    
    cv2.namedWindow('dst')
    cv2.createTrackbar('Threshold', 'dst', 0, 255, on_threshold) # 임계값 범위 0~255
   '''
    
    cv2.imshow('video', gray)
    cv2.imshow('video2', img_binary)   
    
    cv2.imshow('main1', frame)
    
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
    '''
    
    
    if run:
        img = cv2.cvtColor(frame, cv2.IMREAD_COLOR)
        
        imgGray = img.convert('L')

        row= img.rows
        col= img.cols
        for y in range(0,row ):
            for x in range(0,col ):
                b = frame.item(y, x, 0)
                g = frame.item(y, x, 1)
                r = frame.item(y, x, 2)

        gray = (int(b) + int(g) + int(r)) / 3.0

        if gray > 255:
            gray = 255
           ''' 
   

cap.release()
cv2.destroyAllWindows()
 