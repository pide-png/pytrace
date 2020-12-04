from utils import *


class Sphere:
    def __init__(self, centre, radius, material):
        self.centre = centre
        self.radius = radius
        self.material = material

    def intersect(self, direction, origin):
        a = np.linalg.norm(direction) ** 2
        b = 2 * np.dot(origin - self.centre, direction)
        c = np.linalg.norm(origin - self.centre) ** 2 - self.radius ** 2
        discriminant = b ** 2 - 4 * a * c
        if discriminant > 0:
            t1 = (-b + np.sqrt(discriminant)) / 2
            t2 = (-b - np.sqrt(discriminant)) / 2
            if t1 > 0 and t2 > 0:
                return min(t1, t2)

    def normal(self, camera, image_point):
        intersection = lerp(camera, image_point, self.intersect(image_point, camera))
        return normalize(intersection - self.centre)

    def get_color(self, camera, image_point, ambient, lights, hitables, max_reflections):
        intersection = lerp(camera, image_point, self.intersect(image_point, camera))
        return self.material.get_color(self.normal(camera, image_point), ambient, lights, intersection, camera,
                                       hitables, max_reflections=max_reflections)
