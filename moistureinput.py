def Moisture(i,j):
    import cv2

    img = cv2.imread('moisturemap.png',1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    moisture = 0
    px = hsv[i,j]

    if(px[1]>=104):
        if(px[0]>=11 and px[0]<18):
            moisture = 0
        elif(px[0]>=18 and px[0]<31):
            moisture = 5
        elif(px[0]>=31 and px[0]<33):
            moisture = 10
        elif(px[0]>=33 and px[0]<40):
            moisture = 15
        elif(px[0]>=40 and px[0]<66):
            moisture = 20
        elif(px[0]>=66 and px[0]<87):
            moisture = 25
        elif(px[0]>=87 and px[0]<96):
            moisture = 30
        elif(px[0]>=96 and px[0]<107):
            moisture = 35
        elif(px[0]>=107 and px[0]<115):
            moisture = 40
        elif(px[0]>=115 and px[0]<120):
            moisture = 50
    
    return moisture