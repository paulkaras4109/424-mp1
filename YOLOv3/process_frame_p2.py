from scheduling.misc import *
from scheduling.TaskEntity import *


# read the input bounding box data from file
box_info = read_json_file('../dataset/waymo_ground_truth_flat.json')


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

    tasklist = []
    #cluster_boxes_data = get_bbox_info(frame, box_info)
    # student's code here
    #box_info = read_json_file(frame.path)
    cluster_boxes_data = get_bbox_info(frame, box_info)
    for bbox in cluster_boxes_data:
        bbox_width = bbox[2] - bbox[0]
        bbox_height = bbox[3] - bbox[1]
        priority = bbox_height * bbox_width
        task = TaskEntity(frame.path, coord = bbox[:4], priority = priority, depth = bbox[4])
        tasklist.append(task)
    

    return tasklist


    
