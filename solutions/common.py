import os


def read_input(name):
    path = os.path.join(os.path.dirname(__file__), f'../inputs/{name}.txt')
    with open(path, 'r') as file:
        return file.readlines()
