from scheduling.misc import *
from scheduling.TaskEntity import *
import numpy as np

# read the input bounding box data from file
box_info = read_json_file('../dataset/waymo_ground_truth_flat.json')
recent_boxes = []
frame_num = 1

def process_frame(frame):
    """Process frame for scheduling.

    Process a image frame to obtain cluster boxes and corresponding scheduling parameters
    for scheduling. 

    Student's code here.

    Args:
        param1: The image frame to be processed. 

    Returns:
        A list of tasks with each task containing image_path and other necessary information. 
    """
    global frame_num
    global recent_boxes
    if (frame_num % 10 == 0):
        recent_boxes = []

    tasklist = []
    # student's code here
    cluster_boxes_data = get_bbox_info(frame, box_info)
    for bbox in cluster_boxes_data:
        simFound = False
        for rb in recent_boxes:
            if (rb[0] > 0 and rb[1] > 0 and rb[2] > 0 and rb[3] > 0 and 
            abs((bbox[:4][0] - rb[0]) / rb[0]) < 0.05 and 
            abs((bbox[:4][1] - rb[1]) / rb[1]) < 0.05 and 
            abs((bbox[:4][2] - rb[2]) / rb[2]) < 0.05 and 
            abs((bbox[:4][3] - rb[3]) / rb[3]) < 0.05):
                rb = bbox[:4]
                simFound = True
                break
        
        if not simFound:
            priority = int(bbox[4]/10)
            task = TaskEntity(frame.path, coord = bbox[:4], priority = priority, depth = bbox[4])
            tasklist.append(task)
            recent_boxes.append(bbox[:4])
    
    frame_num += 1
    return tasklist


    
