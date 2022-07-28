import cv2
import pytesseract
import math

net = cv2.dnn.readNet("C:\\Users\\Rajni\\Desktop\\Python\\imagetotxt\\frozen_east_text_detection.pb")

def formatting(image):
    size=image.shape
    if size[2]==4:
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
    longest=max(size[0:2])
    temp=longest/32.0
    if(temp>=32):
        base=1024
    elif(temp<32):
        base=32*temp
    ratio=base/longest
    w=round(size[1]*ratio)
    w=w-w%32
    h=round(size[0]*ratio)
    h=h-h%32
    result = cv2.resize(image,(w,h),interpolation = cv2.INTER_AREA)
    return result,(w,h)

def decode(scores, geometry, score_thresh):
    detections = []
    confidences = []

    # Checking geometry AND scores
    assert len(scores.shape) == 4, "Incorrect dimensions of scores"
    assert len(geometry.shape) == 4, "Incorrect dimensions of geometry"
    assert scores.shape[0] == 1, "Invalid dimensions of scores"
    assert geometry.shape[0] == 1, "Invalid dimensions of geometry"
    assert scores.shape[1] == 1, "Invalid dimensions of scores"
    assert geometry.shape[1] == 5, "Invalid dimensions of geometry"
    assert scores.shape[2] == geometry.shape[2], "Invalid dimensions of scores and geometry"
    assert scores.shape[3] == geometry.shape[3], "Invalid dimensions of scores and geometry"
    height = scores.shape[2]
    width = scores.shape[3]
    
    for y in range(0, height):

        # Extract data from scores
        scores_data = scores[0][0][y]
        x0_data = geometry[0][0][y]
        x1_data = geometry[0][1][y]
        x2_data = geometry[0][2][y]
        x3_data = geometry[0][3][y]
        angles_data = geometry[0][4][y]
        for x in range(0, width):
            score = scores_data[x]

            # If score is lower than threshold score, move to next x
            if(score < score_thresh):
                continue

            # Calculate offset
            offsetX = x * 4.0
            offsetY = y * 4.0
            angle = angles_data[x]

            # Calculate cos and sin of angle
            cosA = math.cos(angle)
            sinA = math.sin(angle)
            h = x0_data[x] + x2_data[x]
            w = x1_data[x] + x3_data[x]

            # Calculate offset
            offset = ([offsetX + cosA * x1_data[x] + sinA * x2_data[x], offsetY - sinA * x1_data[x] + cosA * x2_data[x]])

            # Find points for rectangle
            p1 = (-sinA * h + offset[0], -cosA * h + offset[1])
            p3 = (-cosA * w + offset[0],  sinA * w + offset[1])
            center = (0.5*(p1[0]+p3[0]), 0.5*(p1[1]+p3[1]))
            detections.append((center, (w,h), -1*angle * 180.0 / math.pi))
            confidences.append(float(score))

    #Credits Satya Mallick
    return [detections, confidences]

def getSkewAngle(image) -> float:
        newImage = image.copy()
    # try:
        blur = cv2.GaussianBlur(newImage, (9, 9), 0)
        thrsh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 5))
        dilate = cv2.dilate(thrsh, kernel, iterations=3)

        contours, hierarchy = cv2.findContours(dilate, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key = cv2.contourArea, reverse = True)
        
        largestContour = contours[0]
        minAreaRect = cv2.minAreaRect(largestContour)
        angle = minAreaRect[-1]

        if(angle < -45):
            angle = 90 + angle
        return -1.0 * angle
    # except:
        # return 0

def rotateImage(cvImage, angle: float):
    newImage = cvImage.copy()
    (h, w) = newImage.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    # try:
    newImage = cv2.warpAffine(newImage, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    # except:
    newImage=newImage
    return newImage

def deskew(cvImage):
    angle = getSkewAngle(cvImage)
    return rotateImage(cvImage, -1.0 * angle)

def boundingbox(image,size):
    outputLayer = ["feature_fusion/Conv_7/Sigmoid","feature_fusion/concat_3"]
    imageBlob = cv2.dnn.blobFromImage(image, 1.0, size, (103.94, 116.78, 123.68), False, False)
    net.setInput(imageBlob)
    (scores, geometry) = net.forward(outputLayer)
    [boxes, confidences] = decode(scores, geometry, 0.5)
    indices = cv2.dnn.NMSBoxesRotated(boxes, confidences, 0.5, 0.3)
    result=[]
    print(boxes)
    for i in indices:
        # print(boxes[i[0]])
        vertices = cv2.boxPoints(boxes[i])
        topX=(round(min(vertices[0][0],vertices[1][0],vertices[2][0],vertices[3][0]))-4)
        topY=(round(min(vertices[0][1],vertices[1][1],vertices[2][1],vertices[3][1]))-2)
        lowX=(round(max(vertices[0][0],vertices[1][0],vertices[2][0],vertices[3][0]))+4)
        lowY=(round(max(vertices[0][1],vertices[1][1],vertices[2][1],vertices[3][1]))-2)
        result.append((topX,topY,lowX,lowY))
    return result

def textRecognition(image,boxes):
    image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    words=[]
    for p in boxes:
        roi=image[p[1]:p[3],p[0]:p[2]].copy()
        rotatedImage=deskew(roi)
        # try:
        word=pytesseract.image_to_string(rotatedImage)
        # except:
        #     continue
        # word=(p[1],p[3],p[0],p[2])
        words.append(word)
    return words
