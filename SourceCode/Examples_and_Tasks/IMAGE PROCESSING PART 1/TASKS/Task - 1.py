import cv2

image = cv2.imread(r'C:\Users\Lenovo\Desktop\mypic.jpg' , 1)

gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)

cv2.imwrite(r'C:\Users\Lenovo\Desktop\mypicgray.jpg' , gray)
