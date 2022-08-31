# <img src="assets/CARRSQ_LOGO.jfif" width=30> Road semantic segmentation
This Git teaches you how to train the CSAIL vision model with the dataset you want (see https://github.com/CSAILVision/semantic-segmentation-pytorch). The CSAIL git offers a model based on a 150 classes dataset = interior and outdoor / urban landscapes. If you want to train a more specific segmentation model with less classes :

The steps :
- import the CSAIL git
- decide on a number of classes and find (or create) a dataset that  fits your needs (colormap images and reference images). The size of the images doesn't matter but I recommand not too large images
- if not done already, you can divide your dataset to have training data and validation data
- convert the colormap images to greyscale images using greyscale.py. This will convert the colors into greyscale from 0 to n (n = total number of classes)
- create a .odgt file that contains the path of your greyscale images and reference images using createodgt.py
- go to /config folder and change the training and validation path (validation data is not needed to complete a full training), the number of classes and other hyperparameters for the training if you wish
-then follow the CSAIL vision git instruction to launch a training. For example python train.py --gpus GPUS --cfg config/ade20k-resnet50dilated-ppm_deepsup.yaml. Make sure you have 1 or several GPUs available, and that they are identified by pytorch.
