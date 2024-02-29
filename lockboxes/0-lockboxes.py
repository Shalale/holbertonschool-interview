#!/usr/bin/python3
'''
Lockboxes algorithm solution
'''

opened_boxes = set()

def open_box(box_index, boxes): 
    for i in boxes[box_index]:
        if i >= len(boxes):
            break
        if not i in opened_boxes:
               opened_boxes.add(i)
               open_box(i, boxes)
           
def canUnlockAll(boxes):
    open_box(0, boxes)
    canUnlockAll = len(boxes) == len(opened_boxes)
    opened_boxes.clear()
    opened_boxes.add(0)
    return canUnlockAll   
    
