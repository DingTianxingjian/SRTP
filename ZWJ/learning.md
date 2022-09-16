```
filename:assets>javascripts>js>controls>TransformControls.js
```

```
function onMouseUp()   line:1219
```

```
-->function onPointerHover()    line:931
监视鼠标位置
```

```
-->function intersectObjects() line:1232

var point = new THREE.Vector3();//创建一个三维向量

```

```
这个数据不太确定是否是标注框的实际的大小    transformControls
```

![box.png](D:\_Life And Experience\大学\srtp\kitti360-learning\box.png)

```
rect0  line:1240
```

![](D:\_Life And Experience\大学\srtp\kitti360-learning\change.png)

```
rect line:1252

viewPort_heightOffset: 0
viewPort_width: 1
viewPort_widthOffset: 0
viewPortrect_height: 0.7
```

![](D:\_Life And Experience\大学\srtp\kitti360-learning\22.png)

![](D:\_Life And Experience\大学\srtp\kitti360-learning\Matrix4.png)

## Matrix4-Learning!!!!!!

- 如果 w == 1，则向量 (x,y,z,1) 是空间中的一个位置。

- 如果 w == 0，则向量 (x,y,z,0) 是一个方向。

  []: http://www.opengl-tutorial.org/beginners-tutorials/tutorial-3-matrices/
  []: http://www.opengl-tutorial.org/intermediate-tutorials/tutorial-17-quaternions/
  []: https://en.wikipedia.org/wiki/Transformation_matrix

  ![](D:\_Life And Experience\大学\srtp\kitti360-learning\四元数.png)

  

```
object 的matrix and matrixworld
```

![](D:\_Life And Experience\大学\srtp\kitti360-learning\matrix.png)

![](D:\_Life And Experience\大学\srtp\kitti360-learning\matrixworld.png)

```
中间
```

![](D:\_Life And Experience\大学\srtp\kitti360-learning\11.png)

<u>**matrix?**</u>

<u>**matrixworld?**</u>

**<u>scope？？？</u>**

```
worldPosition  世界坐标   line:828

scope.update();//每次使用鼠标旋转画面之后，update()用于更新视角

function onPointerHover()//对于不同的模式进行操作  包括旋转、缩放等line:933
```

## Find point cloud

```
config.js  line:2301
labelingGame.js line:115
```

![](D:\_Life And Experience\大学\srtp\kitti360-learning\33.png)





6.28

```
THREE.PointCloud()批量管理粒子
labelingGaming.js  221  verticles 可以看到所有点云的世界坐标
				   157  导入PLY
http://www.yanhuangxueyuan.com/doc/three.js/matrixrst.html
p.applyMatrix4(T)  对向量p运用矩阵T （如T为平移矩阵，则该语句表示对p进行平移）
```

6.30

```
style.js 296 function getLabels()  应该和tools中的类别产生有关  Color.txt
在color.txt中添加类型并设置rgb和1/0  则能在界面中出现相关的button
```

7.1

```
config.js 1644 在左侧的row中添加addmodel
config.js 1083 添加case可以添加标注框的状态
config.js 1946 objController 代表标注框
				objController 的四个属性？？？
				var objController = {
                    controlCube: null,
                    controlCube2D: null,
                    controlCubeFish1: null,
                    controlCubeFish2: null,
                }
如何进入标注框的坐标系，将模型导入到标注框中
确定标注工具中心的点的坐标
```

7.3

```
modify:在javascripts中添加了build
	   在processing.js中添加了script  476
Content-Type:Content-Type（MediaType），即是Internet Media Type，互联网媒体类型，也叫做MIME类型
```

![image-20220703111947227](C:\Users\86136\AppData\Roaming\Typora\typora-user-images\image-20220703111947227.png)

```
INTERSECTED 双击时选中物体
initClassButton 点击button后调用的函数  插入物体
processing 305  mesh 
```

```
labeling.js 52 添加了loadOBJ函数，模型放在public文件夹中
				注：/static/表示从static文件夹中开始
			141 添加了loadOBJ()
config.js 67 添加全局变量cubeTempplate
processing.js  213 编写代码导入模型

检查文件是否存在
// var result = checkFileExist("/static/models/obj/female02/female02.obj");
				// if (result == true) {
				// 	alert('yay, file exists!');
				// } else {
				// 	alert('file does not exist!');
				// }
```

