#!/usr/bin/python3
"""
Solution to unlockboxes
"""


def canUnlockAll(boxes):
    """
    Check whether a series of locked boxes can be opened
    based on keys.
    Solution to unlockboxes
    """
    len = len(boxes)
    keys = set()
    opened_boxes = []
    i = 0

    while i < len:
        oldix = i
        opened_boxes.append(i)
        keys.update(boxes[i])
        for k in keys:
            if k != 0 and k < len and k not in opened_boxes:
                i = k
                break
        if oldix != i:
            continue
        else:
            break

    for i in range(len):
        if i not in opened_boxes and i != 0:
            return False
    return True
