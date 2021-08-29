#""1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок :
#|--my_project
    #|--settings
    #|--mainapp
    #|--adminapp
    #|--authapp""

import os
main_dir = 'my_project'
midFolders = ['settings', 'meinapp', 'adminapp', 'authapp']
for midFolder in midFolders:
        os.makedirs(os.path.join(main_dir, midFolder ))

