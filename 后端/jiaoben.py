from PIL import Image

import numpy as np

image_pil = Image.open("/home/hadoop/图片/4c6.png")

image_np = np.array(image_pil)

print(image_np.shape)