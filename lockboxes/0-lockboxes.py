#!/usr/bin/python3
'''
Lockboxes algorithm solution
'''
boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
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
    return len(boxes) == len(opened_boxes)   
