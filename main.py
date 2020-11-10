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

scene = Scene(cameraPos, width, height, imagePlane, 1, np.array([1, 1, 1]))


scene.add_hitable(Sphere(centre=np.array([0, 0, 6]), radius=2, material=BlinnPhongMaterial({
    "ambient": np.array([0.6, 0, 0]),
    "diffuse": np.array([1, 0, 0]),
    "specular": np.array([1, 1, 1]),
    "shininess": 100
}), _id=0))
scene.add_hitable(Sphere(centre=np.array([1, 0, 3]), radius=0.5, material=BlinnPhongMaterial({
    "ambient": np.array([0, 0.6, 0]),
    "diffuse": np.array([0, 1, 0]),
    "specular": np.array([1, 1, 1]),
    "shininess": 100
}), _id=1))
"""
scene.add_hitable(Sphere(centre=np.array([-3, 3, 10]), radius=1, material=BlinnPhongMaterial({
    "ambient": np.array([0, 0, 0.6]),
    "diffuse": np.array([0, 0, 1]),
    "specular": np.array([1, 1, 1]),
    "shininess": 100
})))
"""
scene.add_light(Light(position=np.array([5, 7, 0]), diffuse=np.array([1, 1, 1]), specular=np.array([1, 1, 1])))

scene.render("output.png", 3)
