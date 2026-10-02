from PIL import Image
import numpy as np


image =np.array (Image.open("img/cat.jpg").convert("RGB"))

h, w, _ = image.shape
print("image shape:", h, w, _)


image_crop=image[h//4:h*3//4, w//4:w*3//4]
print("image crop shape:", image_crop.shape)
Image.fromarray(image_crop).save("img/cat_crop.jpg")



image_flip_from_left_to_right = image[:, ::-1]
image_flip_from_top_to_bottom = image[::-1, :]

Image.fromarray(image_flip_from_left_to_right).save("img/cat_flip_from_left_to_right.jpg")
Image.fromarray(image_flip_from_top_to_bottom).save("img/cat_flip_from_top_to_bottom.jpg")



grayscale_image = (0.29 * image[:, :, 0] + 0.59 * image[:, :, 1] + 0.11 * image[:, :, 2]).astype(np.uint8)

print("grayscale image shape:", grayscale_image.shape)
Image.fromarray(grayscale_image).save("img/cat_grayscale.jpg")
