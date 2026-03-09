from PIL import Image


def resize_image(input_path, output_path, size):
    image = Image.open(input_path)
    resized = image.resize(size)
    resized.save(output_path)


def convert_to_grayscale(input_path, output_path):
    image = Image.open(input_path)
    gray = image.convert("L")
    gray.save(output_path)