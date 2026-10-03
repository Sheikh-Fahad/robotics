import numpy as np


list = np.array([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]])

print("list shape:", list)



print(list[0, 2])
print(list[-1, -1])
print(list[1])
print(list[:, 1])
print(list[list > 5])


#Broadcasting


B_list = np.array([[1, 2, 3],
                 [4, 5, 6]])


print(B_list + 10)
print(B_list + np.array([[10, 20, 30]]))
print(B_list + np.array([[100], [200]]))



#Image e broadcasting

from PIL import Image
image=np.array(Image.open("img/cat.jpg").convert("RGB"))


arr= np.array([1.0, 0.5, 0.5])
tint=image * arr

out = np.clip(tint, 0, 255).astype(np.uint8)
Image.fromarray(out).save("img/cat_tint.jpg")
