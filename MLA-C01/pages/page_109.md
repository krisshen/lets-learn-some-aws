## Question #109

An ML engineer needs to merge and transform data from two sources to retrain an existing ML model. One data source consists of .csv files that are stored in an Amazon S3 bucket. Each .csv file consists of millions of records. The other data source is an Amazon Aurora DB cluster.

The result of the merge process must be written to a second S3 bucket. The ML engineer needs to perform this merge-and- transform task every week.

Which solution will meet these requirements with the LEAST operational overhead?

- A. Create a transient Amazon EMR cluster every week. Use the cluster to run an Apache Spark job to merge and transform the data.
- B. Create a weekly AWS Glue job that uses the Apache Spark engine. Use DynamicFrame native operations to merge and transform the data.
- C. Create an AWS Lambda function that runs Apache Spark code every week to merge and transform the data. Configure the Lambda function to connect to the initial S3 bucket and the DB cluster.
- D. Create an AWS Batch job that runs Apache Spark code on Amazon EC2 instances every week. Configure the Spark code to save the data from the EC2 instances to the second S3 bucket. 

Correct Answer: 
B Community vote distribution B (100%)