![image-20220706135509706](C:\Users\86136\AppData\Roaming\Typora\typora-user-images\image-20220706135509706.png)

7.6

```
config.js 67 添加全局变量OBJMeshes 用于存储obj所有的mesh
labeling.js 67 OBJMeshes = obj.children;
scene中添加一个标注之后，会出现一个edgeshelper和mesh


获取three.js内部子模型的真实位置
obj.geometry.computeBoundingSphere();
let realPosition = obj.geometry.boundingSphere.center;
```

7.10

```
创建gemoteryArry 和 materialArray存储导入模型各个部分的gemotery和material  定义位于config.js 69
labelingGame.js 67

```

![image-20220710100043614](C:\Users\86136\AppData\Roaming\Typora\typora-user-images\image-20220710100043614.png)

7.12

example中所给的模型的material

![image-20220714141548708](C:\Users\86136\AppData\Roaming\Typora\typora-user-images\image-20220714141548708.png)

自己用相同代码实现的时候

![image-20220715200522423](C:\Users\86136\AppData\Roaming\Typora\typora-user-images\image-20220715200522423.png)

在materials属性处则没有显示  需要使用preload()函数  但是会报错，因为缺少“图片”？

![image-20220715201038025](C:\Users\86136\AppData\Roaming\Typora\typora-user-images\image-20220715201038025.png)

官网提供的preload函数 和  kitty360提供的preload函数有区别  

放到array

![image-20220715195847601](C:\Users\86136\AppData\Roaming\Typora\typora-user-images\image-20220715195847601.png)

但是无法使用Buffermerge函数    

![image-20220715200046567](C:\Users\86136\AppData\Roaming\Typora\typora-user-images\image-20220715200046567.png)

![image-20220715200252653](C:\Users\86136\AppData\Roaming\Typora\typora-user-images\image-20220715200252653.png)

原因是数组中的每一个children（Geometry缺少attributes）  同样方式load  为什么没有attribute属性？







```
shapenet上的模型导入
```

7.17

利用merge()将模型的mesh合并

BufferGeometry和Geometry有区别

```
//labelingGame.js 56
function loadOBJ() {
	var OBJLoader = new THREE.OBJLoader();
	function onError() { }
	function onProgress(xhr) {
		if (xhr.lengthComputable) {
			const percentComplete = xhr.loaded / xhr.total * 100;
			console.log('model ' + Math.round(percentComplete, 2) + '% downloaded');

		}
	}
	const cubeMaterial = new THREE.MeshNormalMaterial({
		transparent: true,
		opacity: 0.5
	})
	OBJLoader.load('/static/models/obj/female02/female02.obj', function (obj) {
		const mergedGeometries = new THREE.Geometry();
		for (var i = 0; i < obj.children.length; i++) {
			obj.children[i].updateMatrix();
			mergedGeometries.merge(obj.children[i].geometry, obj.children[i].matrix);
		}
		console.log(mergedGeometries);
		mergeMesh = new THREE.Mesh(mergedGeometries, cubeMaterial);
	}, onProgress, onError);

}

//config.js 68 
var mergeMesh;
var add_OBJ;
```

7.18

