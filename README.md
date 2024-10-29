Project #1: Data-Driven Feature Tracking with Privacy Filtering for Aerial Imagery

Objective:
Apply a data-driven feature tracking method, originally designed for event cameras, to aerial imagery to extract features and build feature tracks over an image sequence. These tracks will be used to estimate 3D camera poses using a Structure-from-Motion (SfM) algorithm. Additionally, implement a privacy filtering mechanism to obscure identifiable information within the imagery. The project will also evaluate the quality of the recovered camera poses and assess the effectiveness of the privacy filter.

Goals:

Develop a robust feature tracking pipeline for aerial imagery using event cameras.
Build feature tracks from the aerial image sequence and integrate them with an SfM algorithm to estimate 3D camera poses.
Implement and integrate a privacy filtering method to protect sensitive information in the imagery.
Evaluate the accuracy and reliability of the reconstructed camera poses, as well as the effectiveness of the privacy filter.
Dataset:
Aerial imagery captured using event cameras and RGB cameras (will be provided).

Steps:

Feature Extraction from Aerial Imagery:

Extract features from aerial images using the data-driven feature tracking method proposed by Messikommer et al. ("Data-Driven Feature Tracking for Event Cameras," CVPR 2023). This paper will serve as the baseline for this project.
Adapt the event-based feature tracking method to work with aerial imagery, focusing on leveraging the high temporal resolution of event data.
Privacy Filtering on Aerial Imagery:

Apply a privacy filter to the aerial imagery to obscure identifiable information before feature extraction.
Design the privacy filter to selectively blur or mask sensitive areas, ensuring minimal impact on feature extraction and tracking accuracy.
Feature Tracking Across Image Sequence:

Track features over time to build a consistent set of feature tracks across the entire sequence of aerial images. Utilize the novel frame attention module introduced by Messikommer et al. to share information across different feature tracks in a single frame.
Generate Feature Tracks for SfM:

Use the extracted feature tracks to create inputs for the SfM algorithm. The feature tracks should be accurate and consistent across the sequence, with privacy filtering maintained throughout.
3D Pose Estimation with SfM:

Apply an SfM algorithm, such as COLMAP and BA4S, to the tracked features to estimate the 3D camera poses. Use the tracked features as inputs to ensure robustness in pose estimation.
Evaluation of Results:

Evaluate the quality of the estimated 3D camera poses. Metrics should include accuracy, consistency of feature tracks, robustness to different environmental conditions, and effectiveness of the privacy filter.
Expected Deliverables:

A report detailing the methodology, experiments, results, and key findings.
Evaluation metrics comparing feature tracking accuracy, camera pose estimation quality, and privacy filter effectiveness.
Code and relevant documentation for reproducibility.
