In this repository, it is recommended that you use the CNN pre-trained model of the Places-365 Resnet.  
(You can also use other CNN models as you like.)  

This folder needs above files in "/CNN/CNN_Places365/" folder.  
- places365resnet/resnet152_places365.caffemodel  
- places365resnet/deploy_resnet152_places365.prototxt  
- places365resnet/places365CNN_mean.npy  

Please set the CNN model's file name and path in "CNN_place_*.py"  

The caffemodels of Places-CNN can be download as follows:  
- https://github.com/CSAILVision/places365
- https://github.com/BVLC/caffe/wiki/Model-Zoo#places-cnn-model-from-mit
- http://places.csail.mit.edu/

