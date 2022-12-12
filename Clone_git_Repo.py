import os
from git import Repo



class clone_repo:
    def __init__(self,link,directory_path):
        self.link=link
        self.directory_path=directory_path
        

    def cloning(self):

        print("okkkkk_clone_git_repo")
        os.makedirs(self.directory_path)
        Repo.clone_from(self.link, self.directory_path)
        


     
    



# a=clone_repo("https://github.com/ultralytics/yolov5.git","yolov5")
# a.Cloning()