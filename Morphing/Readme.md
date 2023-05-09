# Introduction
This repository includes projects such as:

1. Image Morphing - Using Triangulation

# About
### 1. There are two functions, **GenerateTiePoints** and **takePointsFromTextFile**, either one can be used to run the code to get the tie points

### 2. It uses delaunay triangulation on two images say A and B, and converts the image A and B to small triangles and then warps those triangles in A and B to the intermediate triangle obtained from both the images (which is (1-alpha)*A + alpha*B), where alpha is some factor.

### 3. GIF file is generated using the gif.py file.

# Tools and Libraries Needed
If you don't have any one of the installed, run the command that follows for whichever you don't have installed

1. OpenCv

    ```pip install opencv-python```
2. Numpy

    ```pip install numpy```
3. Matplotlib

    ```pip install matplotlib```
4. Scipy
   
    ```pip install scipy```
5. Dlib
   
    ```pip install dlib```



# How to Run
1. Configure the environment
2. Make sure you have the images that you've loaded, in the directories that are mentioned at the start of the code notebook. Example image is provided in the repository.
3. Run the jupyter notebook