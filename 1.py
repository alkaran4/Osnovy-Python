import os

dir_main = 'my_project'
dir_list = ('settings', 'mainapp', 'adminapp', 'authap')


if not os.path.exists(dir_main):
    os.mkdir(dir_main)

for d in dir_list:
    os.mkdir(os.path.join(dir_main, d))
