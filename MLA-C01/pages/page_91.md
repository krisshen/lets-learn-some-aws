## Question #91

A company runs Amazon SageMaker ML models that use accelerated instances. The models require real-time responses. Each model has different scaling requirements. The company must not allow a cold start for the models.

Which solution will meet these requirements?

- A. Create a SageMaker Serverless Inference endpoint for each model. Use provisioned concurrency for the endpoints.
- B. Create a SageMaker Asynchronous Inference endpoint for each model. Create an auto scaling policy for each endpoint.
- C. Create a SageMaker endpoint. Create an inference component for each model. In the inference component settings, specify the newly created endpoint. Create an auto scaling policy for each inference component. Set the parameter for the minimum number of copies to at least 1.
- D. Create an Amazon S3 bucket. Store all the model artifacts in the S3 bucket. Create a SageMaker multi-model endpoint. Point the endpoint to the S3 bucket. Create an auto scaling policy for the endpoint. Set the parameter for the minimum number of copies to at least 1. 

Correct Answer: 
C Community vote distribution C (67%) A (33%)