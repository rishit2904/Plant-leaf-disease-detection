# 🌿 Plant Leaf Disease Detection

A deep learning-based system for detecting and classifying diseases in plant leaves using computer vision and neural networks.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Deep Learning](https://img.shields.io/badge/Deep-Learning-green.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-orange.svg)
![Computer Vision](https://img.shields.io/badge/Computer-Vision-purple.svg)

## 📋 Overview

This project uses convolutional neural networks (CNNs) to automatically detect and classify diseases in plant leaves. Early detection of plant diseases is crucial for agricultural productivity and food security.

## 🎯 Features

- **Disease Detection**: Identify various plant leaf diseases from images
- **Multi-Class Classification**: Support for multiple disease categories
- **Deep Learning Model**: CNN architecture for accurate predictions
- **Data Pipeline**: Complete data preprocessing and augmentation
- **Visualization**: Training metrics and prediction results

## 📁 Project Structure

```
Plant-leaf-disease-detection/
├── README.md                              # Project documentation
├── Plant-leaf-disease-detection-main.zip # Archived project files
├── data/                                  # Dataset directory
├── notebooks/                             # Jupyter notebooks
└── src/                                   # Source code
```

## 🦠 Supported Diseases

The model can detect various plant diseases including:
- Bacterial infections
- Fungal diseases
- Viral infections
- Nutrient deficiencies
- Healthy plant classification

## 🛠️ Tech Stack

- **Python 3.8+**
- **TensorFlow/Keras** - Deep learning framework
- **OpenCV** - Image processing
- **NumPy & Pandas** - Data manipulation
- **Matplotlib & Seaborn** - Visualization
- **Scikit-learn** - ML utilities

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- GPU recommended for training (optional)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/rishit2904/Plant-leaf-disease-detection.git
   cd Plant-leaf-disease-detection
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install tensorflow numpy pandas matplotlib seaborn opencv-python scikit-learn jupyter
   ```

4. **Extract archived files** (if needed)
   ```bash
   unzip Plant-leaf-disease-detection-main.zip
   ```

### Running the Project

1. **Start Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

2. **Navigate to `notebooks/` directory**

3. **Run the notebooks** in order

## 📊 Model Pipeline

1. **Data Collection**: Gather plant leaf images
2. **Preprocessing**: Resize, normalize, augment images
3. **Model Architecture**: Build CNN model
4. **Training**: Train with appropriate hyperparameters
5. **Evaluation**: Assess accuracy and loss
6. **Prediction**: Classify new leaf images

## 📈 Model Performance

The model achieves high accuracy in detecting plant diseases:
- Training accuracy and validation metrics
- Confusion matrix for class-wise performance
- Precision, recall, and F1-score

## 🌱 Applications

- **Precision Agriculture**: Early disease detection in crops
- **Smart Farming**: Automated plant health monitoring
- **Research**: Plant pathology studies
- **Mobile Apps**: Field-deployable disease detection

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add new disease categories
- Improve model accuracy
- Enhance documentation
- Submit pull requests

## 📄 License

This project is open source and available for educational and research purposes.

---

⭐ **Star this repository if you found it helpful!**
