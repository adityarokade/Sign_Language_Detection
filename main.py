import os
import shutil

from Clone_git_Repo import clone_repo
# import clone_repo
from File_Operations import File_Operations
from Model_Training import Model_Training
from Data_Processing import Data_Processing


EPOCH=100
def data_operations():
    Data_Processing.Collecting_all_Data()
    Data_Processing.SeperateImagesLabels()


def main():

    clone_repo=clone_repo("https://github.com/ultralytics/yolov5.git","yolov5")
    clone_repo.cloning()

    File_Operations.File_Move('/custom_yolov5s.yaml','/yolov5/models/')


    Model_Training.model_train(EPOCH)




    
    
    
    
    
    
    
    
    
    
    
    




    
    















if __name__ == "__main__":
    data_operations()
    # main()
