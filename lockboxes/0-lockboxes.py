#!/usr/bin/python3
'''
Lockboxes algorithm solution
'''

opened_boxes = set()
opened_boxes.add(0)

def is_opened(index):
    return index in opened_boxes

def open_box(box_index): 
    for i in boxes[box_index]:
       if not i in opened_boxes:
           opened_boxes.add(i)
           open_box(i)
           
def canUnlockAll(boxes):
    open_box(0)
    canUnlockAll = len(boxes) == len(opened_boxes)
    opened_boxes.clear()
    opened_boxes.add(0)
    return canUnlockAll   
    
