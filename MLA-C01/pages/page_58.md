## Question #58

An ML engineer trained an ML model on Amazon SageMaker to detect automobile accidents from dosed-circuit TV footage.

The ML engineer used SageMaker Data Wrangler to create a training dataset of images of accidents and non-accidents.

The model performed well during training and validation. However, the model is underperforming in production because of variations in the quality of the images from various cameras.

Which solution will improve the model's accuracy in the LEAST amount of time?

- A. Collect more images from all the cameras. Use Data Wrangler to prepare a new training dataset.
- B. Recreate the training dataset by using the Data Wrangler corrupt image transform. Specify the impulse noise option.
- C. Recreate the training dataset by using the Data Wrangler enhance image contrast transform. Specify the Gamma contrast option.
- D. Recreate the training dataset by using the Data Wrangler resize image transform. Crop all images to the same size. 

Correct Answer: 
B Community vote distribution B (69%) C (31%)