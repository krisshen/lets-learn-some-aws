## Question #114

A medical company needs to store clinical data. The data includes personally identifiable information (PII) and protected health information (PHI).

An ML engineer needs to implement a solution to ensure that the PII and PHI are not used to train ML models.

Which solution will meet these requirements?

- A. Store the clinical data in Amazon S3 buckets. Use AWS Glue DataBrew to mask the PII and PHI before the data is used for model training.
- B. Upload the clinical data to an Amazon Redshift database. Use built-in SQL stored procedures to automatically classify and mask the PII and PHI before the data is used for model training.
- C. Use Amazon Comprehend to detect and mask the PII before the data is used for model training. Use Amazon Comprehend Medical to detect and mask the PHI before the data is used for model training.
- D. Create an AWS Lambda function to encrypt the PII and PHI. Program the Lambda function to save the encrypted data to an Amazon S3 bucket for model training. 

Correct Answer: 
C Community vote distribution C (100%)