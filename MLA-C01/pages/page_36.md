## Question #36

A company has implemented a data ingestion pipeline for sales transactions from its ecommerce website. The company uses Amazon Data Firehose to ingest data into Amazon OpenSearch Service. The buffer interval of the Firehose stream is set for 60 seconds. An OpenSearch linear model generates real-time sales forecasts based on the data and presents the data in an OpenSearch dashboard.

The company needs to optimize the data ingestion pipeline to support sub-second latency for the real-time dashboard.

Which change to the architecture will meet these requirements?

- A. Use zero buffering in the Firehose stream. Tune the batch size that is used in the PutRecordBatch operation.
- B. Replace the Firehose stream with an AWS DataSync task. Configure the task with enhanced fan-out consumers.
- C. Increase the buffer interval of the Firehose stream from 60 seconds to 120 seconds.
- D. Replace the Firehose stream with an Amazon Simple Queue Service (Amazon SQS) queue. 

Correct Answer: 
A Community vote distribution A (100%)