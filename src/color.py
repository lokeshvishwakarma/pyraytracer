from src.vector import Vector


class Color(Vector):
    def __init__(self, R, G, B):
        """
        Color class which is represented using a Vector class
        :param R: between 0 to 1
        :param G: between 0 to 1
        :param B: between 0 to 1
        """
        super().__init__()
        self.x = R
        self.y = G
        self.z = B
