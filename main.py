from PIL import Image

step = 50
step50 = step/2

image = Image.open("monro.jpg")
red, green, blue = image.split()

monro_left_red = (step, 0, red.width, red.height)
cropped_left_red = red.crop(monro_left_red)
monro_middle_red = (step50, 0, red.width - step50, red.height)
cropped_middle_red = red.crop(monro_middle_red)
displaced_red = Image.blend(cropped_left_red, cropped_middle_red, 0.5)

monro_left_blue = (0, 0, blue.width-step, blue.height)
cropped_left_blue = blue.crop(monro_left_blue)
monro_middle_blue = (step50, 0, blue.width - step50, blue.height)
cropped_middle_blue = blue.crop(monro_middle_blue)
displaced_blue = Image.blend(cropped_left_blue, cropped_middle_blue, 0.5)

monro_middle_green = (step50, 0, green.width - step50, green.height)
cropped_middle_green = green.crop(monro_middle_green)

new_image = Image.merge("RGB", (displaced_red, cropped_middle_green, displaced_blue))
new_image.save("monro_ava.jpg")
new_image.thumbnail((80, 80))
new_image.save("monro_ava_80.jpg")