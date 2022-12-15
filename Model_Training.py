import os
import time
import torch

import yolov5/train.py





class Model_Training:
    def__init__(Self):
        pass
                
    def model_train(self,epochs):
        self.EPOCH=epochs

        os.system("python /yolov5/train.py --img 416 --batch 16 --epochs 1 --data '/Data/data.yaml' --cfg /yolov5/models/custom_yolov5s.yaml --weights 'yolov5s.pt' --name yolov5s_results  --cache")

        # python /yolov5/train.py --img 416 --batch 16 --epochs 1 --data '/Data/data.yaml' --cfg /yolov5/models/custom_yolov5s.yaml --weights 'yolov5s.pt' --name yolov5s_results  --cache
        # python /yolov5/train.py --img 416 --batch 16 --epochs self.EPOCH --data '/Data/data.yaml' --cfg /yolov5/models/custom_yolov5s.yaml --weights 'yolov5s.pt' --name yolov5s_results  --cache








# !python /content/drive/MyDrive/Ineuron/CV/16_April/yolov5/train.py --img 416 --batch 16 --epochs 100 --data '/content/drive/MyDrive/Ineuron/CV/16_April/Data/data.yaml' --cfg /content/drive/MyDrive/Ineuron/CV/16_April/yolov5/models/custom_yolov5s.yaml --weights 'yolov5s.pt' --name yolov5s_results  --cache
