import os
from File_Operations import File_Operations
from read_yaml import Read_Yaml
import glob





class Data_Processing:
    def __init__(Self):
        self.File_Operations= File_Operations()
        self.config=Read_Yaml.read_yaml("CaptureConfig.yaml")
        self.AllImagesPath=self.config['ALL_IMAGES_PATH']
        self.ImageFolderPath=self.config['IMAGE_FOLDER_PATH']
        self.DataPath=self.config.['DATA_PATH']
        pass
    
    def Collecting_all_Data(self):
        self.File_Operations.Create_Folder(self.ALL_IMAGES_PATH)
        folder_list=[i for i in os.listdir(self.ImageFolderPath)]

        for folder in folder_list:
        file_list= [i for i in os.listdir(f"{self.ImageFolderPath}/{folder}")]
        for file in file_list:
            file_path=os.path.join(f'{self.ImageFolderPath}/{folder}',f'{file}')
            shutil.copy(file_path,self.AllImagesPath)
            


    def SeperateImagesLabels(Self):
        if os.path.isfile(f'{self.AllImagesPath}/classes.txt'):

            os.remove(f'{self.AllImagesPath}/classes.txt')

        images=glob.glob(f'{self.AllImagesPath}/*.jpg')
        labels=glob.glob(f'{self.AllImagesPath}/*.txt')  

        
        self.File_Operations.Create_Folder(f'{self.DataPath}/train/images')
        self.File_Operations.Create_Folder(f'{self.DataPath}/test/labels')
        


        for i in Txtfiles:
            shutil.copy(i,f'{self.DataPath}/test/labels') 

        for i in images:
            shutil.copy(i,f'{self.DataPath}/train/images')
