import matplotlib.pyplot as plt
import random
from utils import *
import beepy


# noinspection DuplicatedCode
class Scene:
    def __init__(self, camera, width, height, image_plane, antialiasing, ambient):
        self.camera = camera
        self.width = width
        self.height = height
        self.image_plane = image_plane
        self.antialiasing = antialiasing
        self.hitables = []
        self.lights = []
        self.ambient = ambient

    # noinspection PyShadowingNames
    def ray_trace(self, alpha, beta):
        image_point = lerp(
            lerp(self.image_plane[0], self.image_plane[1], alpha),
            lerp(self.image_plane[2], self.image_plane[3], alpha),
            beta
        )  # take the bilinear interpolation to get the actual image point
        intersected_objects = []
        for obj in self.hitables:
            if obj.intersect(image_point, self.camera):
                intersected_objects.append(obj)
        try:
            closest_object = sorted(intersected_objects, key=(lambda obj: obj.intersect(image_point, self.camera)))[0]
            return closest_object.get_color(self.camera, image_point, self.ambient, self.lights, self.hitables, )
        except IndexError:
            return np.array([0, 0, 0])

    def add_hitable(self, hitable):
        self.hitables.append(hitable)

    def add_light(self, light):
        self.lights.append(light)

    def render(self, name, beeps):
        image = np.empty((self.height, self.width, 3))

        for y, row in enumerate(image):
            for x, pixel in enumerate(row):
                rays = []
                # image[y][x] = ray_trace(x / width, y / height)
                for i in range(self.antialiasing):
                    rays.append(self.ray_trace((x + random.random()) / self.width, (y + random.random()) / self.height))

                image[y][x] = np.clip(np.array(rays).mean(axis=0), 0, 1)

        plt.imsave(name, image)
        for i in range(beeps):
            beepy.beep(sound="ping")
