# Keras Yolo3 Guide #
Author: qinhongjie@imilab.com  

## Tree ##
```
.
├── darknet53.cfg   // config file for darknet53
├── font
├── LICENSE
├── model_data
├── README.md
├── scripts
├── train_bottleneck.py
├── train.py
├── yolo3
├── Yolo3.md        // what u're reading
├── yolo.py
├── yolov3.cfg
├── yolov3-tiny.cfg
└── yolo_video.py
```

## Note ##
```
1. *.cfg
This file is only used to convert origin model to keras model.
The items in "yolo" section are useless.

2. model_data/*_classes.txt
These files are used to train/test keras yolo3 models.
One needs to update it before training or testing.

3. model_data/*_anchors.txt
These files are also used to train/test keras yolo3 models.
One needs to generate it with scripts/kmeans.py .
```