```
config.js  1890
function attachControlCubes(obj, mode, isAttach)
双击后能够得到被双击物体的信息
添加obj_position，记录被双击物体的position
需要得到obj.name.buttonId（即为标注框的category）

config.js 1646
var obj = {
		AddModel: function () {
			add_model(true);
		}
	};
	gui.add(obj, 'AddModel').name('Add Model').listen();

processing.js
//判断是否点击了添加模型的按钮，且需要判断标注框是否选定
function add_model(activated) {

	if (activated == true && INTERSECTED) {
		console.log("add_model");
		// scene.add(add_OBJ);
	}
}


loadOBJ时需要传递classId  info
为此设置了全局变量
var OBJ_classId;
var OBJ_info;
注意赋值时，不仅仅需要在点击添加新的标注框时可以进行，而且需要在双击已有的标注框时也能够赋值
“在双击已有的标注框时也能够赋值” 在函数
	function attachControlCubes(obj, mode, isAttach)
中完成

processing.js 5127
是否点击了添加模型的按钮，且需要判断标注框是否选定
function add_model(activated) {
	if (activated == true && INTERSECTED) {

		loadOBJ();

		add_OBJ = mergeMesh;
		add_OBJ.scale.set(category[OBJ_classId].scale[0] * 0.01, category[OBJ_classId].scale[1] * 0.01, category[OBJ_classId].scale[2] * 0.01);
		console.log(OBJ_position);
		add_OBJ.position.x = OBJ_position.x;
		add_OBJ.position.y = OBJ_position.y;
		add_OBJ.position.z = OBJ_position.z;

		add_OBJ.name = OBJ_info;
		add_OBJ.geometry.computeBoundingBox();
		add_OBJ.geometry.computeBoundingSphere();

		labels.push(add_OBJ);
		scene.add(add_OBJ);
		console.log(add_OBJ)

		var wireframe = new THREE.EdgesHelper(add_OBJ, WIREFRAME_COLOR[OBJ_info.dynamic]);
		wireframe.material.linewidth = 2;
		wireframe.updateMatrixWorld();
		labels_helper.push(wireframe);
		scene.add(wireframe);
		planes.push(0);
		plane_helpers.push(0);
		
		
		//这一部分代码貌似是当添加进去的模型后，更新arrow  将新导入的模型的arrow push到新的				arrow这个堆里面  若不添加，点击立方体后，添加模型，再点击模型，就会报错，因为原本是要读取模型的arrow，但是由于模型的arrow没有导入到这个堆里面，所以查询不到，为此需要用到下面的代码
		var arrow = addArrow(INTERSECTED.name.label);
		updateArrow(arrow, add_OBJ.quaternion, add_OBJ.scale, add_OBJ.position);
		labels_arrow.push(arrow);

		currentIdx = labels.length - 1;
	}
}

```

8.5

![image-20220805102640328](C:\Users\86136\AppData\Roaming\Typora\typora-user-images\image-20220805102640328.png)

经过处理的obj，和three.js提供的obj相比，缺少了  scale  和   clone （clone需要用到这些Vecrot2，即为纹理坐标）

![image-20220805102846470](C:\Users\86136\AppData\Roaming\Typora\typora-user-images\image-20220805102846470.png)

为了解决这个问题，需要将OBJLoader中的函数add__uvs相关部分注释掉，也就是去掉导入模型的纹理的部分

```
OBJLoader.js
133
153
154
注释之后，应当就是去除了纹理信息
```



8.13

```
processing.js   3964  getPointsInCube()
style.js    325   getMapping()

processing.js     118 
	CLASSID = classId;
config.js中定义CLASSID,用于存储鼠标点击之后得到的按钮的信息
```

8.17

计算地面的高度

```
config.js  737  computeRange()  >>>GROUND_POS  
```

改变点云的可见方式

或许可以改进的地方：隐藏之后，不能恢复可见，只能通过reset 的方式，将所有的隐藏点全部恢复

```
processing.js 
5014 changeCloudVisbility()
inside_cube_list 存储了方框内所有点的不透明度
processing.js    checkInsideBoundingBox(bound, pt)判断点是否在box中

plyParticles.geometry.vertices应该记录了所有的导入的点的坐标
```





inside_vertices中存储了在标注框内的点的坐标

```
在config.js中添加
var check_cube_matrixWorld;
var check_cube_geometry_vertices;

在processing.js  5137 （add_model()函数）内加上
//获得选中的标注框的边界
var boundbox = computeBound(check_cube_geometry_vertices, check_cube_matrixWorld);

//get the points in the box first
var check_vertices = plyParticles.geometry.vertices;
var inside_vertices = new Array();
for (var i = 0; i < check_vertices.length; i++) {
	if (checkInsideBoundingBox(boundbox, check_vertices[i]))
		inside_vertices.push(check_vertices[i]);
}
```

在config.js 中存储了相机坐标

