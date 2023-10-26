import os
import shutil


def delete_folder_contents(folder_path):
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        if os.path.isfile(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)


delete_folder_contents('output')
delete_folder_contents('Screenshots')
delete_folder_contents('Voiceovers')
