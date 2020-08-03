# facial-landmark-dataset
A collection of public facial landmark datasets and the Python code to make use of them.

## Supported Datasets

| Name        | Author                                                                                                         | Published | #Marks | #Samples |
| ----------- | -------------------------------------------------------------------------------------------------------------- | --------- | ------ | -------- |
| 300-W       | [Imperial College London](https://ibug.doc.ic.ac.uk/resources/300-W/)                                          | 2013      | 68     | 600      |
| 300-VW      | [Imperial College London](https://ibug.doc.ic.ac.uk/resources/300-VW/)                                         | 2015      | 68     | 218597   |
| AFW         | [Imperial College London](https://ibug.doc.ic.ac.uk/resources/facial-point-annotations/)                       | 2013      | 68     | 337      |
| AFLW        | [Graz University of Technology](https://www.tugraz.at/institute/icg/research/team-bischof/lrs/downloads/aflw/) | 2011      | 21     |          |
| AFLW2000-3D | [Chinese Academy of Sciences](http://www.cbsr.ia.ac.cn/users/xiangyuzhu/projects/3DDFA/main.htm)               | 2015      | 68     | 2000     |
| HELEN       | [Imperial College London](https://ibug.doc.ic.ac.uk/resources/facial-point-annotations/)                       | 2013      | 68     | 2330     |
| IBUG        | [Imperial College London](https://ibug.doc.ic.ac.uk/resources/facial-point-annotations/)                       | 2013      | 68     | 135      |
| LFPW        | [Imperial College London](https://ibug.doc.ic.ac.uk/resources/facial-point-annotations/)                       | 2013      | 68     | 1035     |
| WFLW        | [Tsinghua National Laboratory](https://wywu.github.io/projects/LAB/WFLW.html)                                  | 2018      | 98     | 10000    |

*Face images and mark coordinates are required. Some dataset used existing images from other dataset, in which case the dataset was named after the image dataset.*

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
OpenCV 4.x

### Installing
Just git clone this repo and you are good to go.

```shell
# From your favorite development directory
git clone https://github.com/yinguobing/facial-landmark-dataset
```

## How to run

First, initialize the dataset. Take 300W as an example.
```python
from fmd.ds300w import DS300W

# Set the path to the dataset directory.
DS300W_DIR = "/home/robin/data/facial-marks/300W"

# Construct a dataset.
ds = DS300W("300w")

# Populate the dataset with essential data
ds.populate_dataset(DS300W_DIR)

# See what we have got.
print(ds)
```
Possible output:

```shell
name: 300w
authors: [Imperial College London]
year: 2013
num_marks: 68
num_samples: 600
```

### Pick one sample, randomly

Once the dataset is constructed:
```python
sample = ds.pick_one()
```

### Enumerate the dataset
This could be useful when you are trying to transform or export the dataset.
```python
for sample in ds:
    # do whatever you want, like
    print(sample.marks)
```

### Read image file
Read in the image file as a numpy array, and show the image.

```python
image = sample.read_image()

import cv2
cv2.imshow("Preview", image)
cv2.waitKey()
```

### Get all the marks

```python
facial_marks = sample.marks
```

### Get the key marks
The key marks are: left eye left corner, left eye right corner, right eye left corner, right eye right corner, mouse left corner, mouse right corner.

```python
key_marks = sample.get_key_marks()
```

### Draw the marks
```python
draw_marks(image, facial_marks)
```

## Authors
Yin Guobing (尹国冰) - yinguobing

![wechat](docs/wechat.png)

## License
![GitHub](https://img.shields.io/github/license/yinguobing/facial-landmark-dataset)

## Acknowledgments
All the dataset authors who made their data public.