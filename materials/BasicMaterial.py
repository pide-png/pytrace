from materials.Material import Material


class BasicMaterial(Material):
    def __init__(self, color):
        super().__init__(color)

    def get_color(self, surface_normal, ambient, lights, intersection, camera, hitables, _id):
        return self.color["color"]
