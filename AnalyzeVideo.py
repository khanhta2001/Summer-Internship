"""
This is a file for recording a video. It takes a recorded video and output analyzed video.
This file is on PC/Laptops.
"""

import numpy as np
import cv2

boundaries = [([17, 15, 100], [50, 56, 200]), ([86, 31, 4], [220, 88, 50]), ([25, 146, 190], [62, 174, 250])]
""" 
[17, 15, 100], [50, 56, 200] is the color code of a given color. Change it to anything else to analyze any given color
"""

filename = cv2.VideoCapture('video-1627602084.mp4')

while filename.isOpened():
    ret,frame = filename.read()
    for (lower_bound, upper_bound) in boundaries:
        bottom = np.array(lower_bound, dtype = "uint8")
        top = np.array(upper_bound, dtype = "uint8")
        mask = cv2.inRange(frame, bottom, top)
        output = cv2.bitwise_and(frame, frame, mask=mask)
        """
        can change "file" to any other name for a more meaning name instead of mine.
        """

        cv2.imshow("file", output)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            filename.release()
            cv2.destroyAllWindows()
            break
