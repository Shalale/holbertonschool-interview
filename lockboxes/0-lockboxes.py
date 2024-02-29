#!/usr/bin/python3
'''
Lockboxes algorithm solution
'''

opened_boxes = set()
opened_boxes.add(0)

def open_box(box_index, boxes): 
    for i in boxes[box_index]:
        if i >= len(boxes) and not i.isdigit():
            continue
        if not i in opened_boxes:
               opened_boxes.add(i)
               open_box(i, boxes)
           
def canUnlockAll(boxes):
    open_box(0, boxes)
    canUnlockAll = len(boxes) == len(opened_boxes)
    opened_boxes.clear()
    opened_boxes.add(0)
    return canUnlockAll   
    
