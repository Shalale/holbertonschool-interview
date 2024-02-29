#!/usr/bin/python3
'''
Lockboxes algorithm solution
'''


def open_box(box_index, boxes, opened_boxes):
    for i in boxes[box_index]:
        if i >= len(boxes):
            continue
        if not isinstance(i, int):
            print("I am in")
            continue
        if i not in opened_boxes:
            opened_boxes.add(i)
            open_box(i, boxes, opened_boxes)


def canUnlockAll(boxes):
    opened_boxes = {0}
    open_box(0, boxes, opened_boxes)
    can_unlock_all = len(boxes) == len(opened_boxes)
    return can_unlock_all
