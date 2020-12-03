#!/usr/bin/env python
# coding: utf-8
# %%
# This file was used to parse the XML files and image files to create numpy arraysfor Object Detection

# %%
i=3
os.rename("../data/images/train_images/00000" + "0"*(3-len(str(i)))+str(i)+" (Custom).jpg", "../data/images/train_images/00000" + "0"*(3-len(str(i)))+str(i)+".jpg")

# %%
import os
for i in range(1, 980):
    try:
        os.rename("../data/images/train_images/00000" + "0"*(3-len(str(i)))+str(i)+" (Custom).png", "../data/images/train_images/00000" + "0"*(3-len(str(i)))+str(i)+".png")
    except:
        pass

# %%
import numpy as np
import numpy

"""
Rectangle class that allows for easier use/access to the four coordinates of a bounding box
"""
class rectangle:
    def __init__(self, xmin, ymin, xmax, ymax):
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax
    
    def __repr__(self):
        return str([self.xmin, self.ymin, self.xmax, self.ymax])
    
    
    def toArray(self):
        return np.array([self.xmin, self.ymin, self.xmax, self.ymax])


# %%
import xml.etree.ElementTree as ET


# %%

boxes = []
colors = []
images = []
for i in range(1000):
    tmp_box = []
    tmp_color = []
    try:
        tree = ET.parse('../data/images/train_labels/00000'+"0"*(3-len(str(i)))+str(i)+'.xml')
        root = tree.getroot()
        for child in root:
            if child.tag == 'object' :
                for subchild in child:
                    if subchild.tag == 'name':
                        if subchild.text == 'green':
                            tmp_color.append(0)
                        elif subchild.text == 'red':
                            tmp_color.append(1)
                        else:
                            print("something is wrong with "+str(i))
                for subchild in child:
                    if subchild.tag == 'bndbox':
                        for subsubchild in subchild:
                            if subsubchild.tag == 'xmin':
                                xmin = int(subsubchild.text)
                            elif subsubchild.tag == 'ymin':
                                ymin = int(subsubchild.text)
                            elif subsubchild.tag == 'xmax':
                                xmax = int(subsubchild.text)
                            elif subsubchild.tag == 'ymax':
                                ymax = int(subsubchild.text)
                        tmp_box.append(rectangle(xmin, ymin, xmax, ymax).toArray())
    except:
        boxes.append([])
        colors.append([])
        continue

    boxes.append(tmp_box)
    colors.append(tmp_color)
        
print(boxes)
print(colors)


# %%


"""
Removes non-array elements from all 3 data lists
"""
def remove_same(a, b, c):
    assert len(a) == len(b) and len(b) == len(c)
    for i in range(len(a)):
        try:
            if type(a[i]) != numpy.ndarray:
                a.pop(i)
                b.pop(i)
                c.pop(i)
                remove_same(a,b,c)
        except:
            pass


# %%


"""
Reads the .jpg image files and appends their data to the 'images' list
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
images = []
for i in range(10):
    x = 'images_new_resized/green_new/0000000'+str(i)+".jpg"
    try:
        plt.imshow(cv2.imread(x));
        assert cv2.imread(x).shape == (300,300,3)
        images.append(cv2.imread(x))
    except:
        images.append([])
for i in range(10,100):
    x = 'images_new_resized/green_new/000000'+str(i)+".jpg"
    try:
        plt.imshow(cv2.imread(x)); 
        assert cv2.imread(x).shape == (300,300,3)
        images.append(cv2.imread(x))
    except:
         images.append([])
for i in range(100,480):
    x = 'images_new_resized/green_new/00000'+str(i)+".jpg"
    try:
        plt.imshow(cv2.imread(x)); 
        assert cv2.imread(x).shape == (300,300,3)
        images.append(cv2.imread(x))
    except:
         images.append([])


for i in range(10):
    x = 'images_new_resized/red_new/0000000'+str(i)+".jpg"
    try:
        plt.imshow(cv2.imread(x));
        assert cv2.imread(x).shape == (300,300,3)
        images.append(cv2.imread(x))
    except:
        images.append([])
for i in range(10,100):
    x = 'images_new_resized/red_new/000000'+str(i)+".jpg"
    try:
        plt.imshow(cv2.imread(x)); 
        assert cv2.imread(x).shape == (300,300,3)
        images.append(cv2.imread(x))
    except:
         images.append([])
for i in range(100,500):
    x = 'images_new_resized/red_new/00000'+str(i)+".jpg"
    try:
        plt.imshow(cv2.imread(x)); 
        assert cv2.imread(x).shape == (300,300,3)
        images.append(cv2.imread(x))
    except:
         images.append([])

images = np.array(images)


# %%


len(images)


# %%


print(len(images), len(boxes), len(colors))


# %%


images = list(images)
boxes = list(boxes)
colors = list(colors)
remove_same(images, boxes, colors)


# %%


print(len(images), len(boxes), len(colors))


# %%


"""
Converts images from BGR format to RGB format
"""
def bgr_to_rgb(img):
    return img[:, :, ::-1]


# %%


images = np.array(images)
boxes = np.array(boxes)
colors = np.array(colors)

