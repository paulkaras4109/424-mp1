from scheduling.misc import *
from scheduling.TaskEntity import *
import numpy as np

# read the input bounding box data from file
box_info = read_json_file('../dataset/waymo_ground_truth_flat.json')
recent_boxes = []
frame_num = 1
threshold = 25

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
    for rb in recent_boxes:
        if (frame_num - rb[1] > 9):
            recent_boxes.remove(rb)

    tasklist = []
    # student's code here
    cluster_boxes_data = get_bbox_info(frame, box_info)
    for bbox in cluster_boxes_data:
        simFound = False
        for rb in recent_boxes:
            if (abs(bbox[0] - rb[0][0]) < threshold and 
            abs(bbox[1] - rb[0][1]) < threshold and 
            abs(bbox[2] - rb[0][2]) < threshold and 
            abs(bbox[3] - rb[0][3]) < threshold):
                rb = tuple(bbox[:4], frame_num)
                simFound = True
                break
        
        if not simFound:
            priority = int(bbox[4]/10)
            task = TaskEntity(frame.path, coord = bbox[:4], priority = priority, depth = bbox[4])
            tasklist.append(task)
            recent_boxes.append(tuple(bbox[:4], frame_num))
    
    frame_num += 1
    return tasklist
