# npz_to_obj.py

### 功能

将.npz格式文件转为.obj格式文件

利用ParaView软件，便于点云可视化

### 使用

1. 将`npz_to_obj.py`和需要转换的`pointcloud.npz`文件放在同一路径下
2. 运行`npz_to_obj.py`，生成文件`pointcloud.obj`
3. 用ParaView软件打开，将左下角的Representation选项修改为“Point Gaussian”，即可呈现点云
