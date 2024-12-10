# Machine Learning Documentation

## Dataset Overview

This project uses a dataset of 7 classes of skin diseases in dogs and cats, sourced from **Roboflow**.

### Classes of Diseases

The dataset includes the following skin disease classes:

- Eyelid Lump
- Keratosis
- Ringworm
- Scabies
- Flea Allergy
- Nasal Discharge
- Ear Mites

### Dataset Splitting

- **Training**: 560 images
- **Validation**: 140 images

The images are evenly distributed across all 7 classes to maintain class balance.

## Preprocessing

### Data Augmentation (for Training)
To improve model generalization, the training dataset undergoes various augmentation techniques:

- **Rescaling**: Pixel values are normalized to the range `[0, 1]`.
- **Rotation**: Images are randomly rotated by up to **20 degrees**.
- **Shifting**:
  - **Width shift**: Images are randomly shifted horizontally by up to **20%**.
  - **Height shift**: Images are randomly shifted vertically by up to **20%**.
- **Shear and Zoom**: Random shearing and zooming within a **20%** range.
- **Flipping**: Images are randomly flipped **horizontally**.
- **Fill Mode**: The `nearest` fill mode is used to fill any empty pixels created by transformations.

### Rescaling (for Validation)
For validation dataset, only rescaling is applied, which normalizes the pixel values to `[0, 1]` to match the training data.

## Modeling

The model is built using **InceptionV3**, a pre-trained deep learning model, with custom layers for this specific classification task.

### Architecture

1. **Base Model**:  
   - InceptionV3 pre-trained on ImageNet.
   - Fully connected layers excluded (`include_top=False`).
   - Input shape: `(224, 224, 3)`.

2. **Fine-Tuning**:  
   - Layers frozen: All except the last 30 layers.

3. **Custom Layers**:
   - **Global Average Pooling**: Reduces parameters and improves efficiency.
   - **Dense Layer 1**: 256 neurons with ReLU activation.
   - **Batch Normalization**: Stabilizes and accelerates training.
   - **Dropout**: 40% to reduce overfitting.
   - **Dense Layer 2**: 64 neurons with ReLU activation.
   - **Batch Normalization**: Further stabilization.
   - **Dropout**: An additional 40% dropout rate.
   - **Output Layer**: 7 neurons with softmax activation for multi-class classification.

### Compilation

- **Optimizer**: Adam with a learning rate of `0.0001` for fine-tuning.
- **Loss Function**: Categorical crossentropy.
- **Metrics**: Accuracy.

## Evaluation

After training, the model's performance is visualized using the metrics of accuracy and loss for both training and validation datasets over each epoch. 

![Screenshot 2024-12-10 174148](https://github.com/user-attachments/assets/719131d3-a39c-4b67-a59a-6e1297b32823)

## Testing

![photo-collage png](https://github.com/user-attachments/assets/53622067-1a89-454a-a130-b2709deaee6a)

## Model Saving

Model is saved in HDF5 format dan Keras format.
