## Question #92

A company uses Amazon SageMaker for its ML process. A compliance audit discovers that an Amazon S3 bucket for training data uses server-side encryption with S3 managed keys (SSE-S3).

The company requires customer managed keys. An ML engineer changes the S3 bucket to use server-side encryption with AWS KMS keys (SSE-KMS). The ML engineer makes no other configuration changes.

After the change to the encryption settings, SageMaker training jobs start to fail with AccessDenied errors.

What should the ML engineer do to resolve this problem?

- A. Update the IAM policy that is attached to the execution role for the training jobs. Include the s3:ListBucket and s3:GetObject permissions.
- B. Update the S3 bucket policy that is attached to the S3 bucket. Set the value of the aws:SecureTransport condition key to True.
- C. Update the IAM policy that is attached to the execution role for the training jobs. Include the kms:Encrypt and kms:Decrypt permissions.
- D. Update the IAM policy that is attached to the user that created the training jobs. Include the kms:CreateGrant permission. 

Correct Answer: 
C Community vote distribution C (100%)