import pandas as pd
import matplotlib.pyplot as plt
import feature_hair, feature_pen_marks, feature_A, feature_B, feature_C # all of our features
import cv2

# ------------------
data_path = "../data/"
img_path = data_path + "imgs/"
mask_path = data_path + "masks/"

class Picture:
    def __init__(self, input_ID, img_path = img_path, mask_path = mask_path) -> None:
        self.input_ID = input_ID
        self.img_file = img_path + self.input_ID
        self.mask_file = (mask_path + self.input_ID).replace(".png","_mask.png")
        self.img_org = cv2.imread(self.img_file)
        self._grey = cv2.cvtColor(self.img_org, cv2.COLOR_RGB2GRAY)  #img_file
      
    def _raw_picture(self) -> list:
        return self.img_file

    def mask(self) -> list:
        return self.mask_file

    def clean_picture(self):
        # Step 1 call feature_hair (need greyscale)
        self.blackhat, self.hair_mask, self.hairless = feature_hair.removeHair(self.img_org, self._grey)
        # Step 2 call feature_pen (on hair removed pic)
        
        return self.hairless
# ------------------

img1 = Picture("PAT_8_15_820.png")
print(img1.clean_picture())


    