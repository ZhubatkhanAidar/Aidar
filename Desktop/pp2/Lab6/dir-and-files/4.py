import os

pathie = "C:/Users/Aidar/Desktop/pp2"

def fun(pathie):
    with open(pathie, 'r') as file:
        print("Number of lines:", len(file.readlines()))
