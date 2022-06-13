'''
Generating MetaData for image Dataset
This module consist for create_metadata function which extracts metadata of the image passed and returns it as a csv file
Author Parth Shah shah.parth3@northeastern.edu'
Created at 11th June 2022

Creating Metadata is means you need to make a for loop which iterates over all your images and pass all your images through Pillow package
which will extract the metadata such as image size, image color, image channels. Make use of this metadata for you expecations and profling.
'''

from __future__ import annotations
from PIL import Image
from PIL.ExifTags import TAGS
import pandas as pd
import os

def create_metadata(image_directory,extra_file):
    '''
    This Function downloads the csv file with metadata for image folder provided
    Parameters:
    ---------------------
    image_directory: string
        Directory of Images where they are all stored.
    extra_file: string 
        File Path for the file which you want to merge with the Dataset for this example it is annotations file
        
    '''
    # assign directory
    annotations = pd.read_csv(extra_file)
    # iterate over files in
    # that directory
    info_dict = {}
    for filename in os.listdir(image_directory):
        print("Reading file:",filename)
        f = os.path.join(image_directory, filename)
        imagename = f
        info_dict[filename] = {}
        # # read the image data using PIL
        image = Image.open(imagename)
        info_dict[filename]['image_size']  = image.size
        info_dict[filename]['image_Height']  = image.height
        info_dict[filename]['image_Width']  = image.width
        info_dict[filename]['image_Format']  = image.format
        info_dict[filename]['image_mode'] = image.mode
        info_dict[filename]['image_Animated']  = getattr(image, "is_animated", False)
        info_dict[filename]['image_Frames']  = getattr(image, "n_frames", 1)
        print("Inserted in DataFrame")

    df_final = pd.DataFrame.from_dict(info_dict)

    df = df_final.T
    df.reset_index(inplace= True)
    print("Merging Extra Files")
    df = pd.merge(df,annotations,left_on = 'index', right_on = 'image_id',how = 'left')
    df.to_csv('MetaData.csv')
    print("***************************")
    print(df.head())

#run when file is directly executed
if __name__ == '__main__':
    create_metadata('archive/images','archive/annotations.csv')
    print("done")


