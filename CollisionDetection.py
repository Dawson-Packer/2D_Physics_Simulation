import math as math
from objects.objects import *

# TODO: Clean up code!!!

def handle_collisions(objects: list):
    """
    @brief    Handles the collision logic and executes collision functions on colliding objects.
    @param objects    The list of objects to check for collisions on.
    """
    calculate_ssp(objects, 1)

def calculate_ssp(objects: list, recursive_id: int):
    """
    @brief    Uses the Smart Space Partition algorithm twice for segmenting the locations of
              the colliding objects, and checks for collisions. Reduces the total number of
              calculations necessary for collision detection.
    @param objects    The list of objects to check for collisions on.
    @param recursive_id    The n-th time the function has been run within the first call.
    """
    objects_flattened_x = sorted(objects, key=lambda x: x.x_pos)

    # First split
    split_idx = len(objects_flattened_x) // 2
    if math.sqrt((objects_flattened_x[split_idx].x_pos -\
                   objects_flattened_x[split_idx-1].x_pos)**2 +\
                      (objects_flattened_x[split_idx].y_pos -\
                        objects_flattened_x[split_idx-1].y_pos)**2) <=\
                              objects_flattened_x[split_idx-1].radius +\
                                  objects_flattened_x[split_idx].radius + 1:
        print("collision!", objects_flattened_x[split_idx-1].name,\
               objects_flattened_x[split_idx].name) # FIXME Will not be in final implementation
        objects_flattened_x[split_idx-1].stop() # FIXME Will not be in final implementation
        objects_flattened_x[split_idx].stop() # FIXME Will not be in final implementation
    objects_flattened_x = [objects_flattened_x[0:split_idx], objects_flattened_x[split_idx:]]
    

    for split in objects_flattened_x:
        if len(split) > 2:
            objects_flattened_y = sorted(split, key=lambda x: x.y_pos)
            # Second split
            split_idx = len(objects_flattened_y) // 2
            if math.sqrt((objects_flattened_y[split_idx].x_pos -\
                           objects_flattened_y[split_idx-1].x_pos)**2 +\
                              (objects_flattened_y[split_idx].y_pos -\
                                objects_flattened_y[split_idx-1].y_pos)**2) <=\
                                      objects_flattened_y[split_idx-1].radius +\
                                          objects_flattened_y[split_idx].radius + 1:
                print("collision!", objects_flattened_y[split_idx-1].name,\
                       objects_flattened_y[split_idx].name) # FIXME Will not be in final implementation
                objects_flattened_y[split_idx-1].stop() # FIXME Will not be in final implementation
                objects_flattened_y[split_idx].stop() # FIXME Will not be in final implementation
            objects_flattened_y = [objects_flattened_y[0:split_idx], 
                                    objects_flattened_y[split_idx:]]
            for split in objects_flattened_y:
                if len(split) > 1:
                    calculate_ssp(split, recursive_id + 1)
                    # for index, object in enumerate(split[:-1]):
                    #     if math.sqrt((split[index+1].x_pos - object.x_pos)**2 +\
                    #                   (split[index+1].y_pos - object.y_pos)**2) <= object.radius\
                    #                       + split[index+1].radius + 1:
                    #         print("collision!", split[0].name, split[1].name) # FIXME Will not be in final implementation
                    #         split[0].stop() # FIXME Will not be in final implementation
                    #         split[1].stop() # FIXME Will not be in final implementation
        elif len(split) == 2:
            if math.sqrt((split[1].x_pos - split[0].x_pos)**2 + \
                         (split[1].y_pos - split[0].y_pos)**2) <=\
                              split[0].radius + split[1].radius + 1:
                print("collision!", split[0].name, split[1].name) # FIXME Will not be in final implementation
                split[0].stop() # FIXME Will not be in final implementation
                split[1].stop() # FIXME Will not be in final implementation