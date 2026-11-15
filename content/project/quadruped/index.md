---
title: "Learning by Touching: Contact-Rich Intelligence for Quadruped Robots"
summary: "Enabling quadruped robots to sense and manipulate their environment through whole-body physical contact."
type: book
weight: 5
# Disable author profile block
profile: false
authors: []
share: false
show_date: false

# Front matter buttons at the top of the page
# links:
#   - icon: github
#     icon_pack: fab
#     name: Code
#     url: https://github.com/HORC-Lab
#   - icon: youtube
#     icon_pack: fab
#     name: Video Channel
#     url: https://youtube.com
---

## Project Goal
This project develops tactile sensing and learning-based whole-body control that let quadruped robots use their bodies to perceive, push, and manipulate objects in unstructured environments.

---

## Key Contributions
* <strong style="color: #F97316;">Sensorized Head for Physical Interaction:</strong> Developed Head-On, a helmet for the Unitree Go1 with four soft magnetometer-based tactile sensors in an optimized layout. It turns the robot’s head into a contact surface that can measure 3D interaction forces while pushing and manipulating objects.
* <strong style="color: #F97316;">Drift-Robust Tactile Force Estimation:</strong> Built a learning-based calibration pipeline that works on a moving, floating-base robot. A causal 1D CNN detects contact and resets the sensor baseline to cancel drift, and an LSTM-MLP network maps the magnetic readings to 3D forces with minimum error.
* <strong style="color: #F97316;">Whole-Body Manipulation of Object Stacks:</strong> Introduced SOMA, a hierarchical reinforcement learning framework in which the robot adjusts its body height to push multi-object stacks in 3D without the top layers sliding or tipping. It reached up to 90% success in simulation and transferred zero-shot to the real Go1.

---



## Media & Experimental Demos

<!-- 1-Column Media Layout -->
<div style="display: flex; flex-direction: column; gap: 2rem; margin: 2rem 0; width: 100%;">

  <!-- YouTube Embed 1 -->
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; border-radius: 8px;">
    <iframe src="https://www.youtube.com/embed/hryuHfYyxQs?si=tHSwUitiXljucjU2" style="position: absolute; top:0; left:0; width:100%; height:100%; border:0;" allowfullscreen></iframe>
  </div>


  <!-- YouTube Embed 2 -->
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; border-radius: 8px;">
    <iframe src="https://www.youtube.com/embed/zm-xnCMI1uE?si=p-V8bLsfMT5cao8c" style="position: absolute; top:0; left:0; width:100%; height:100%; border:0;" allowfullscreen></iframe>
  </div>


</div>

<!-- Image Gallery Container -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1rem; margin-bottom: 2rem;">
  <img src="./quad1.png" alt="Experimental Setup" style="width: 100%; height: 300px; object-fit: cover; border-radius: 8px;">
  <img src="./quad2.png" alt="Neural Control Interface" style="width: 100%; height: 300px; object-fit: cover; border-radius: 8px;">
</div>

---

## Selected Publications  
(see [Publications](/publication/) for a complete list)

* **Head-On: Robust Tactile Force Sensing for Quadrupedal Interaction**  
  Stergios Bachoumas, John Cahill and Panagiotis Artemiadis
  *2026 IEEE/RSJ International Conference on Intelligent Robots and Systems*, 2026.
  [[PDF](/papers/bachoumas2026headon.pdf)]



---






## Funding & Acknowledgments
This work has been supported by the following grants:
