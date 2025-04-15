import cv2
import os
import numpy as np

def crop_image_to_tiles(input_path, output_dir, tile_width, tile_height, overlap=0):
    """
    将单张图像裁剪为多个指定大小的小图
    
    参数:
        input_path: 输入图像路径
        output_dir: 输出目录
        tile_width: 小图宽度
        tile_height: 小图高度
        overlap: 小图之间的重叠像素(默认为0)
    """
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)
    
    # 读取图像(保持uint8格式)
    img = cv2.imread(input_path)
    if img is None:
        raise ValueError(f"无法读取图像: {input_path}")
    
    # 获取图像尺寸
    img_height, img_width = img.shape[:2]
    
    # 计算裁剪的行列数
    x_steps = (img_width - overlap) // (tile_width - overlap)
    y_steps = (img_height - overlap) // (tile_height - overlap)
    
    # 确保不会超出图像边界
    x_steps = max(1, x_steps)
    y_steps = max(1, y_steps)
    
    tile_count = 0
    
    for y in range(y_steps):
        for x in range(x_steps):
            # 计算裁剪区域坐标
            x_start = x * (tile_width - overlap)
            y_start = y * (tile_height - overlap)
            
            # 确保不超出图像边界
            x_end = min(x_start + tile_width, img_width)
            y_end = min(y_start + tile_height, img_height)
            
            # 实际裁剪尺寸(可能边缘部分小于指定尺寸)
            actual_width = x_end - x_start
            actual_height = y_end - y_start
            
            # 裁剪图像
            tile = img[y_start:y_end, x_start:x_end]
            
            # 保存小图
            output_path = os.path.join(output_dir, f"tile_{tile_count}_x{x}_y{y}_{actual_width}x{actual_height}.jpg")
            cv2.imwrite(output_path, tile)
            
            tile_count += 1
    
    print(f"成功裁剪为 {tile_count} 张小图，保存在: {output_dir}")

if __name__ == "__main__":
    # 使用示例
    input_image = "Examples/nano_foam.jpg"  # 替换为你的输入图像路径
    output_directory = "Examples/nano_foam"  # 输出目录
    tile_w = 256  # 小图宽度
    tile_h = 256  # 小图高度
    overlap_pixels = 0  # 重叠像素数
    
    crop_image_to_tiles(input_image, output_directory, tile_w, tile_h, overlap_pixels)