import textwrap
from PIL import Image, ImageDraw, ImageFont

text = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et " \
       "dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet " \
       "clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."

image_width = 1000
image_height = 1200
left_padding = 50
top_padding = 100
color_background = (255, 255, 255)
color_text = (0, 0, 0)
font_size = 50
wrapping_width = 30
font_path = "YOUR_FILE_PATH/SourceHanSerifSC-Regular.otf"

# wrap text
printed_string = ""
wrapped_text = textwrap.wrap(text, width=wrapping_width)
for line in wrapped_text:
    printed_string = printed_string + line + "\n"

# create image
img = Image.new('RGB', (image_width, image_height), color=color_background)
my_image = ImageDraw.Draw(img)

# print text to image
my_fonts = ImageFont.truetype(font_path, font_size)
my_image.text((left_padding, top_padding), printed_string, fill=color_text, font=my_fonts)

# save image
img.save('image_file.jpg')
