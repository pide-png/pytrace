import numpy as np
from utils import normalize
from materials.Material import Material


class BlinnPhongMaterial(Material):
    def __init__(self, color):
        super().__init__(color)

    def get_color(self, surface_normal, ambient, lights, intersection, camera, hitables, _id):
        illumination = np.zeros(3)
        illumination += self.color["ambient"] * ambient
        for light in lights:
            light_vector = normalize(light.position - intersection)
            if np.dot(light_vector, surface_normal) < 0:
                continue
            is_shadowed = False
            for hitable in hitables:
                """if hitable.id == _id:
                    print("me!")
                    continue"""
                if hitable.intersect(light_vector, intersection):
                    print("shadow")
                    is_shadowed = True
                    break
            if not is_shadowed:
                illumination += self.color["diffuse"] * light.diffuse * np.dot(light_vector, surface_normal)
                reflectance = normalize(2 * np.dot(surface_normal, light_vector) * surface_normal - light_vector)
                view = normalize(intersection - camera)
                illumination += self.color["specular"] * light.specular * np.dot(view, reflectance) ** self.color["shininess"]
        return illumination
