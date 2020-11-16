from __future__ import print_function
import torch
import torchvision
import torchvision.transforms as transforms

import torch.nn as nn
import torch.nn.functional as F

from PIL import Image
from dataLoaderFile.matlabReader import returnImage
import numpy as np

from dataLoaderFile import dataLoader

data = dataLoader.main()


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        # self.fc1 = nn.Linear(16*5*5, 120)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        print(x.size)


net = Net()

# labels = []
# inputPaths = []


# for i, d in enumerate(data, 0):
#     inputPaths = d
#     print(inputPaths)

# take one batch
inputBatch = data[0]

# split the batch into labels and input paths
unzipped = [[i for i, j in inputBatch],
            [j for i, j in inputBatch]]
# print(unzipped)

labels, inputPaths = unzipped
# print(f'inputs: {inputPaths} labels: {labels}')

# creates new inputs list
inputs = []

# for every path in inputPaths, load the image.
# If it is a 'no' image then it has a opens with pillow
# Otherwise it uses the same returnImage function from matlabReader
for i in inputPaths:
    if '.mat' in str(i):
        inputs = inputs + [returnImage(i)]
    elif '.png' in str(i):
        inputs = inputs + [Image.open(str(i))]
print(inputs)

trans = transforms.ToTensor()

ninputs = np.array(inputs)
print(ninputs.shape)
# net.forward(trans(inputs))

# img = Image.open(inputPaths[3])
# print(str(inputPaths[3]).lstrip("b'").rstrip("'"))

# print(data[0][3][1])
# img_pil = Image.open(img)
# newimg = img.convert('RGB')
# print(f'imagemode {img.mode} {img.getbands()} newimg {newimg.getbands()}')
# img.show()
# newimg.show()
# img.save('image1.png')
# newimg.save(f'newimage{newimg.mode}.jpeg')


# print(net)
# # print(group)
# print(data)
# tensor1 = trans(data)
# net.forward(data)