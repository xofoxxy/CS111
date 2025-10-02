from byuimage import Image


def flipped(filename):
    image = Image(filename)
    new_image = Image.blank(image.width, image.height)
    for x in range(image.width):
        for y in range(image.height):
            new_image.pixels[x, y] = image.pixels[x, -y-1]
    new_image.show()
    return new_image


def make_borders(filename, thickness, red, green, blue):
    image = Image(filename)
    image.show()
    print("no image")
    new_image = Image.blank(image.width+thickness*2, image.height+thickness*2)
    for pixel in new_image:
        pixel.color = (red, green, blue)
    for x in range(image.width):
        for y in range(image.height):
            new_image.pixels[x+thickness, y+thickness] = image.pixels[x, y]
    new_image.show()
    return new_image


if __name__ == "__main__":
    filepath = input()
    flipped(filepath)
    make_borders(filepath, 20, 20, 20, 20)
    pass

