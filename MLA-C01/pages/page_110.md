## Question #110

An ML engineer has deployed an Amazon SageMaker model to a serverless endpoint in production. The model is invoked by the InvokeEndpoint API operation.

The model's latency in production is higher than the baseline latency in the test environment. The ML engineer thinks that the increase in latency is because of model startup time.

What should the ML engineer do to confirm or deny this hypothesis?

- A. Schedule a SageMaker Model Monitor job. Observe metrics about model quality.
- B. Schedule a SageMaker Model Monitor job with Amazon CloudWatch metrics enabled.
- C. Enable Amazon CloudWatch metrics. Observe the ModelSetupTime metric in the SageMaker namespace.
- D. Enable Amazon CloudWatch metrics. Observe the ModelLoadingWaitTime metric in the SageMaker namespace. 

Correct Answer: 
D Community vote distribution D (67%) C (33%)