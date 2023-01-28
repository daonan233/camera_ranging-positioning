import cv2
import cvzone
import mediapipe
from cvzone.FaceMeshModule import FaceMeshDetector
#导入摄像头
cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces = 1)
while True:
    success,img = cap.read()
    img,faces = detector.findFaceMesh(img,draw = False)    #做检测器，查找面部网格，返回图像（img）和我们的面部（faces）  ,draw = False有了这句话后就看不到网格了
    if faces:
        face = faces[0]
        pointLeft = face[145]     #左眼
        pointRight = face[374]    #右眼

        w, _ = detector.findDistance(pointLeft, pointRight)  # 将左眼点的位置到右眼点位置的距离赋值给w        w后面的下划线是忽略其他的值
        W = 6.3  # 人眼的左眼与右眼之间的距离为63mm
        #f = (w * d) / W
        f = 550
        d = (W * f) / w
        print(d)
    cvzone.putTextRect(img,f'distance:{int(d)}cm',(face[10][0]-95,face[10][1]-5),scale = 2)

    cv2.imshow("Iamge",img)
    cv2.waitKey(1)