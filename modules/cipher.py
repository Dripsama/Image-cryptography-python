from PIL import Image

def generate_ciphered_image(secret_image, prepared_image):
    width, height = prepared_image.size
    ciphered_image = Image.new(mode = "1", size = (width * 2, height * 2))
    for x in range(0, width*2, 2):
        for y in range(0, height*2, 2):
            secret = secret_image.getpixel((x,y))
            message = prepared_image.getpixel((x/2,y/2))
            if (message > 0 and secret > 0) or (message == 0 and secret == 0):
                color = 0
            else:
                color = 1

    return ciphered_image
