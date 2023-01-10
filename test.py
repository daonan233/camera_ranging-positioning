import cv2


def CalculateFocalLength(image, distance, width):
    image_t = image.copy()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    image = cv2.GaussianBlur(image, (3, 3), 1)
    image = cv2.erode(image, kernel, iterations=2)
    image = cv2.dilate(image, kernel, iterations=2)
    ret, thresh = cv2.threshold(image, 175, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        print(f"w={w},h={h}")
        cv2.rectangle(image_t, (x, y), (x + w, y + h), (255, 255, 0), 2)
        print(h * distance / width)
        return image_t
    else:
        return None


video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    if frame is None:
        break
    img = CalculateFocalLength(frame, distance=0.723, width=0.295)
    if img is None:
        break
    cv2.imshow('result', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

video.release()
cv2.destroyAllWindows()
