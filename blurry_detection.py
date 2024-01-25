import cv2
import numpy as np
import glob
import shutil


def filtre():
	image_paths = glob.glob('/home/haktan/Desktop/mapping/orthomapping_test_photos/inputs_test_3/*.png')
	try:
		for i in image_paths:
			
			img = cv2.imread(i, cv2.IMREAD_GRAYSCALE)

			laplacian_var = cv2.Laplacian(img, cv2.CV_64F).var()

			if laplacian_var < 280:
				print("IMAGE IS BLURRY")
				#cv2.imshow("Img", img)
				shutil.move(i, "/home/haktan/Desktop/mapping/orthomapping_test_photos/blurry_ones")
				print("Blurry photo Moved Successfully...")
			if laplacian_var > 280:
				shutil.move(i,"/home/haktan/Desktop/mapping/orthomapping_test_photos/normal_photos_test_3")
				print("Others moved succesfully...")
			print(laplacian_var)

			#cv2.imshow("Img", img)
			#cv2.waitKey(0)
			cv2.destroyAllWindows()
	except:
		print("ERROR while elimination!!")


	"""# import the necessary packages
from imutils import paths
import cv2

def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image, cv2.CV_64F).var()

# Specify the input directory of images and the threshold
images_directory = "/path/to/your/images/directory"
threshold_value = 100.0

# loop over the input images
for imagePath in paths.list_images(images_directory):
	# load the image, convert it to grayscale, and compute the
	# focus measure of the image using the Variance of Laplacian
	# method
	image = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	fm = variance_of_laplacian(gray)
	text = "Not Blurry"
	# if the focus measure is less than the supplied threshold,
	# then the image should be considered "blurry"
	if fm < threshold_value:
		text = "Blurry"
	# show the image
	cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),
		cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
	cv2.imshow("Image", image)
	key = cv2.waitKey(0)
"""