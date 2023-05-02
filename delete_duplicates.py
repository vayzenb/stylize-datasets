from glob import glob as glob
import pandas as pd
import os

import natsort
from multiprocessing import Pool
import pdb

def delete_image_files(dir_path):
    # Get a list of all image files in the directory
    image_files = glob.glob(os.path.join(dir_path, '*.png')) + glob.glob(os.path.join(dir_path, '*.jpg')) + glob.glob(os.path.join(dir_path, '*.JPEG')) + glob.glob(os.path.join(dir_path, '*.gif'))







img_dir = '/lab_data/behrmannlab/image_sets/stylized-ecoset/train'

img_dir = '/lab_data/behrmannlab/image_sets/stylized-ecoset/train/0001_man'

image_files = glob(f'{img_dir}/*-stylized-*.JPEG') +  glob(f'{img_dir}/*-stylized-*.jpg')

image_files = natsort.natsorted(image_files,reverse=True)

im_list  = pd.DataFrame(image_files, columns=['file_name'])

file_list = im_list['file_name'].str.split('-stylized-', expand=True)
#count the number of each item in the pd column and put it in a new column
file_list['count'] = file_list.groupby(0)[0].transform('count')

#remove all rows where the count is less than 2
file_list = file_list[file_list['count'] > 1]

#loop through items and check if the next item is the same as the previous item
# if it is, then add the second item to the list

delete_list = []
for i in range(len(file_list)-1):
    if file_list.iloc[i,0] == file_list.iloc[i+1,0]:
        delete_list.append(file_list.iloc[i+1,0] + '-stylized-' + file_list.iloc[i+1,1])




# Use multiprocessing to delete the image files in parallel
with Pool() as p:
    p.map(os.remove, delete_list)