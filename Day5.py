import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


# tiny = np.array ([[0, 120],
#                   [220, 255]])

# plt.imshow(tiny, cmap='Blues')
# plt.show()

img= np.array(Image.open("img/cat.jpg").convert("RGB"))

# plt.imshow(img)
# plt.show()

h, w, _ = img.shape

print("Img shaped", h, w, _)

crop = img[h // 4 : 3 * h // 4, w // 4 : 3 * w // 4]
flip = img[:, ::-1]
gray = (0.299 * img[:, :, 0] + 0.587 * img[:, :, 1] + 0.114 * img[:, :, 2]).astype(np.uint8)

# plt.imshow(crop)
# plt.show()
# plt.imshow(flip)
# plt.show()
# plt.imshow(gray, cmap='gray')
# plt.show()

fig, axes = plt.subplots(1, 4, figsize=(12, 3))

axes[0].imshow(img)
axes[0].set_title("original")

axes[1].imshow(crop)
axes[1].set_title("crop")

axes[2].imshow(flip)
axes[2].set_title("flip")

axes[3].imshow(gray, cmap="gray")
axes[3].set_title("gray")


axes[0].imshow(img)
axes[0].set_title("original")
axes[0].axis("off")


plt.savefig("img/cat_collage.png", dpi=150, bbox_inches="tight")
plt.show()