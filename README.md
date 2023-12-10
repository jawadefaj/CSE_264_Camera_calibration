# Perspective Correction Project

## Overview
This project focuses on correcting the perspective of building images using advanced image processing techniques. The process is divided into five key parts, each targeting a specific aspect of perspective correction.

## Part 1: Camera Calibration
- **Objective**: Calculate the camera's intrinsic parameters and radial distortion.
- **Method**: Use of chessboard patterns for accurate calibration.

![Chess board](/readme_images/chessboard.png)
![Chess board](/readme_images/camera.png)


## Part 2: Take the Picture
- **Task**: Capture the building image, ensuring conditions are suitable for effective perspective correction.
![undistorted image](/readme_images/undistort.png)

## Part 3: Find Bundles of Parallel Lines
- **Goal**: Identify and group parallel lines in the building image.
- **Importance**: Crucial for determining vanishing points.

![undistorted image](/readme_images/parallel.png)
![undistorted image](/readme_images/camera2.png)

## Part 4: Find Vanishing Directions
- **Process**: Calculate vanishing directions for each line bundle.

![undistorted image](/readme_images/camera4.png)

## Part 5: Find the Rectifying Homography
- **Final Step**: Apply a rectifying homography to correct the building image's perspective.

![undistorted image](/readme_images/camera5.png)