#cherche sur l'ordinateur des fichiers avec l'extension spécifié et copie les fichiers dans un nouveau dossier
import os
import sys
import shutil

path = input("Enter the path: ")
nouveau_path = input("Enter the new path for the copy: ")
extension = input("Enter the extension: ")

def copy(path, nouveau_path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith("."+extension):
                print(os.path.join(root, file))
                shutil.copy(os.path.join(root, file), nouveau_path)


copy(path, nouveau_path)


