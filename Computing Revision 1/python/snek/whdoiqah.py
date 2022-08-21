import numpy as np
import pandas as pd
import cv2 as cv
from google.colab.patches import cv2_imshow
from skimage import io
from PIL import Imageimport matplotlib.pylab as plt

img = cv.imread("test.jpg",0)
cv2_imshow(img)