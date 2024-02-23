from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
from os.path import exists


class ImageGenerator:
    def __init__(self):
        pass

    @staticmethod
    def generate_clock_image():
        time = str(datetime.time(datetime.now()))[0:5]
        img_link = f"img/{time}.png"
        if not exists(img_link):
            image = Image.new('RGB', (200, 200), color='black')

            draw = ImageDraw.Draw(image)

            font = ImageFont.truetype('fonts/digital-7.ttf', size=50)

            text_x = (image.width - font.getlength(time)) / 2
            text_y = (image.height - font.size) / 2
            draw.text((text_x, text_y), time, fill='red', font=font)

            image.save(img_link)
        return img_link
