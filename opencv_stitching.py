import cv2
import glob

def image_stitching():
    paths = glob.glob('/home/haktan/Desktop/mapping/orthomapping_test_photos/normal_photos_test_3/*.png')
    images = []
    try:
        for image in paths:
            img = cv2.imread(image) 
            images.append(img)
            #cv2.imshow("Image", img)
            #cv2.waitKey(0)


        image_Stitcher = cv2.Stitcher_create()

        status, stitched = image_Stitcher.stitch(images)
        #cv2.imwrite('lossless_compressed_image.png', stitched)
        #jpeg_quality = 90  # A value between 0 and 100 (higher means better quality, but larger file size)
        #cv2.imwrite('lossy_compressed_image.jpg', stitched, [cv2.IMWRITE_JPEG_QUALITY, jpeg_quality])

        if status == cv2.Stitcher_OK:
            cv2.imwrite("orthomapping_test_photos/outputs/stitchedOutput.png", stitched)
            #cv2.imshow("Stitched Image", stitched)
            #cv2.waitKey()
            print("Stitched Succesfully...")
    except:
        print("ERROR while stitching!!!")



"""
    stitched_img = cv2.copyMakeBorder(stitched, 10,10, 10, 10, cv2.BORDER_CONSTANT, (0,0,0))

    gray = cv2.
    cvtColor(stitched_img, cv2.COLOR_BGR2GRAY)
    thresh_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)[1]
    
    cv2.imshow("Threshold Image", thresh_img)
    cv2.waitKey(0)

    contours = cv2.findContours(thresh_img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    contours = imutils.grab_contours(contours)
    areaOI = max(contours, key=cv2.contourArea)

    mask = np.zeros(thresh_img.shape , dtype="uint8")
    x, y, w, h = cv2.boundingRect(areaOI)
    cv2.rectangle(mask, (x,y), (x+y , w+h), 255, -1)

    minRectangle = mask.copy()
    sub = mask.copy()

    while cv2.countNonZero(sub) > 0:
        minRectangle = cv2.erode(minRectangle,None)
        sub = cv2.subtract(minRectangle, thresh_img)


    contours = cv2.findContours(minRectangle.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    contours = imutils.grab_contours(contours)
    areaOI = max(contours, key = cv2.contourArea)

    cv2.imshow("Minrectangle Image", minRectangle)
    cv2.waitKey(0)

    x, y, w, h = cv2.boundingRect(areaOI)

    stitched_img = stitched_img[y:y + h, x:x +w]

    cv2.imwrite("StitchedOutputProcessed.png", stitched_img)

    cv2.imshow("Stitched Image Processed",stitched_img)
        
    cv2.waitKey(0)

else:
    print("Error during stitching. Status code:", status)  

"""
