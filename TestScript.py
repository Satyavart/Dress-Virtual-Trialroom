from Measurements import Measurements
from PIL import Image
import cv2
import os
# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def start(front, bent, back, shirt):    
    error = 6
    inches = 76+error
    #m = Measurements(inches, front, bent, back)
    m = Measurements(inches, frontView=front)
    '''
    print(m.shoulder_width)
    print(m.right_shoulder_elbow)
    print(m.right_elbow_wrist)
    print(m.left_shoulder_elbow )
    print(m.left_elbow_wrist )
    print(m.right_shoulder_wrist )
    print(m.left_shoulder_wrist )
    print(m.shoulder_hip)
    print(m.right_hip_ankle )
    print(m.left_hip_ankle )
    print(m.right_hip_knee )
    print(m.left_hip_knee )
    print(m.hip_ankle_max )
    print(m.chest_point)
    '''
    #shirt_height = 29.875
    shirt_height = 26.125
    shoulder_length = 18.875
    sleeve_length = 32.5
    print("image height ", shirt_height/m.inchesPerPixel)
    print("image width ", (m.calc.getDistance(m.points[1][0], m.points[3][0]) + (1.5/m.inchesPerPixel))*2)
    Original_Image = Image.open(bent).convert('RGBA')
    Original_Image_Copy = Original_Image.copy()
    original_height, original_width = Original_Image.size
    image_ratio = original_height/original_width
    shirt_image = Image.open(shirt).convert('RGBA')
    shirt_image_copy = shirt_image.copy()
    shirt_image_copy = shirt_image_copy.resize((int(shirt_height/(image_ratio * m.inchesPerPixel)),int(shirt_height/m.inchesPerPixel)))
    _, width = shirt_image_copy.size
    coordinate_x = m.points[1][0] - width/2 - (2.5/m.inchesPerPixel)
    coordinate_y = m.points[1][1] + (3/m.inchesPerPixel)
    # paste image giving dimensions
    Original_Image_Copy.paste(shirt_image_copy, (int(coordinate_x), int(coordinate_y)), shirt_image_copy)
    # save the image
    Original_Image_Copy.save('C:/Classnotes/Dress-Virtual-Trialroom/output_maybe_success.png', format='png')
    # img = cv2.imread('output_maybe_success.png')
    # imgplot = plt.imshow(img)
    # plt.show()
    img = cv2.imread('C:/Classnotes/Dress-Virtual-Trialroom/output_maybe_success.png')
    path = 'C:/Classnotes/Dress-Virtual-Trialroom/'
    cv2.imwrite(os.path.join(path , 'static/out.jpg'), img)
    cv2.waitKey(0)



