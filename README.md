# Python Image Upscaler

This is a simple image upscaling script using OpenCv super-resolution module written in python. I have compared two pretrained models [FSRCNN, EDSR] for x4 scaling. For other scale ratios such as x2,x3 you should download the corresponding model from here [EDSR](https://github.com/Saafke/EDSR_Tensorflow/tree/master/models), [FSRCNN](https://github.com/Saafke/FSRCNN_Tensorflow/tree/master/models).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install OpenCV.

```bash
pip install opencv-contrib-python
```

## Usage

Steps:
1. Installing OpenCV with the contrib modules (containing dnn_superres).
2. Downloading the pre-trained models.
3. Upscaling the image.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)