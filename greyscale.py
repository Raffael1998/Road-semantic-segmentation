import os
import shutil
from pathlib import Path
from PIL import Image, ImageOps
import numpy as np

#path to colormap images folder
annotation_dir = r'C:\Users\grosr\OneDrive - Queensland University of Technology\Desktop\Raffael\CARRS-Q internship\Databases\bdd100k_sem_seg_labels_trainval\val2 _ Images colormap BDD'
annotation_list = list(os.listdir(annotation_dir))
annotation_list.sort()
annotation_path = []
for i in range(len(annotation_list)):
    annotation_path.append(os.path.join(annotation_dir, annotation_list[i]))
    
#path to destination directory
dst_dir = r"C:\Users\grosr\OneDrive - Queensland University of Technology\Desktop\Raffael\CARRS-Q internship\Other Projects\CitycapeToB&W\annotations\training"

    
color_list = []

for i in range(len(annotation_path)):
    annotation = Image.open(annotation_path[i])
    pix = annotation.load()
    annotationGREY = Image.new(mode="L", size=(annotation.size[0], annotation.size[1]))
    pix_grey = annotationGREY.load()
    for i in range(annotation.size[0]):  # for every pixel:
        for j in range(annotation.size[1]):
            if pix[i, j] not in color_list:
                color_list.append(pix[i, j])
            pix_grey[i, j] = color_list.index(pix[i, j])
            
    dst_file = os.path.join(dst_dir, annotation_list[i])
    annotationGREY.save(dst_file)
