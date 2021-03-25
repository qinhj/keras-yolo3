import argparse
import xml.etree.ElementTree as ET
from os import getcwd

## construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-y", "--year", type=str, default="2007", help="year of VOC datasets")
ap.add_argument("-c", "--classes_path", type=str, help="path of classes file")
args = vars(ap.parse_args())
#print("args: %s" % args)

## VOC datasets: year
year = args["year"]
sets = [(year, 'train'), (year, 'val')]
if "2012" == year:
    pass
else:
    sets.append((year, 'test'))
print("VOC dataset year: %s, sets: %s" % (year, sets))

def get_classes(classes_path):
    '''loads the classes'''
    with open(classes_path) as f:
        class_names = f.readlines()
    class_names = [c.strip() for c in class_names]
    return class_names
## VOC datasets: classes
if "classes_path" not in args.keys() or args["classes_path"] is None:
    classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
else:
    classes = get_classes(args["classes_path"])
print("VOC dataset classes: %s" % classes)

def convert_annotation(year, image_id, list_file):
    in_file = open('VOCdevkit/VOC%s/Annotations/%s.xml' % (year, image_id))
    tree = ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

wd = getcwd()

for year, image_set in sets:
    image_ids = open('VOCdevkit/VOC%s/ImageSets/Main/%s.txt' % (year, image_set)).readlines()
    list_file = open('%s_%s.txt' % (year, image_set), 'w')
    for image_id in image_ids:
        image_id = image_id.strip().split()[0]
        list_file.write('%s/VOCdevkit/VOC%s/JPEGImages/%s.jpg' % (wd, year, image_id))
        convert_annotation(year, image_id, list_file)
        list_file.write('\n')
    list_file.close()

