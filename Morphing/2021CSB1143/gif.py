import imageio.v2 as imageio
# if not installed, do `conda install imageio`
import os

images = []

for i in range(100):
    fname= f'morph/img{i}.png'
    print(fname)
    images.append(imageio.imread(fname))


imageio.mimsave('movie.gif', images)