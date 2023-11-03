import numpy as np
from objects.objects import *

def idx_median(lst):
    if len(lst) % 2 == 1:
        return np.where(lst == np.median(lst))[0][0]
    else:
        length, remainder = len(lst) // 2 - 1, len(lst) // 2
        left = np.partition(lst, length)[length]
        right = np.partition(lst, remainder)[remainder]
        return [np.where(lst == left)[0][0], np.where(lst == right)[0][0]]

def handle_collisions(objects: list):
    objects_flattened_x = sorted(objects, key=lambda x: x.x_pos)
    objects_x_coords = [object.x_pos for object in objects_flattened_x]

    # First split
    split_idx = idx_median(objects_x_coords)
    if type(split_idx) is list:
        split_idx = split_idx[1]
    objects_flattened_x = [objects_flattened_x[0:split_idx], objects_flattened_x[split_idx+1:]]

    for split in objects_flattened_x:
        if len(split) > 0:
            objects_flattened_y = sorted(split, key=lambda x: x.y_pos)
            objects_y_coords = [object.y_pos for object in objects_flattened_y]

            # Second split
            split_idx = idx_median(objects_y_coords)
            if type(split_idx) is list:
                split_idx = split_idx[1]
            objects_flattened_y = [objects_flattened_y[0:split_idx], 
                                   objects_flattened_y[split_idx+1:]]
            
def calculate_bvh(objects: list):
    pass

    