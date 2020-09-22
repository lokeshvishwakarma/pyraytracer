class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [[None for _ in range(width)] for _ in range(height)]

    def set_pixel(self, row, column, color):
        self.pixels[column][row] = color

    def write_ppm(self, _file):
        def to_byte(c):
            return round(max(min(c * 255, 255), 0))

        _file.write("P3 {} {}\n255\n".format(self.width, self.height))
        for row in self.pixels:
            for color in row:
                _file.write('{} {} {} '.format(
                    to_byte(color.x),
                    to_byte(color.y),
                    to_byte(color.z)))
            _file.write('\n')
