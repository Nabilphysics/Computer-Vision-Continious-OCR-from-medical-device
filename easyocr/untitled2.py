# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 22:23:17 2021

@author: CTO
"""
################################
##Generated with a lot of love##
##    with   EasyPython       ##
##Web site: easycoding.tn     ##
################################
import urllib.request
import cv2 as cv #Please install with PIP: pip install cv2
import numpy as np

frame = None
key = None


print('START')
while True:
  imgResponse = urllib.request.urlopen ('http://192.168.0.108/capture?')
  imgNp = np.array(bytearray(imgResponse.read()),dtype=np.uint8)
  frame= cv.imdecode (imgNp,-1)
  cv.imshow('Window',frame)
  key = cv.waitKey(500)
  if key == (ord('q')):
    break
cv.destroyAllWindows()
print('TNE END')