import os
from PIL import Image

def check_tif_file(file_path):
    try:
        # 打开TIFF文件
        img = Image.open(file_path)
        
        # 获取文件基本信息
        print(f"文件名：{os.path.basename(file_path)}")
        print(f"文件大小：{os.path.getsize(file_path)} bytes")
        print(f"图像模式：{img.mode}")
        print(f"图像尺寸：{img.size[0]} x {img.size[1]} pixels")
        print(f"图像格式：{img.format}")
        
        # 获取TIFF标签信息
        tags = img.tag_v2
        if tags:
            print("TIFF标签信息：")
            for tag, value in tags.items():
                print(f"  {tag}: {value}")
        
        # 检查文件是否损坏
        try:
            img.verify()
            print("文件检查：正常")
        except Exception as e:
            print(f"文件检查：损坏 ({str(e)})")
        
    except Exception as e:
        print(f"打开文件失败：{str(e)}")

# 测试脚本
file_path = "Examples/nano_foam.tif"  
check_tif_file(file_path)