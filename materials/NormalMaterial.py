from materials.Material import Material


class NormalMaterial(Material):
    def __init__(self, color):
        super().__init__(color)

    def get_color(self, surface_normal, ambient, lights, intersection, camera, hitables, max_reflections):
        return 0.5 * (surface_normal + 1)
