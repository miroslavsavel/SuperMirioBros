import os
import pygame

def import_folder(path):
    surface_list = []
    """this logic will import everything so make sure you only have images in the folder"""
    for _,__, img_files in os.walk(path):
        # we get back list of strings
        for image in img_files:
            full_path = path + '/' + image
            image_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surface)

    return surface_list

