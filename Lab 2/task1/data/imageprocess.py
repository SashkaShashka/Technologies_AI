import cv2
import numpy as np

def func1(img, core):
    if core.shape[0] % 2 != 1 or core.shape[1] % 2 != 1:
        new_shape_x = core.shape[0] + (1 - core.shape[0] % 2)
        new_shape_y = core.shape[1] + (1 - core.shape[1] % 2)
        
        new_core = np.zeros((new_shape_x, new_shape_y), dtype = int)
        new_core[0:core.shape[0], 0:core.shape[1]] = core
        core = new_core
    stp_x = core.shape[0] - 1
    halfstp_x = stp_x//2
    stp_y = core.shape[1] - 1
    halfstp_y = stp_y//2

    img_bord = np.zeros((img.shape[0]+stp_x, img.shape[1]+stp_y), dtype = np.uint8)
    res = np.zeros((img.shape), dtype = np.uint8)
    
    img_bord[halfstp_x:img.shape[0]+halfstp_x,halfstp_y:img.shape[1]+halfstp_y] = img[:,:]
    
#     img_bord[0:halfstp_x, :] = img_bord[halfstp_x, :]
#     img_bord[img.shape[0]+halfstp_x:img.shape[0]+stp_x, :] = img_bord[img.shape[0]+halfstp_x-1, :]
    
#     img_bord[:, 0:halfstp_y] = img_bord[:, halfstp_y].reshape(img_bord.shape[0], 1)
#     img_bord[:, img.shape[1]+halfstp_y:img.shape[1]+stp_y] = img_bord[:, img.shape[1]+halfstp_y-1].reshape(img_bord.shape[0], 1)
    
    core = core.reshape(1,-1)

    for i in range(halfstp_x, img.shape[0]+halfstp_x):
        for j in range(halfstp_y, img.shape[1]+halfstp_y):
            window = img_bord[i-halfstp_x:i+halfstp_x+1,j-halfstp_y:j+halfstp_y+1].copy()
            summ = 0
            window = window.reshape(1,-1)              
            for k in range(0, window.shape[1]):
                summ = summ + (window[0,k]*core[0,core.shape[1]-1-k])
            res[i-halfstp_x,j-halfstp_y] = summ
    return res

def threshold(img_grayscale, threshold = 127):
    img_threshold = img_grayscale.copy()
    img_threshold[img_threshold < threshold] = 0
    img_threshold[img_threshold >= threshold] = 255
    return img_threshold

img = cv2.imread("/usr/app/src/input.png", cv2.IMREAD_GRAYSCALE)

mask1 = (1/6) * np.array([
    [-1,-1,-1],
    [ 0, 0, 0],
    [ 1, 1, 1]
])
mask2 = mask1.T

x = func1(img, mask1)
y = func1(img, mask2)

img_grad_contour = np.sqrt(x**2 + y**2).astype(np.uint8)

img_grad_contour_binary = threshold(img_grad_contour, 4)

cv2.imwrite("/usr/app/src/output.png", img_grad_contour_binary)
