from PIL import Image
import numpy as np


img = Image.open('img/cat.jpg').convert("RGB")
arr = np.array(img)



print("Image shape:", arr.shape)
print("Image data type:", arr.dtype)
print("min/max pixel values:", arr.min(), arr.max())
print("top-left pixel value:", arr[0,0])
print("center pixel (R,G,B):", arr[arr.shape[0] // 2, arr.shape[1] // 2])




print(arr[:100, :100].shape) 
print(arr[:, :, 0].shape) 
print(arr[:, :, 0].mean()) 