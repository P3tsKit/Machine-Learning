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

- **Training**: 880 images
- **Validation**: 220 images

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

### Rescaling (for Validation and Testing)
For validation and testing datasets, only rescaling is applied, which normalizes the pixel values to `[0, 1]` to match the training data.
