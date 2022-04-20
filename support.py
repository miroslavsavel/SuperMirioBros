import os

def import_folder(path):

    for information in os.walk(path):
        print(information)
        #print('walkiiee')

import_folder('./graphics/character/run')