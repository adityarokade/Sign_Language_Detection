# Sign_Language_Detection using YOLOv5


###  Image Labeling
```bash
pip install labelImg
```


## Steps

### STEP 01- Clone the new repository

### STEP 02- Create a conda environment after opening the repository in VSCODE

```bash
conda create --prefix ./env python=3.7 -y
```

```bash
conda activate ./env
```
OR
```bash
source activate ./env
```

### STEP 03- install the requirements
```bash
pip install -r requirements.txt
```
### STEP 04- capture images
```bash
python Capture_Images.py
```
### STEP 05- Data Preprocessing
```bash
python main.py
```
In main.py file do changes based on operation required like image lebeling

### STEP 06- Prediction 
```bash
python run.py
```

## Main Packages
```bash
pip install -r requirements.txt
```

```bash
pip install PyYAML
```

```bash
pip install opencv-python
```
```bash
pip install GitPython
```

