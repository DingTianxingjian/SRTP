import numpy as np

# read point information from .npz file
data = np.load('pointcloud.npz')
points = data['points']

# # create an .obj file and write point data into it
with open(file = 'pointcloud.obj', mode = 'w') as obj:
    for i in range(len(points)):
        output = 'v ' + repr(points[i][0]) + ' ' + repr(points[i][1]) + ' ' + repr(points[i][2]) + '\n'
        obj.write(output)