import tifffile
import numpy as np
from skimage import io

# 输入和输出文件路径
input_2d_image = "Examples/nano_foam.tif"
output_3d_tif = "Examples/nano_foam_3d.tif"

# 读取2D图像
img_2d = io.imread(input_2d_image)

# 检查图像是否是灰度图
if len(img_2d.shape) > 2:
    img_2d = img_2d[:, :, 0]  # 如果是RGB，取第一个通道

# 沿着z轴重复10次创建3D图像
img_3d = np.repeat(img_2d[np.newaxis, :, :], 10, axis=0)

# 保存为3D TIFF
tifffile.imwrite(output_3d_tif, img_3d)

print(f"成功创建3D TIFF文件: {output_3d_tif}")
print(f"3D图像尺寸: {img_3d.shape} (Z,Y,X)")