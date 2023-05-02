
#load packages for deleting files
from glob import glob as glob
import os
import shutil
import pdb
from multiprocessing import Pool

stim_dir = '/lab_data/behrmannlab/image_sets/stylized-imagenet/'
folder_to_exclude = ['train','val']


files = glob(stim_dir + '*')

#exclude folders in folder_to_exclude
files_to_delete = [f for f in files if not any([f.endswith(x) for x in folder_to_exclude])]


def delete_file(file_path):
    if os.path.isfile(file_path):
        # If the path is a file, delete it
        os.remove(file_path)
    elif os.path.isdir(file_path):
        # If the path is a directory, delete it and all its contents
        shutil.rmtree(file_path)
    else:
        # If the path is neither a file nor a directory, raise an exception
        raise ValueError(f'{file_path} is not a valid file or directory')

if __name__ == '__main__':
    # Create a process pool with the number of CPUs available
    with Pool() as p:
        # Use the pool.map method to call delete_file function on each file path in parallel
        p.map(delete_file, files_to_delete)