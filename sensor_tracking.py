"""
This script processes a thresholded video of a maple seed-inspired sensor to:
- Track its autorotation using the CamShift algorithm
- Estimate average rotational velocity (in degrees/s and revolutions/s)
- Calculate tip velocity (m/s) based on the design radius

"""

import cv2
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Ask user for video file
Tk().withdraw()  # Hide root Tk window
VIDEO_PATH = askopenfilename(
    title="Select thresholded rotation video",
    filetypes=[("MP4 files", "*.mp4"), ("All files", "*.*")]
)

if not VIDEO_PATH:
    raise ValueError("No video file selected.")

# Configuration
START_FRAME = 180
END_FRAME = 280
RADIUS_M = 0.023  # Radius of the sensor (23 mm)

# Load video
cap = cv2.VideoCapture(VIDEO_PATH)
if not cap.isOpened():
    raise IOError("Error: Could not open video.")

cap.set(cv2.CAP_PROP_POS_FRAMES, START_FRAME)
ret, frame = cap.read()
if not ret:
    raise ValueError("Error: Could not read starting frame.")

# ROI Selection
roi = cv2.selectROI("Select ROI", frame, False)
cv2.destroyWindow("Select ROI")

# Expand ROI by 20%
dw, dh = int(roi[2] * 0.2), int(roi[3] * 0.2)
track_window = (
    max(0, roi[0] - dw // 2),
    max(0, roi[1] - dh // 2),
    roi[2] + dw,
    roi[3] + dh
)

# Initialise variables
roi_hist = None
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 5, 1)
fps = cap.get(cv2.CAP_PROP_FPS)
delta_t = 1.0 / fps
duration = (END_FRAME - START_FRAME) * delta_t
total_delta_theta = 0
prev_angle = None
frame_idx = START_FRAME

# Tracking loop
while cap.isOpened() and frame_idx <= END_FRAME:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (0., 60., 32.), (180., 255., 255.))

    if roi_hist is None:
        roi_hist = cv2.calcHist([hsv], [0], mask, [32], [0, 180])
        cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
    else:
        back_proj = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
        ret_camshift, track_window = cv2.CamShift(back_proj, track_window, term_crit)
        (center, (w, h), angle) = ret_camshift

        if prev_angle is not None:
            delta_theta = angle - prev_angle
            if delta_theta > 180:
                delta_theta -= 360
            elif delta_theta < -180:
                delta_theta += 360
            total_delta_theta += delta_theta

        prev_angle = angle

        box = cv2.boxPoints(ret_camshift)
        box = np.intp(box)
        tracked_frame = cv2.polylines(frame.copy(), [box], True, (0, 255, 0), 2)
        cv2.imshow("Tracking", tracked_frame)

    key = cv2.waitKey(int(1000 / fps)) & 0xFF
    if key == 27:  # ESC to exit
        break

    frame_idx += 1

# Results
cap.release()
cv2.destroyAllWindows()

rotation_rate_degrees = total_delta_theta / duration
rotation_rate_rps = rotation_rate_degrees / 360.0
tip_velocity_mps = rotation_rate_rps * 2 * np.pi * RADIUS_M

print("\n=== Autorotation Tracking Results ===")
print(f"Frames analysed: {START_FRAME}–{END_FRAME}")
print(f"Rotation rate: {rotation_rate_degrees:.2f} degrees/s")
print(f"             ≈ {rotation_rate_rps:.2f} revolutions/s")
print(f"Tip velocity: {tip_velocity_mps:.2f} m/s")
