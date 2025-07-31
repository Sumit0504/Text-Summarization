import os
from pathlib import Path
import logging # used to log info while runtime

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "Text_Summarizer"

# File and folder structre
list_of_file = [
    ".github/workflows/.gitkeep", # it will used when we do deployement
    f"src/{project_name}/__int__.py", # For the installation of local package we use the constructor
    f"src/{project_name}/components/__int__.py", 
    f"src/{project_name}/utils/__int__.py", 
    f"src/{project_name}/utils/common.py", 
    f"src/{project_name}/logging/__int__.py", 
    f"src/{project_name}/config/__int__.py", 
    f"src/{project_name}/config/configuration.py", 
    f"src/{project_name}/pipeline/__int__.py", 
    f"src/{project_name}/entity/__int__.py", 
    f"src/{project_name}/constants/__int__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
]

for file_path in list_of_file:
    file_path = Path(file_path)
    
    #Split file and folder so that we can first create folder then file
    file_dir, file_name = os.path.split(file_path)
    
    # Handling if file_dir is empty 
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True) # exist_ok says if already exists it will not create it again
        logging.info(f"Creating Directory {file_dir} for the file {file_name}")
        
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path, 'w') as f:
            pass
            logging.info(f"Creating the empty file {file_name}")
            
    else:
        logging.info(f"{file_name} Already exists")