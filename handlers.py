def get_projects_directory():
  name_of_project_folder = str(input('Por favor, informe o nome da pasta do seu projeto?: ' \
  '\n >projects ' \
  '\n >courses ' \
  '\nYour Answer: '))

  if name_of_project_folder == 'projects':
    return name_of_project_folder
  elif name_of_project_folder == 'courses':
    return name_of_project_folder
  else:
    print('Algo deu errado. Por favor, verifique se o valor insirido é válido.')
    return get_projects_directory()