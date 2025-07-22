# 🍁 Biodegradable maple seed inspired sensors for environmental monitoring

This project explores the design, fabrication, and analysis of biodegradable, electronics-free sensors, inspired by the aerodynamic properties of maple seeds. These sensors are intended for distributed, low-cost environmental monitoring (e.g. pH detection) and are capable of passive wind dispersal.


# Features

- Bio-inspired design for efficient wind dispersal
- Electronics-free and biodegradable 
- Visual pH sensing at point of contact
- Image processing for autorotation and dispersal analysis


# Project Overview

Modern environmental monitoring systems often rely on electronics that contribute to e-waste. This project explores a sustainable alternative by using biodegradable materials and passive aerodynamics inspired by samaras (maple seeds).

Each design integrates:
- A 3D-printed biodegradable body (PLA/PVA)
- Colour-based pH sensing using flavin powder
- Passive autorotation and dispersal, with no electronics
- Image analysis and flight tracking using OpenCV


# 3D model:
The maple seed inspired designs were modelled in Autodesk Fusion 360, using a spline-
fitting method based on photographs of dried samaras collected around Bristol. The CAD 
models replicate key morphological features such as:

- Nut and wing shape
- Leading edge thickness
- Centre of gravity biased towards the nut

![Maple seed CAD model](cad_model.jpg) 

# 3D printing parameters:  
- Printer used: Bambulab P1P
- Slicer: Bambu Studio
Materials:
- PLA (Bambulab, 1.75mm)
- PVA (eSun, 1.75mm, water soluble)

# Key print settings:
- Layer height: 0.05mm
- First layer height: 0.05mm
- Infill pattern: cubic
- Infill density: 20%
- Top / bottom pattern: concentric 
- Print orientation: flat (wing-down)

# Printing Notes: 
- Thin models make the prints delicate. Take care when removing from the bed. 
- PVA filament is highly moisture sensitive. Ensure it is dry before use to prevent poor extrusion.

  # Sample frames:
  A set of example thresholded frames are included for demonstrating the tracking process:
  <p align="center">
  <img src="<img width="1920" height="1080" alt="frame_181" src="https://github.com/user-attachments/assets/f93d7379-73bf-4d49-96c8-f6573800c67e" />
" width="30%">
  <img src="<img width="1920" height="1080" alt="frame_188" src="https://github.com/user-attachments/assets/ea39b433-c4d8-4c46-ba7c-22b4794efd39" />
" width="30%">
  <img src="<img width="1920" height="1080" alt="frame_192" src="https://github.com/user-attachments/assets/8ba706d8-6675-4ba0-98ea-4acb44406660" />
" width="30%">
</p>
