from PIL import Image

def generate_secret(size, secret_image = None):
    width, height = size
    new_secret_image = Image.new(mode = "1", size = (width * 2, height * 2))
    if secret_image:
        old_width, old_height = secret_image.size
    else:
        old_width, old_height = (-1, -1)

    for x in range(0, 2 * width, 2):
        for y in range(0, 2 * height, 2):
            if x < old_width and y < old_height:
                color = secret_image.getpixel((x, y))
            else:
                color = random.getrandbits(1)
            #generating secret
            new_secret_image.putpixel((x,  y),   color)
            new_secret_image.putpixel((x+1,y),   1-color)
            new_secret_image.putpixel((x,  y+1), 1-color)
            new_secret_image.putpixel((x+1,y+1), color)
    return new_secret_image