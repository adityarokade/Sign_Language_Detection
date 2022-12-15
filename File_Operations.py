import os
import shutil


class File_Operations:
    def __init__(Self):
        pass
    
    def Create_Folder(self,FolderPath):
        self.FolderPath=FolderPath

        os.makedirs(self.FolderPath)
        
    def File_Move(self,Filepath,TargetPath):

        self.Filepath=Filepath
        self.TargetPath=TargetPath

        shutil.move(self.Filepath,self.TargetPath)
             
