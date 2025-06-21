## Question #57

A company has an ML model that needs to run one time each night to predict stock values. The model input is 3 MB of data that is collected during the current day. The model produces the predictions for the next day. The prediction process takes less than 1 minute to finish running.

How should the company deploy the model on Amazon SageMaker to meet these requirements?

- A. Use a multi-model serverless endpoint. Enable caching.
- B. Use an asynchronous inference endpoint. Set the InitialInstanceCount parameter to 0.
- C. Use a real-time endpoint. Configure an auto scaling policy to scale the model to 0 when the model is not in use.
- D. Use a serverless inference endpoint. Set the MaxConcurrency parameter to 1. 

Correct Answer: 
D Community vote distribution D (100%)