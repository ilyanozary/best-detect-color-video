import cv2 as cv
import numpy as np

webcam = cv.VideoCapture(0)

while True:
    # Read frame from webcam 
    ret, frame = webcam.read()
    
# Convert frame from BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

# Define blue color range in HSV
    lower_blue = np.array([100,50,50]) 
    upper_blue = np.array([116,255,255])
    
# Create a blue color mask
    blue_mask = cv.inRange(hsv, lower_blue, upper_blue)
   
# Apply blue mask to frame    
    blue_frame = cv.bitwise_and(frame, frame, mask=blue_mask)

# Display original frame    
    cv.imshow("original", frame)  

# Display blue masked frame    
    cv.imshow("blue detected", blue_frame)

# Display blue color mask
    cv.imshow("mask", blue_mask)
        
# Close windows when 'q' pressed  
    if cv.waitKey(5) & 0xFF == ord('q'):
        break
webcam.release()
cv.destroyAllWindows()