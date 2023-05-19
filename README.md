
# Pneumonia Detection Web App with deployment using HF Spaces

![GitHub](https://img.shields.io/github/license/Taha533/Pneumonia-Detection-WebApp-and-deployment-using-HF-Spaces)
![Python](https://img.shields.io/badge/python-v3.8-blue)
![TensorFlow](https://img.shields.io/badge/tensorflow-v2.5.0-orange)

## Table of Contents
- [Dataset](#dataset)
- [Model Architecture](#model-architecture)
- [Data Augmentation](#data-augmentation)
- [Training](#training)
- [Web Application](#web-application)
- [Usage](#usage)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

This project aims to classify pneumonia using the transfer learning model VGG19. The dataset used for training the model consists of 5,856 images of chest X-rays. The trained model can classify whether an input chest X-ray image is positive or negative for pneumonia.

## Dataset
The dataset used in this project contains 5,856 chest X-ray images. It includes both pneumonia-positive and pneumonia-negative cases. You can obtain the dataset from this [source](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia).

## Model Architecture
The VGG19 model is a deep convolutional neural network architecture that has proven to be effective for various computer vision tasks. It consists of 19 layers, including 16 convolutional layers and 3 fully connected layers. The model has been pre-trained on the ImageNet dataset, which enables it to learn rich features from images.

## Data Augmentation
To improve the model's performance and increase the diversity of the training data, data augmentation techniques have been applied. Augmentation includes flips, shear and zoom. These techniques help to reduce overfitting and improve the model's generalization ability.

## Training
The model has been trained on the augmented dataset using transfer learning. The pre-trained VGG19 model was used as the base model, and the last fully connected layer was replaced with a new classification layer. The model was trained using the Adam optimizer with a learning rate of 0.001 for 15 epochs.

## Web Application
A web application has been developed using Gradio to provide a user-friendly interface for pneumonia detection. The application allows users to upload a chest X-ray image, and it provides a result based on the image, indicating whether the image is positive or negative for pneumonia.



## Usage




## Usage

1. Clone the repository:

```bash
git clone [https://github.com/your-username/Pneumonia-Detection.git](https://github.com/Taha533/Pneumonia-Detection-WebApp-and-deployment-using-HF-Spaces.git)
```
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```
3. Run the web application:

```bash
python app.py
```

## Requirements

Python\
TensorFlow\
keras\
Gradio\
Numpy

To see the model building procedure properly, check out my notebook here: https://www.kaggle.com/code/taha07/pneumonia-detection-using-transfer-learning

## Sample:
![image](https://user-images.githubusercontent.com/64063436/206949412-ec23d84d-56da-4900-bcbb-11d3b63f05f9.png)

## Contributing
Contributions to this project are welcome. If you find any issues or want to add new features, please feel free to submit a pull request.

## License
This project is licensed under the [MIT License](https://github.com/Taha533/Pneumonia-Detection-WebApp-and-deployment-using-HF-Spaces/blob/main/LICENSE). You are free to modify and distribute the code for personal or commercial purposes.
   


