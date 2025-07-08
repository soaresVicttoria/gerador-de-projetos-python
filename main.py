from manage_directory import get_home_directory, create_directory_if_not_exists, change_directory, create_file_if_not_exists
from handlers import get_projects_directory
from bash_commands import update_linux, install_pip, install_venv, activate_venv, open_project

home_directory: str = get_home_directory()
projects_directory: str = get_projects_directory()
default_projects_directory: str = f'{home_directory}/{projects_directory}'

create_directory_if_not_exists(default_projects_directory)

project_name: str = input('Agora, informe o nome do projeto a ser criado: ')
full_project_path: str = f'{default_projects_directory}/{project_name}'

create_directory_if_not_exists(full_project_path)
change_directory(full_project_path)
create_file_if_not_exists(full_project_path, 'main.py')
create_file_if_not_exists(full_project_path, 'requirements.txt')

print(f'{full_project_path}/main.py')

update_linux()
install_pip()
install_venv()
activate_venv()
open_project(full_project_path)