import cv2
from cv2 import dnn_superres
import os

models = ['FSRCNN_x4','EDSR_x4']
modelname = ['fsrcnn','edsr']

# Create an SR object
sr = dnn_superres.DnnSuperResImpl_create()

# Read image
image = cv2.imread('yonderhills.jpg')

for index,names in enumerate(models):
# Read the desired model
    path = f"{names}.pb"
    sr.readModel(path)
    
    # Set CUDA backend and target to enable GPU inference
    sr.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
    sr.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

    # Set the desired model and scale to get correct pre- and post-processing
    sr.setModel(f'{modelname[index]}', 4)

    # Upscale the image
    result = sr.upsample(image)

    Rescalepath = 'RescaledImages'

    # Save the image
    cv2.imwrite(os.path.join(f'{Rescalepath}/{names}'+'.png'), result)