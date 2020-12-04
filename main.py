from Light import Light
from Scene import Scene
from hitables.Sphere import Sphere
from materials.BlinnPhongMaterial import BlinnPhongMaterial
from utils import *

cameraPos = np.array([0, 0, 0])

width, height = 640, 360

imagePlane = np.array([
    [-0.89, +0.5, 1], [+0.89, +0.5, 1],
    [-0.89, -0.5, 1], [+0.89, -0.5, 1]
])

scene = Scene(cameraPos, width, height, imagePlane, 1, np.array([1, 1, 1]), 3)

scene.add_hitable(Sphere(centre=np.array([-0.2, 0, 5]), radius=1.5, material=BlinnPhongMaterial({
    "ambient": np.array([0.1, 0, 0]),
    "diffuse": np.array([0.7, 0, 0]),
    "specular": np.array([1, 1, 1]),
    "shininess": 100,
    "reflection": 1
})))

scene.add_hitable(Sphere(centre=np.array([-0.3, 0, 1]), radius=0.15, material=BlinnPhongMaterial({
    "ambient": np.array([0, 0.1, 0]),
    "diffuse": np.array([0, 0.7, 0]),
    "specular": np.array([1, 1, 1]),
    "shininess": 100,
    "reflection": 1
})))


scene.add_hitable(Sphere(centre=np.array([0, -9000, 1]), radius=9000 - 1.5, material=BlinnPhongMaterial({
    "ambient": np.array([0.1, 0.1, 0.1]),
    "diffuse": np.array([0.7, 0.7, 0.7]),
    "specular": np.array([1, 1, 1]),
    "shininess": 100,
    "reflection": 1
})))

scene.add_light(Light(position=np.array([5, 5, -4]), diffuse=np.array([1, 1, 1]), specular=np.array([1, 1, 1])))

scene.render("output.png", 3)
