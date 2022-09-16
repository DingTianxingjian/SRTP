基本框架

```
//构建场景
var scene = new THREE.Scene();
//构建对象
var geometry = new THREE.BufferGeometry(); //创建一个Buffer类型几何体对象
//类型数组创建顶点数据
var vertices = new Float32Array([
            0, 0, 0, //顶点1坐标
            50, 0, 0, //顶点2坐标
            0, 100, 0, //顶点3坐标

            0, 0, 0, //顶点4坐标
            0, 0, 100, //顶点5坐标
            50, 0, 0, //顶点6坐标
        ]);
// 创建属性缓冲区对象
var attribue = new THREE.BufferAttribute(vertices, 3); //3个为一组，表示一个顶点的xyz坐标
// 设置几何体attributes属性的位置属性
geometry.attributes.position = attribue;

var material = new THREE.MeshBasicMaterial({
            color: 0x0000ff, //三角面颜色
            side: THREE.DoubleSide //两面可见
        }); //材质对象
//设置顶点法向量
var normals = new Float32Array([
            0, 0, 1, //顶点1法向量
            0, 0, 1, //顶点2法向量
            0, 0, 1, //顶点3法向量

            0, 1, 0, //顶点4法向量
            0, 1, 0, //顶点5法向量
            0, 1, 0, //顶点6法向量
        ]);
geometry.attributes.normal = new THREE.BufferAttribute(normals, 3);

var mesh = new THREE.Mesh(geometry, material); //点模型对象
scene.add(mesh);

//插入坐标轴
var axesHelper = new THREE.AxesHelper(250);
scene.add(axesHelper);

var point = new THREE.PointLight(0xffffff);
point.position.set(100, 100, 300); //点光源位置
scene.add(point); //点光源添加到场景中

//环境光
var ambient = new THREE.AmbientLight(0x444444);
scene.add(ambient);

var width = window.innerWidth; //窗口宽度
var height = window.innerHeight; //窗口高度
var k = width / height; //窗口宽高比
var s = 200; //三维场景显示范围控制系数，系数越大，显示的范围越大
//创建相机对象
var camera = new THREE.OrthographicCamera(-s * k, s * k, s, -s, 1, 1000);
camera.position.set(100, 100, 200); //设置相机位置
camera.lookAt(scene.position); //设置相机方向(指向的场景对象)

var renderer = new THREE.WebGLRenderer();
renderer.setSize(width, height);//设置渲染区域尺寸
renderer.setClearColor(0xb9d3ff, 1); //设置背景颜色
document.body.appendChild(renderer.domElement); //body元素中插入canvas对象

let T0 = new Date();//上次时间
function render() {
            let T1 = new Date();//本次时间
            let t = T1-T0;//时间差
            T0 = T1;//把本次时间赋值给上次时间
            requestAnimationFrame(render);
            renderer.render(scene, camera);//执行渲染操作
            //axesHelper.rotateY(0.01);//旋转角速度0.001弧度每毫秒
            //mesh2.rotateY(0.01);//旋转角速度0.001弧度每毫秒
            //mesh3.rotateY(0.01);//旋转角速度0.001弧度每毫秒

        }


        //setInterval("render()",20);
render();
var controls = new THREE.OrbitControls(camera, renderer.domElement);//创建控件对象
controls.addEventListener('change', render);//监听鼠标、键盘事件
```

