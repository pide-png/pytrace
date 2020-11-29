import numpy as np
from utils import normalize
from materials.Material import Material


class BlinnPhongMaterial(Material):
    def __init__(self, color):
        super().__init__(color)

    def get_color(self, surface_normal, ambient, lights, intersection, camera, hitables):
        illumination = np.zeros(3)
        illumination += self.color["ambient"] * ambient
        for light in lights:
            light_vector = normalize(light.position - intersection)
            if np.dot(light_vector, surface_normal) >= 0:
                illumination += self.color["diffuse"] * light.diffuse * np.dot(light_vector, surface_normal)

                camera_vector = normalize(camera - intersection)
                illumination += self.color["specular"] * light.diffuse * np.dot(surface_normal, normalize(light_vector + camera_vector)) ** (self.color["shininess"] / 4)

        return illumination
