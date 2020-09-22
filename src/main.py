from src.image import Image
from src.color import Color


def main():
    width = 3
    height = 2
    image = Image(width, height)
    red = Color(1, 0, 0)
    green = Color(0, 1, 0)
    blue = Color(0, 0, 1)
    image.set_pixel(0, 0, red)
    image.set_pixel(1, 0, green)
    image.set_pixel(2, 0, blue)

    image.set_pixel(0, 1, red + green)
    image.set_pixel(1, 1, red + green + blue)
    image.set_pixel(2, 1, red * 0.001)

    with open('test_image.ppm', 'w') as _image_file:
        image.write_ppm(_image_file)


if __name__ == '__main__':
    main()
