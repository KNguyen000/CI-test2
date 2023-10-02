# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from src.models.ml_models import *


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    models = Model("Resnet", 0.9, 0.8)

    print(type(models.name)==str)
