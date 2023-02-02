#!/usr/bin/python3


def canUnlockAll(boxes):
    visited = [False] * len(boxes)
    visited[0] = True
    keys = [0]
    while keys:
        box = keys.pop()
        for key in boxes[box]:
            if key < len(boxes) and not visited[key]:
                visited[key] = True
                keys.append(key)
    return all(visited)
