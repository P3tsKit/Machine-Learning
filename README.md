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

1. **Base Model**  
   - InceptionV3 pre-trained on ImageNet.
   - Fully connected layers excluded (`include_top=False`).
   - Input shape: `(224, 224, 3)`.

2. **Fine-Tuning**  
   - Layers frozen: All except the last 30 layers.

3. **Custom Layers**
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

![Screenshot 2024-12-12 175005](https://github.com/user-attachments/assets/7c387680-3a33-440a-8524-ed48dcfc1d07)

## Testing

![Screenshot 2024-12-12 182437](https://github.com/user-attachments/assets/39834d69-ac1c-4b54-8bbc-80dc98430992)

## Model Saving

Model is saved in HDF5 format dan Keras format.

## Model API

A Flask-based API is built to serve the trained model for predicting skin diseases in dogs and cats. The API accepts an image as input, processes it, and returns the predicted disease class along with relevant information.

### Endpoints

1. **Home Page**
   - **URL**: `/`
   - **Method**: GET
   - **Description**: Returns the home page with an interface for image upload.
   - 
2. **Prediction Endpoint**
   - **URL**: `/predict`
   - **Method**: POST
   - **Description**: Accepts an image file, processes it, and returns the predicted class along with additional disease information.

   **Request Example**:
   - Upload an image file as a form-data key named `file`.

   **Response Example**:
   ```json
   {
       "predicted_class": "Ringworm",
       "disease_info": {
           "description": "Ear mites are tiny parasites that live in the ear canal of dogs or cats causing itching, pain and abnormal discharge. If left untreated ear mites can lead to secondary infections or hearing loss.",
           "causes": "Ear Mites are generally spread through close contact with other animals, such as dogs or cats, that already have ear mites. Animals can contract ear mites from contaminated surroundings, bedding or toys. Animals that do not have monthly vaccinations are particularly at risk of ear mites if exposed.",
           "symptoms": [
            "1. Shaking the head",
            "2. Itchy and red ears",
            "3. Ear odor",
            "4. Thick brown or black discharge from the ear",
            "5. Sore and sensitive ears",
            "6. Head Tilt",
            "7. Loss of hair around the ears and eyes",
            "8. Decreased appetite",
            "9. Lethargic"
        ],
           "treatment": [
            "1. Clean the ears of dogs and cats with an ear cleaner every day or twice a day.", 
            "2. Topical and oral treatment of dogs and cats."
        ],
           "note": "If the condition does not get better, consult a veterinarian for further treatment.",
           "source": "https://www.petmd.com/dog/conditions/infectious-parasitic/ear-mites-dogs-what-are-they-and-how-do-you-treat-them"
       }
   }
   ```

   If the confidence is below the threshold:

   ```json
   {
       "predicted_class": "Sorry, disease cannot be detected",
       "disease_info": null
   }
   ```
## Running the API

1. Install the required dependencies listed in requirements.txt.

   ```bash
   pip install -r requirements.txt
   ```

2. Run the flask API.

   ```bash
   python main.py
   ```
