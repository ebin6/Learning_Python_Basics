import cv2 as cv
img = cv.imread("bmw-m4-chromebook-wallpaper.jpg")

cv.imshow("Display window", img)

k = cv.waitKey(7000) # Wait for a keystroke in the window
print(dir(cv))

