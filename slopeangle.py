import cv2
import moistureinput,SFalgorithm

img = cv2.imread('slope.png',1)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
colors = []

for i in range(519):
    for j in range(523):

        px = hsv[i,j]

        if(px[1]>=200):
            if(px[0]>=6 and px[0]<=30):

                if(px[2]<=202 and px[2]>=200):
                    slope = 0.06
                elif(px[2]<=199 and px[2]>=164):
                    slope = 0.07
                elif(px[2]<=165 and px[2]>=135):
                    slope = 0.08
                elif(px[2]<=134 and px[2]>=99):
                    slope = 0.09
                elif(px[2]<=98 and px[2]>=68):
                    slope = 0.1
                else:
                    slope = None
                
                    moisture = moistureinput.Moisture(i,j)

                if(slope==None):
                    Safety_Factor = None

                else:
                    Safety_Factor = SFalgorithm.Algorithm(moisture,slope)

                    img_out = cv2.imread('output.png',1)

                    if(Safety_Factor<=1 and Safety_Factor>0.7):
                        img_out[i,j:j+5][0] = 255
                        img_out[i,j:j+5][1] = 0
                        img_out[i,j][2] = 0

                    elif(Safety_Factor<=0.7):
                        img_out[i,j:j+5][0] = 0
                        img_out[i,j:j+5][1] = 0
                        img_out[i,j][2] = 255

                    cv2.imwrite('output.png',img_out)