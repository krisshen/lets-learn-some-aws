## Question #97

A company uses 10 Reserved Instances of accelerated instance types to serve the current version of an ML model. An ML engineer needs to deploy a new version of the model to an Amazon SageMaker real-time inference endpoint.

The solution must use the original 10 instances to serve both versions of the model. The solution also must include one additional Reserved Instance that is available to use in the deployment process. The transition between versions must occur with no downtime or service interruptions.

Which solution will meet these requirements?

- A. Configure a blue/green deployment with all-at-once traffic shifting.
- B. Configure a blue/green deployment with canary traffic shifting and a size of 10%.
- C. Configure a shadow test with a traffic sampling percentage of 10%.
- D. Configure a rolling deployment with a rolling batch size of 1. 

Correct Answer: 
B Community vote distribution B (60%) D (40%)