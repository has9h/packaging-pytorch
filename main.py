# import numpy as np
import os
import sys
# import torch
# print(torch.cuda.is_available())
try:
    import cv2
except Exception as e:
    print('Error bundling cv2')
    print(e)
print(cv2.__file__)
print(sys.builtin_module_names)
print(globals())


input('Here to wait.')