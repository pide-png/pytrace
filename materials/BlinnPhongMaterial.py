import numpy as np
from utils import *
from materials.Material import Material


class BlinnPhongMaterial(Material):
    def __init__(self, color):
        super().__init__(color)

    def get_color(self, surface_normal, ambient, lights, intersection, camera, hitables, max_reflections):
        illumination = np.zeros(3)
        illumination += self.color["ambient"] * ambient
        camera_vector = normalize(camera - intersection)
        for light in lights:
            shadow_ray = normalize(light.position - (intersection + 1e-5 * surface_normal))
            is_shadowed = False
            for hitable in hitables:
                if hitable.intersect(shadow_ray, intersection + 1e-5 * surface_normal):
                    is_shadowed = True
            if np.dot(shadow_ray, surface_normal) >= 0 and not is_shadowed:
                illumination += self.color["diffuse"] * light.diffuse * np.dot(shadow_ray, surface_normal)
                illumination += self.color["specular"] * light.diffuse * np.dot(surface_normal, normalize(shadow_ray + camera_vector)) ** (self.color["shininess"] / 4)
        try:
            illumination += self.color["reflection"] * ray_trace(origin=intersection, direction=camera_vector - 2 * np.dot(camera, surface_normal) * surface_normal, hitables=hitables, ambient=ambient, lights=lights, max_reflections=max_reflections)
        except TypeError:
            pass
        return illumination
