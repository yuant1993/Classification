This is the document classification web service for HeavyWater

Using instruction:
On the home page, please upload one CSV test file having the same format as the "shuffled-full-set-hashed.csv" and click the "Summit" button.
This will lead to the classification page which will show you a table having "True label", "Predicted label" and "Confidence score" columns and also the accuracy_score above the table.
On this page, you can continue to upload another CSV test file.

Information about the AWS environment:
I have tried to use AWS Lambda, but the unzipped file size should be less than 262.144M. My files are more than 262M because I have 2 large pkl file. One is the vectorizer.pkl which stores the fitted vectorizer and in order to save the memory, I changed the TfidfVectorizer to the HashingVectorizer and it successfully shrank the file size from 70M to 498 bytes. The other one is the model.pkl which stores the trained model. I was wondering if there was a way that I don't need to save these 2 pkl files. What I think is that if I don't save these 2 file, I have to run the train each time I uploaded a new test file, and it would be very slow.
I have switched to AWS EB which doesn't limit the file size. However, I still have to deal with the memory issue because the free instance (t2.micro) I am using has very limited memory size.Please don't upload a file having more than 1800 documents to the service, because you would get a MemoryError.

Github issue:
As I said above, the model.pkl is super large and the Github cannot accept a single file larger than 100M, so I switched to bitbucket. The whole repository is on the bitbucket (https://bitbucket.org/zhuangjiadi/document-classification/src/8914738c6991ace8818fe3b2978bd7f3cc0f6ef3?at=master). I've also uploaded the folder without the model.pkl to the Github (https://github.com/zhuangjiadi/Document-Classification). I'm really curious about ways to solving the large file issues and I would be very appreciated if you could share your thoughts with me.
