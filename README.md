# Bottle Fill Detection

## University Project | Computer Vision | OpenCV

A university project that detects the fill level of bottles using computer vision techniques.

---

## Description

This project was developed to analyze images of bottles and determine their fill level based on contour detection and aspect ratio calculations. It uses OpenCV for image processing and NumPy for numerical operations.

> **Note:** The **documentation is currently only available in German**, but an English version might be provided in the future.

---

## Getting Started

### Dependencies

- Python 3.8 or later
- OpenCV
- NumPy
- imutils

### Dataset

The dataset used for training and testing can be downloaded from the following link:

[Download Bottle Dataset](#)  

After downloading, extract the dataset and specify the correct path in the code. In `main.py`, update the `path` variables to match the location of your dataset. You can also choose whether to use the **train** or **test** set by modifying the file paths accordingly.

Example:
```python
# Set dataset path and mode (train/test)
path = glob.glob("C:/Users/yourname/Desktop/Flaschendatensatz/test/0/*.JPG")
```

### Executing program

Run `main.py` and click through the images with space bar.

The script will analyze images from the dataset and classify them based on fill levels (Empty, 25%, 50%, 75%, Full).

---

## How It Works

1. **Image Loading & Scaling**  - Resizes images for efficient processing.
2. **Grayscale Conversion & Blurring**  - Converts images to grayscale and applies Gaussian blur.
3. **Thresholding & Morphological Transformations**  - Extracts liquid area using binary thresholding and removes noise.
4. **Contour Detection & Fill Level Classification**  - Identifies the largest contour and classifies the bottle’s fill level based on its aspect ratio.

---

## Documentation

The **full documentation is available in German**. If an English version is created in the future, it will be included here.

---

## Help

If you encounter issues, ensure that all dependencies are installed correctly. 

---

## Authors

- Mustafa Kilci - [@m-kilci](https://github.com/m-kilci)

---

## License

This project is licensed under the **MIT License** - see the LICENSE file for details.
Feel free to use and modify it!


