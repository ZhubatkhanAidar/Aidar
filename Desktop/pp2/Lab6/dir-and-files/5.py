import os

pathie = "C:/Users/Aidar/Desktop/pp2"

def fun(list_items, pathie):
    with open(pathie, 'w') as file:
        for item in list_items:
            file.write(f"{item}\n")
