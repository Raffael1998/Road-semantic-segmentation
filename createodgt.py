import os
from PIL import Image

#path to reference image folder and annotation folder (also called label or colormap)
image_dir = r"C:\Users\grosr\OneDrive - Queensland University of Technology\Desktop\Raffael\CARRS-Q internship\Databases\bdd100k_sem_seg_labels_trainval\train _ Images references BDD"
annotation_dir = r"C:\Users\grosr\OneDrive - Queensland University of Technology\Desktop\Raffael\CARRS-Q internship\Other Projects\LabelsToB&W\annotations\training"

#create odgt file for a dataset
def create_training_odgt(image_dir, annotation_dir):
  
    #the path that will be used during training. I recommand making a directory for reference images and a directory for annotations as below
    path_of_stored_images = "ADEChallengeData2016/images/training/"
    path_of_stored_annotations = "ADEChallengeData2016/annotations/training/"
  
    image_list = list(os.listdir(image_dir))
    annotation_list = list(os.listdir(annotation_dir))
    image_list.sort()
    annotation_list.sort()
    image_path = []
    annotation_path = []
    for i in range(len(image_list)):
        image_path.append(os.path.join(image_dir, image_list[i]))
    for i in range(len(annotation_list)):
        annotation_path.append(os.path.join(annotation_dir, annotation_list[i]))
    
    im = Image.open(annotation_path[0])
    width, height = im.size
    
    with open('training.odgt', 'w') as f:
        s = ''
        for i in range(len(image_list)):
            s += '{"fpath_img": "' + path_of_stored_images + image_list[i] + '", "fpath_segm": "' + path_of_stored_annotations + annotation_list[i] + '", "width": ' + str(width) + ', "height": ' + str(height) + '}\n'

        f.write(s)
        
create_training_odgt(image_dir, annotation_dir)
