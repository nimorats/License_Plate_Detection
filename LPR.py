import cv2
import imutils
import numpy as np

def lpr(img, output_file_name):
    #img = imutils.resize(img, width=500)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #ret,thresh1 = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)

    ###smoothing
    blur = cv2.bilateralFilter(gray,5,75,75)

    ###finding edges
    edges = cv2.Canny(blur,100,200)

    ###contours
    (_, contours, _) = cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key = cv2.contourArea, reverse = True)[:30]
    NumberPlateCnt = None
    result = ""

    #checking for rectangle shapes
    for cont in contours:
        peri = cv2.arcLength(cont,True)
        approx = cv2.approxPolyDP(cont, 0.01 * peri, True)
        if len(approx) == 4:
            #print(approx)
            #NumberPlateCnt = approx
            ###drawing contours on images
            cv2.drawContours(img, [approx], -1, (0,255,0), 3)
            cv2.imwrite("output/"+output_file_name, img)

            ###cropping contours
            [x,y,w,h] = cv2.boundingRect(approx)
            cv2.rectangle(img,(x,y),(x+w,y+h), (255,255,0), 1)
            roi = img[y:y+h, x:x+w]
            cv2.imwrite("ocr/"+output_file_name, roi)
            
            result = "Done. Check output in location: media/output/"
            cv2.destroyAllWindows()
            break
        """       
        elif len(approx) != 4:
            NumberPlateCnt = "none"
            
    if NumberPlateCnt != "none": 
        #drawing only rectangle shape contours
        cv2.drawContours(img, [NumberPlateCnt], -1, (0,255,0), 3)
        cv2.imwrite("output/"+output_file_name, img)
        result = "Done. Check output in location: media/output/"
        cv2.destroyAllWindows()
    else:
        result = "No plate detected"
        cv2.destroyAllWindows()"""

    return result

