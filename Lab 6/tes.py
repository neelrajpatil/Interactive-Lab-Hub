import cv2

# Load the image
image = cv2.imread("/home/pi/Documents/idd/Interactive-Lab-Hub/Lab 6/lockdown.png")

# Get the screen size




# Resize the image to fit the screen
resized_image = cv2.resize(image, (1920,1080))

# Display the image in fullscreen
cv2.imshow("Image", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
