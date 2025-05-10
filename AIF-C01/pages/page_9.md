## Question #9

 A company wants to create a chatbot by using a foundation model (FM) on Amazon Bedrock. The FM needs to access encrypted data that is stored in an Amazon S3 bucket. The data is encrypted with Amazon S3 managed keys (SSE-S3).

The FM encounters a failure when attempting to access the S3 bucket data.

Which solution will meet these requirements?

- A. Ensure that the role that Amazon Bedrock assumes has permission to decrypt data with the correct encryption key.

- B. Set the access permissions for the S3 buckets to allow public access to enable access over the internet.

- C. Use prompt engineering techniques to tell the model to look for information in Amazon S3.

- D. Ensure that the S3 data does not contain sensitive information.