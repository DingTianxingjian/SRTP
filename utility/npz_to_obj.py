import numpy as np

'''
  Transfer points array to .obj file
  @param obj_file_name: The given name of .obj file
  @param points: The array of points, where each point is 3-dimensional
'''
def PointsToObj(obj_file_name, points):
    with open(file = obj_file_name, mode = 'w') as obj:
        output = '# ' + repr(len(points) + '\n')
        for i in range(len(points)):
            output = 'v ' + repr(points[i][0]) + ' ' + repr(points[i][1]) + ' ' + repr(points[i][2]) + '\n'
            obj.write(output)

'''
  Transfer .npz file to .obj file
  @param obj_file_name: The given name of .obj file
  @param npz_file_name: .npz file extracted from ShapeNet, containing 3-dimensional coordinates of all the points
'''
def NpzToObj(obj_file_name, npz_file_name):
    data = np.load(npz_file_name)
    points = data['points']
    PointsToObj(obj_file_name, points)