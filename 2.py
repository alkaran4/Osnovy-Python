import os

dir_main = 'my_project'
dir_list = ('settings', 'mainapp', 'authapp')
list_settings = ['__init__.py', 'dev.py', 'prod.py']
list_mainapp = ['__init__.py', 'models.py', 'views.py']
list_2nd_mainapp = ['base.html', 'index.html']
templates = 'templates'

def make_dirs(arg):
    if arg == 0:
        os.makedirs(os.path.join(f'{dir_main}/{dir_list[arg]}'))
        for r in range(len(list_settings)):
            with open(f'{dir_main}/{dir_list[arg]}/{list_settings[r]}', "a") as f:
                f.write('')
    elif arg == 1 or arg == 2:
        os.makedirs(os.path.join(f'{dir_main}/{dir_list[arg]}/{templates}/{dir_list[arg]}'))
        for r in range(len(list_mainapp)):
            with open(f'{dir_main}/{dir_list[arg]}/{list_settings[r]}', "a") as f:
                f.write('')
        for r in range(len(list_2nd_mainapp)):
            with open(f'{dir_main}/{dir_list[arg]}/{templates}/{dir_list[arg]}/{list_2nd_mainapp[r]}', "a") as f:
                f.write('')

make_dirs(0)
make_dirs(1)
make_dirs(2)




