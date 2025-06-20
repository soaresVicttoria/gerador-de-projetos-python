import subprocess

def update_linux():
  return subprocess.run(f'''sudo apt update -y && sudo apt-get upgrade -y''', shell=True, check=True, executable='/bin/bash')

def install_pip():
  return subprocess.run(f'''sudo apt install python3-pip''', shell=True, check=True, executable='/bin/bash')

def install_venv():
  subprocess.run(f'''sudo apt install python3-venv''', shell=True, check=True, executable='/bin/bash')
  subprocess.run(f'''python3 -m venv .venv''', shell=True, check=True, executable='/bin/bash')

def activate_venv():
  subprocess.run(f'''source .venv/bin/activate''', shell=True, check=True, executable='/bin/bash')

def open_project(path_full_novo_projeto):
  subprocess.run(f'''code {path_full_novo_projeto}''', shell=True, check=True, executable='/bin/bash')