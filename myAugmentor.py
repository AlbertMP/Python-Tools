import Augmentor
import os

#for root, dirs, files in os.walk(".\zzy植物增广"):#root:当前目录路径 dirs:当前路径下所有子目录 files:当前路径下所有非目录子文件
#    print('root_dir:', root, type(root))  # 当前目录路径
#    print('sub_dirs:', dirs)  # 当前路径下所有子目录
paths = os.listdir('/Users/albert/Desktop/image augmentation')

# for i in range(15):
	# print('/Users/albert/Desktop/image augmentation/' + paths[i])
# 1. 指定图片所在目录
p = Augmentor.Pipeline('/Users/albert/Desktop/image augmentation/xiang_pi_shu')
#p = Augmentor.Pipeline("./zzy植物/zhu")
# 增强操作
# 旋转 概率0.7，向左最大旋转角度10，向右最大旋转角度10
p.rotate(probability=0.7, max_left_rotation=15, max_right_rotation=15)
#p.rotate90(probability=0.33)
#p.rotate270(probability=0.33)
p.random_brightness(probability=0.7, min_factor=0.7, max_factor=1.4)
#skew_tilt为上下左右方向的垂直型变，参数magnitude为型变的程度（0，1）
#p.skew_tilt(probability=1,magnitude=1)
# 指定增强后图片数目总量
p.sample(71)
