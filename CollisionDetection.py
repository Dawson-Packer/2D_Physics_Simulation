from objects.objects import *

def median(lst):
    return len(lst) // 2

def handle_collisions(objects: list):
    pass

def calculate_ssp(objects: list):
    objects_flattened_x = sorted(objects, key=lambda x: x.x_pos)
    objects_x_coords = [object.x_pos for object in objects_flattened_x]

    # First split
    split_idx = median(objects_x_coords)
    objects_flattened_x = [objects_flattened_x[0:split_idx], objects_flattened_x[split_idx+1:]]

    for split in objects_flattened_x:
        if len(split) > 0:
            objects_flattened_y = sorted(split, key=lambda x: x.y_pos)
            objects_y_coords = [object.y_pos for object in objects_flattened_y]

            # Second split
            split_idx = median(objects_y_coords)
            objects_flattened_y = [objects_flattened_y[0:split_idx], 
                                    objects_flattened_y[split_idx:]]

    