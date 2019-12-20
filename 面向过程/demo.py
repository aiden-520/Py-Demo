import xml.etree.ElementTree as ET
import os, cv2
from tqdm import tqdm

annota_dir = 'C:\\Users\\Administrator\\Desktop\\1_stage_template\\Annotations'
origin_dir = 'C:\\Users\\Administrator\\Desktop\\1_stage_template\\IMG'
target_dir1 = 'C:\\Users\\Administrator\\Desktop\\1_stage_template\\cut'


def divide_img(oriname):
    img_file = os.path.join(origin_dir, oriname + '.jpg')
    im = cv2.imread(img_file)

    # 读取每个原图像的xml文件
    xml_file = os.path.join(annota_dir, oriname + '.xml')
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for object in root.findall('object'):

        object_name = object.find('name').text
        Xmin = int(object.find('bndbox').find('xmin').text)
        Ymin = int(object.find('bndbox').find('ymin').text)
        Xmax = int(object.find('bndbox').find('xmax').text)
        Ymax = int(object.find('bndbox').find('ymax').text)
        color = (10, 250, 7)

        cropped = im[Ymin:Ymax,Xmin:Xmax]
        cv2.imshow('im', im)

    img_name = oriname + '.jpg'
    to_name = os.path.join(target_dir1, img_name)
    cv2.imwrite(to_name, cropped)


img_list = os.listdir(origin_dir)
for name in img_list:
    divide_img(name.rstrip('.jpg'))
