"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

from time import sleep
import cv2
import datetime
from gaze_tracking import GazeTracking

class EyeTracker:
    
    def __init__(self):
        self.horizontal_left_ratio = None
        self.horizontal_right_ratio = None
        self.difference_in_horizontal_ratio = None
        self.horizontal_right_ratio_status = "Undetermined"
        self.horizontal_left_ratio_status = "Undetermined"
        self.difference_in_horizontal_ratio_value = "Undetermined"
        self.drifting_boolean_status = False
        self.dataFile = None
        self.dataFile = open("data.csv", "w")

    def analyzeDrift(self, gaze):
        self.horizontal_left_ratio = gaze.horizontal_pupil_left_ratio() 
        self.horizontal_right_ratio = gaze.horizontal_pupil_right_ratio()
        if self.horizontal_left_ratio is not None and self.horizontal_right_ratio is not None:
            self.difference_in_horizontal_ratio = self.horizontal_left_ratio - self.horizontal_right_ratio
        self.drifting_boolean_status = False
        if self.difference_in_horizontal_ratio is not None:
            if abs(self.difference_in_horizontal_ratio) > 0.15:
                self.drifting_boolean_status = True
        if self.horizontal_right_ratio is not None:
            self.horizontal_right_ratio_status = "{:.2f}".format(self.horizontal_right_ratio)
        if self.horizontal_left_ratio is not None:
            self.horizontal_left_ratio_status = "{:.2f}".format(self.horizontal_left_ratio)
        if self.difference_in_horizontal_ratio is not None:
            self.difference_in_horizontal_ratio_value = "{:.2f}".format(self.difference_in_horizontal_ratio)
        data_to_write = "Current Time, " + datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + ", Drifting, " + str(self.drifting_boolean_status) + ", Left ratio," + self.horizontal_left_ratio_status + ", Right ratio," + self.horizontal_right_ratio_status + ", Difference in ratio," + self.difference_in_horizontal_ratio_value + "\n"
        print(data_to_write)
        self.dataFile.write(data_to_write)
        self.dataFile.flush
        return 0

    def closeResources(self):
        self.dataFile.close()
        return 0

