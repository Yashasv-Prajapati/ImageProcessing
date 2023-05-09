How to run?
run the .ipynb file in jupyter notebook

There are two functions, GenerateTiePoints and takePointsFromTextFile, either one can be used to run the code to get the tie points

It uses delaunay triangulation on two images say A and B, and converts the image A and B to small triangles and then warps those triangles in A and B to the intermediate triangle obtained from both the images which is (1-alpha)*A + alpha*B, where alpha is some factor.

.gif file is generated using the gif.py file.