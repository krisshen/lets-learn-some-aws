## Question #54

A company uses Amazon SageMaker for its ML workloads. The company's ML engineer receives a 50 MB Apache Parquet data file to build a fraud detection model. The file includes several correlated columns that are not required.

What should the ML engineer do to drop the unnecessary columns in the file with the LEAST effort?

- A. Download the file to a local workstation. Perform one-hot encoding by using a custom Python script.
- B. Create an Apache Spark job that uses a custom processing script on Amazon EMR.
- C. Create a SageMaker processing job by calling the SageMaker Python SDK.
- D. Create a data flow in SageMaker Data Wrangler. Configure a transform step. 

Correct Answer: 
D Community vote distribution D (100%)