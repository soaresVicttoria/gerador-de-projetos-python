from pathlib import Path
import os

def get_home_directory() -> Path:
  return Path.home()

def change_directory(dir_path: str):
  os.chdir(dir_path)

def make_directory(dir_path: str):
  os.mkdir(dir_path)

def create_directory_if_not_exists(dir_path: str):
  if not os.path.exists(dir_path):
    make_directory(dir_path)
  
def create_file_if_not_exists(dir_path: str, file_name: str):
  if not os.path.isfile(f'{dir_path}/{file_name}'):
    os.mknod(file_name)
    