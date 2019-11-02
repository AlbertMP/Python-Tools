from PIL import Image
import os

image_list = os.listdir()

root = "/Users/albert/Desktop/reclassify_peng/ba_jiao"
for file in os.listdir(root):
    # if file == '.DS_Store':
    #     os.remove("/Users/albert/Desktop/reclassify_peng/gou_shu/ppbc/"+file)
    img = Image.open(root+"/"+file)
    cropped = img.crop((0, 0, img.size[0], img.size[1]-21))  # (left, upper, right, lower)切下面
    #cropped = img.crop((0, 0, img.size[0]-83, img.size[1]))  # (left, upper, right, lower)切右面
    print(root + "/" + file.split('.')[0] + "_cut." + file.split('.')[1])
    cropped.save(root + "/" + file.split('.')[0] + "_cut." + file.split('.')[1])
