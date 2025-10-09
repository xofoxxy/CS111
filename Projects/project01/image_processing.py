import sys

import byuimage


def validate_input(args):
    flag = args[1]
    if flag in command_requirements:
        for requirement in range(len(command_requirements[flag])):
            if command_requirements[flag][requirement] is not None:
                try:
                    requirement_type = command_requirements[flag][requirement]
                    requirement_value = args[requirement + 2]
                    requirement_type(requirement_value)
                    # if requirement_type is str:
                    #     if not os.path.exists(requirement_value):
                    #         return False
                except (ValueError, IndexError) as e:
                    print(f"error: {e}")
                    return False
        print()
        return True
    else:
        return False


def display(filepath):
    image = byuimage.Image(filepath)
    image.show()


def darken(filepath, output_filepath, percentage):
    image = byuimage.Image(filepath)
    percentage = 1 - float(percentage)
    for pixel in image:
        pixel.color = (pixel.red * percentage, pixel.green * percentage, pixel.blue * percentage)
    image.show()
    image.save(output_filepath)


def sepia(filepath, output_filepath):
    image = byuimage.Image(filepath)
    for pixel in image:
        true_red = 0.393 * pixel.red + 0.769 * pixel.green + 0.189 * pixel.blue
        true_green = 0.349 * pixel.red + 0.686 * pixel.green + 0.168 * pixel.blue
        true_blue = 0.272 * pixel.red + 0.534 * pixel.green + 0.131 * pixel.blue
        if true_red > 255:
            true_red = 255
        if true_green > 255:
            true_green = 255
        if true_blue > 255:
            true_blue = 255
        pixel.color = (true_red, true_green, true_blue)
    image.show()
    image.save(output_filepath)


def grayscale(filepath, output_filepath):
    image = byuimage.Image(filepath)
    for pixel in image:
        average_color = (pixel.red + pixel.green + pixel.blue) / 3
        pixel.color = (average_color, average_color, average_color)
    image.show()
    image.save(output_filepath)


def border(filepath, output_filepath, width, r, g, b):
    width, r, g, b = int(width), int(r), int(g), int(b)
    image = byuimage.Image(filepath)
    new_image = byuimage.Image.blank(image.width + width * 2, image.height + width * 2)
    for pixel in new_image:
        pixel.color = (r, g, b)
    for x in range(image.width):
        for y in range(image.height):
            new_image.pixels[x + width, y + width] = image.pixels[x, y]
    new_image.show()
    new_image.save(output_filepath)


def flip_vertically(filepath, output_filepath):
    image = byuimage.Image(filepath)
    new_image = byuimage.Image.blank(image.width, image.height)
    for x in range(image.width):
        for y in range(image.height):
            new_image.pixels[x, y] = image.pixels[x, -y - 1]
    new_image.show()
    new_image.save(output_filepath)


def mirror_horizontally(filepath,  output_filepath):
    image = byuimage.Image(filepath)
    new_image = byuimage.Image.blank(image.width, image.height)
    for x in range(image.width):
        for y in range(image.height):
            new_image.pixels[x, y] = image.pixels[-x - 1, y]
    new_image.show()
    new_image.save(output_filepath)


def collage(filepath1, filepath2, filepath3, filepath4, output_image, border_width):
    border_width = int(border_width)

    image1 = byuimage.Image(filepath1)
    image2 = byuimage.Image(filepath2)
    image3 = byuimage.Image(filepath3)
    image4 = byuimage.Image(filepath4)

    images = [image1, image2, image3, image4]
    image_location = [[0,0],[1,0],[0,1],[1,1]]


    new_image = byuimage.Image.blank(image1.width + image2.width + border_width*3, image1.height + image3.height + border_width*3)

    for pixel in new_image:
        pixel.color = (0, 0, 0)
    for image_locaiton_pairs in zip(image_location, images):
        for x in range(image_locaiton_pairs[1].width):
            for y in range(image_locaiton_pairs[1].height):
                x_offset = (image_locaiton_pairs[0][0]+1) * border_width + image1.width * image_locaiton_pairs[0][0]
                y_offset = (image_locaiton_pairs[0][1]+1) * border_width + image1.height * image_locaiton_pairs[0][1]
                new_image.pixels[x+x_offset, y+y_offset] = image_locaiton_pairs[1].pixels[x, y]

    new_image.show()
    new_image.save(output_image)


def green_screen(filepath1, filepath2, output_image, threshold, factor):
    threshold = float(threshold)
    factor = float(factor)

    def detect_green(pixel):
        average = (pixel.red + pixel.green + pixel.blue) / 3
        if pixel.green >= factor * average and pixel.green > threshold:
            return True
        else:
            return False

    image1 = byuimage.Image(filepath1) #Foreground
    image2 = byuimage.Image(filepath2) #Background
    width = max([image1.width, image2.width])
    height = max([image1.height, image2.height])

    new_image = byuimage.Image.blank(width, height)
    for x in range(new_image.width):
        for y in range(new_image.height):
            if detect_green(image1.get_pixel(x, y)):
                try:
                    new_image.pixels[x, y] = image2.pixels[x, y]
                except IndexError:
                    new_image.pixels[x, y].color = (0, 0, 0)
            else:
                new_image.pixels[x, y] = image1.pixels[x, y]
    new_image.show()
    new_image.save(output_image)




if __name__ == "__main__":
    command_requirements = {
        "-d": [str],  # Display
        "-k": [str, str, float],  # Darken
        "-s": [str, str],  # Sepia filter
        "-g": [str, str],  # Grayscale
        "-b": [str, str, int, int, int, int],  # Apply a border (filepath, width, r, g, b)
        "-f": [str, str],  # Flip vertically
        "-m": [str, str],  # Mirror horizontally
        "-c": [str, str, str, str, str, int],  # Collage
        "-y": [str, str, str, float, float], # Green Screen
    }

    commands_dict = { # Dicrionary of commands and their respective functions so that I can avoid a lot of if statements.
        "-d": display,
        "-k": darken,
        "-s": sepia,
        "-g": grayscale,
        "-b": border,
        "-f": flip_vertically,
        "-m": mirror_horizontally,
        "-c": collage,
        "-y": green_screen,
    }

    if validate_input(sys.argv):
        print("Valid input")
        flag = sys.argv[1]
        commands_dict[flag](*sys.argv[2:])
    else:
        print("Invalid input")
