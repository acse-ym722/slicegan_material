import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
image = cv2.imread('Examples/nano-foam.jpg', cv2.IMREAD_GRAYSCALE)  # 以灰度模式读取

# 应用简单阈值分割 (使用127作为阈值，可以根据需要调整)
# thresh=127: 阈值值
# maxval=255: 超过阈值的像素将被设为此值
# cv2.THRESH_BINARY: 二值化类型 - 大于阈值为maxval，小于阈值为0
_, binary_image = cv2.threshold(image, 80, 255, cv2.THRESH_BINARY)

# 显示原图和分割后的图像
plt.figure(figsize=(10, 5))
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('原始图像')
plt.subplot(122), plt.imshow(binary_image, cmap='gray'), plt.title('阈值分割后图像')
plt.tight_layout()
plt.show()

# 保存结果
cv2.imwrite('Examples/nano-foam-binary.jpg', binary_image)