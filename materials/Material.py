class Material:
    def __init__(self, color):
        self.color = color

    def get_color(self, surface_normal, ambient, lights, intersection, camera, hitables):
        raise NotImplementedError
