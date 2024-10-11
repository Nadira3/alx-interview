#!/usr/bin/python3
"""
Description:
    This module contains functions that demonstrate
    graph theory
"""


def checkBoxes(boxes, idx, visited):
    """
    Parameters:
        boxes: the list containing the locked boxes
        idx: the index of visited boxes
        visited: a set containing idx of visited boxes

    Return:
        None
    """
    if idx in visited:
        return
    visited.add(idx)
    for key in boxes[idx]:
        checkBoxes(boxes, key, visited)


def canUnlockAll(boxes):
    """
    Parameters:
        boxes: the list containing the locked boxes

    Return:
        bool:   True if all boxes were unlocked
                False otherwise
    """
    visited = set()
    if boxes:
        checkBoxes(boxes, 0, visited)

    return len(visited) == len(boxes)
