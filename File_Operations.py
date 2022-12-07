import os
import shutil


class File_Operations:
    def __init__(Self):
        pass
    
    def Create_Folder(self,FolderPath):
        self.FolderPath=FolderPath

        os.makedirs(self.FolderPath)
        