import os
import cv2
import time
import uuid
import yaml


def read_yaml(path_to_yaml: str):
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
    return content




class CaptureImage:
    def __init__(self):
        self.config=read_yaml("CaptureConfig.yaml")
        self.ImagePath=self.config['IMAGE_PATH']
        self.Labels=self.config['LABELS']
        self.NumberOfImages=self.config['NUMBER_OF_IMAGES']
        self.CameraIdx=self.config['CAMERA_INDEX']

    def capture_image(self,label):
        self.label=label

        try:

            cap=cv2.VideoCapture(self.CameraIdx)
            print("collecting Iamges For {}".format(self.label))
            time.sleep(5)
            for imgnum in range(self.NumberOfImages):
                ret,frame=cap.read()
                imagename=os.path.join(self.ImagePath,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
                cv2.imwrite(imagename,frame)
                cv2.imshow('frame',frame)
                time.sleep(2)

                if cv2.waitkey(1)& oxFF == ord('q'):
                    break
            cap.release()
        except:
            print("Error is ocured in capturing images using opencv")



    def create_folder_image(self):

        for label in self.Labels:
            img_path=os.path.join(self.ImagePath , label)
            os.makedirs(img_path)
            self.capture_image(self.label)


    





    
    
