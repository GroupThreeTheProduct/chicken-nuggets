'''earthEyes demonstrates PIL.Image.paste()
Unpublished work (c)2013 Project Lead The Way
CSE Activity 1.3.7 PIL API
Version 9/10/2013 '''

import PIL
import matplotlib.pyplot as plt
import os.path              

# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
student_file = os.path.join(directory, 'student.jpg')

student_img = PIL.Image.open(student_file)

# Open, resize, and display earth
earth_file = os.path.join(directory, 'earth.png')
earth_img = PIL.Image.open(earth_file)
earth_small = earth_img.resize((89, 87)) #eye width and height measured in plt

# Paste earth into right eye and display
# Uses alpha from mask
student_img.paste(earth_small, (1162, 966), mask=earth_small)
student_img.paste(earth_small, (700, 940), mask=earth_small)
# Display
fig3, axes3 = plt.subplots(1, 2)
axes3[0].imshow(student_img, interpolation='none')
axes3[1].imshow(student_img, interpolation='none')
axes3[1].set_xlim(500, 1500)
axes3[1].set_ylim(1130, 850)
fig3.show()