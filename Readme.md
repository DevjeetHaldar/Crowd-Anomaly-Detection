# CROWD ANOMALY DETECTION


1. Optical flow of blocks (optFlowofblocks.py)

The module optical flow of blocks is provided with a frame and the optical flow of a frame. It divides the frame into blocks of size m x n and sums all the optical flows in each block
and returns it along with details like m, n, size and center of blocks.

2. Motion Influence Generator (motionInfluenceGenerator.py)

This module is provided with training or testing video and it calculates the motion
influence map for each frame in that video and also returns the size of the blocks in the motion influence map.

3. Megablock Generator (createMegaBlocks.py)

This module has 2 functionalities.

a) Generating megablocks and returning them (testing)
Megablocks are generated by grouping motion influence blocks into a bigger sized blocks
as motions of closely situated blocks are similar. 

A set of megablocks of size (number of frames * number of megablocks in each row * number of megablocks each column) is returned.

b) Generating megablocks and returning codewords (training)
After repeating the above process but before returning the set of megablocks, each set of
megablocks present in the same frame position is applied kmeans clustering on and the means
called codewords are only returned to the calling module.


4.  Training module (training.py)

Training module calls motion influence generator and megablock generator to obtain
codewords on a training video input. It then stores codewords in a .npy(NumPY file).


5. Testing module (testing.py)

Testing module calls motion influence generator and megablock generator to obtain
megablocks on a testing video input. It then constructs a minimum distance matrix after loading
the stored codewords, checks if a megablock is unusual by comparing it against a threshold value
and displays unusual megablocks and frames.



Datset Description

UMN:
Crowd Escape Panic, 11 Videos, 3 Scenes, Videos: a normal starting section and an abnormal ending section.
We parcelled each edge into 8×8 non overlapping squares, and set the edge to the most extreme highlight an incentive in the movement impact guides of the preparation pictures. The basis for this methodology is that we expect the unusual exercises to bring about higher movement impact esteems than the typical exercises.

Peds1: 
clasps of gatherings of individuals strolling towards and away from the camera, and some measure of point of view mutilation. Contains 34 preparing video tests and 36 testing video tests.

Peds2:
scenes with passer by development corresponding to the camera plane. Contains 16 preparing video tests and 12 testing video tests.

<img width="932" alt="image" src="https://user-images.githubusercontent.com/99869699/232675132-d238dae7-490a-48d8-bee9-6194ae116772.png">


Language: Python

Tools: Numpy, OpenCV2

Database/Datasets: UMN,  Peds1, Peds2.

Limitations of The Solution  

The proposed method has a limitation when there is a strong perspective distortion in the input video as the motion influence map is built based on the motion direction and magnitude of the moving objects. However, the main focus of this work is to detect unusual activities within a crowded scene, for which the cameras usually cover a wide area, resulting in small objects being present in the scene without significant perspective changes. 