```
loadCameraParaSingle

有三个mode  [0 2 3] 分别为中间，左右两边的相机
不同的相机有不同的CameraIndex

data/frame.txt中存储了实际导入到kitty360中的相机的index
camGroup中存储了部分的camera的index
在fullCameralist中是完整的camera的index

以下函数用于得到最近的相机的坐标（vertice为标注框底面中点）
function new_findNearestCam(vertice) {
	var nearestcamera = new THREE.Vector3();
	var min = vertice.clone().sub(camGroup.vCamera[0].position).clone().dot(vertice.clone().sub(camGroup.vCamera[0].position));
	nearestcamera = camGroup.vCamera[0].position;
	var distance;
	for (var i = 1; i < camGroup.vCamera.length; i++) {
		distance = vertice.clone().sub(camGroup.vCamera[i].position).clone().dot(vertice.clone().sub(camGroup.vCamera[i].position));
		if (distance < min) {
			min = distance;
			nearestcamera = camGroup.vCamera[i].position;
		}
	}
	return nearestcamera;
}
```

问题：

1. 如何衡量点云与不同的点之间的距离（找一找  有确定地面位置    planar stuff        road的标注）
2. checkInsideBoundingBox函数貌似有点问题（求交点的方式函数）

滤波的结果

![image-20220904151439402](C:\Users\86136\AppData\Roaming\Typora\typora-user-images\image-20220904151439402.png)

未滤波时的结果

![image-20220904151340672](C:\Users\86136\AppData\Roaming\Typora\typora-user-images\image-20220904151340672.png)

重新写了一个计算标注框八个点位置的函数 computeBoundvertices   (processing.js 4890)

```
function computeBoundvertices(vertices, matrixWorld) {
	var bounding_vertices = new Array();
	for (var i = 0; i < vertices.length; i++) {
		var vec = vertices[i].clone();
		vec.applyMatrix4(matrixWorld);
		bounding_vertices.push(vec);
	}
	return bounding_vertices;
}
```

重新写了一个判断是否在标注框内部的函数 new_checkInsideBoundingBox   (processing.js) 

立方体中点的分布顺序与bounding_vertices中八个点的顺序相同

![image-20220904151653900](C:\Users\86136\AppData\Roaming\Typora\typora-user-images\image-20220904151653900.png)

![image-20220904152458359](C:\Users\86136\AppData\Roaming\Typora\typora-user-images\image-20220904152458359.png)

判断的原理

![image-20220904151931575](C:\Users\86136\AppData\Roaming\Typora\typora-user-images\image-20220904151931575.png)



```
/**
 * Check if a point is inside a bounding box.
 */
function new_checkInsideBoundingBox(bound, vertices, pt) {
	if (!checkInsideBoundingBox(bound, pt))
		return false;
	var face1 = vertices[0].clone().sub(vertices[2]);
							//.sub()使用是，使用的对象需要.clone(),否则对象本身会发生就会被减掉
	var face2 = vertices[0].clone().sub(vertices[5]);
	var face3 = vertices[0].clone().sub(vertices[1]);
	var v = pt.clone().sub(vertices[0]);
	var v1 = pt.clone().sub(vertices[2]);
	var v2 = pt.clone().sub(vertices[5]);
	var v3 = pt.clone().sub(vertices[1]);
	if (v.clone().dot(face1) * v1.dot(face1) > 0)
		return false;
	if (v.clone().dot(face2) * v2.dot(face2) > 0)
		return false;
	if (v.clone().dot(face3) * v3.dot(face3) > 0)
		return false;
	return true;

}
```

修改判断内部点之后，得到如下结果

滤波之后

![image-20220904160723005](C:\Users\86136\AppData\Roaming\Typora\typora-user-images\image-20220904160723005.png)

滤波之前

![image-20220904160743833](C:\Users\86136\AppData\Roaming\Typora\typora-user-images\image-20220904160743833.png)

如何将js和python结合，取到dense的点云

车子bounding box的xyz  用一个变换矩阵进行调整    车子的方向调整（感觉类似相机的.multiply(matrixworld)）



9.11 
出现的问题：

1. 添加到box之后，重新刷新，车子模型没有了，貌似不能加到标注框的children，得加到scene中
2. 刷新之后，如果之前已经添加了了box，直接点box，会出现bug，set scale会出现问题
3. 提取的坐标 应该需要进一步处理，让



9.12

导入的模型的坐标轴和标注框的坐标轴之间，在旋转的时候坐标轴之间貌似有这样的关系

```
add_OBJ.rotation.x = 0.5 * Math.PI + OBJ.rotation.x;
add_OBJ.rotation.y = 0.5 * Math.PI + OBJ.rotation.y + OBJ.rotation.z;
```

(模型)y——(标注框)z

(模型)z——(标注框)x

(模型)x——(标注框)y



