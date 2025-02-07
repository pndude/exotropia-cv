"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

from time import sleep
import cv2
import datetime
from gaze_tracking import GazeTracking
from EyeTracker import EyeTracker
 
gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
eyeTracker = EyeTracker()

while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    eyeTracker.analyzeDrift(gaze)
    text = ""

    drift_boolean_status = eyeTracker.drifting_boolean_status
    cv2.putText(frame, "Drift Status :" + str(drift_boolean_status) , (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
    cv2.putText(frame, "Left pupil ratio:  " + eyeTracker.horizontal_left_ratio_status, (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil ratio: " + eyeTracker.horizontal_right_ratio_status, (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    cv2.imshow("Eye Tracker Status", frame)
    
    if cv2.waitKey(1) == 27:
        break
   
webcam.release()
cv2.destroyAllWindows()
eyeTracker.closeResources()

