import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw  

'''This program will put a border around all images in a folder, 
currently just a white border but the goat logo will be added.'''
def goatframe (image, percentborder):
    '''puts a frame with the goat logo on an image
    must be a PIL image. border is the percentage input for the 2nd parameter.'''
    width, height = image.size
    borderlength = int( (.01*percentborder) * min(width, height))
    
    rect_mask = PIL.Image.new('RGBA', (width, height), (127, 0, 127, 0))
    drawing_layer = PIL.ImageDraw.Draw(rect_mask)
    
    drawing_layer.polygon( [(borderlength, borderlength),(width-borderlength, 
    borderlength),(width-borderlength, height-borderlength),(borderlength,
    height-borderlength)], fill=(127,0,127,255) )
    
    result = PIL.Image.new ('RGBA', image.size, (0,0,0,0))
    result.paste(image, (0,0), mask = rect_mask)
    return result
    
    
    
def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list
    
    
    
    
def goatborder_all_images(directory=None):
     
    """ Saves a modfied version of each image in directory.

    Uses current directory if no directory is specified. 
    Places images in subdirectory 'modified', creating it if it does not exist.
    New image files are of type PNG and have transparent rounded corners.
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    #load all the images
    image_list, file_list = get_images(directory)  

    #go through the images and save modified versions
    for n in range(len(image_list)):
        # Parse the filename
        filename, filetype = os.path.splitext(file_list[n])
        
        # Round the corners with radius = 30% of short side
        new_image = goatframe(image_list[n],10)
        #save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)