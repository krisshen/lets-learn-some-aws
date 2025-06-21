## Question #87

A company has an Amazon S3 bucket that contains 1 ТВ of files from different sources. The S3 bucket contains the following file types in the same S3 folder: CSV, JSON, XLSX, and Apache Parquet.

An ML engineer must implement a solution that uses AWS Glue DataBrew to process the data. The ML engineer also must store the final output in Amazon S3 so that AWS Glue can consume the output in the future.

Which solution will meet these requirements?

- A. Use DataBrew to process the existing S3 folder. Store the output in Apache Parquet format.
- B. Use DataBrew to process the existing S3 folder. Store the output in AWS Glue Parquet format.
- C. Separate the data into a different folder for each file type. Use DataBrew to process each folder individually. Store the output in Apache Parquet format.
- D. Separate the data into a different folder for each file type. Use DataBrew to process each folder individually. Store the output in AWS Glue Parquet format. 

Correct Answer: 
C Community vote distribution C (50%) A (50%)