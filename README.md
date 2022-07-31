# Serverless Deploy
## AWS Lambda - Docker Image


1. Build the image
```
docker build -t <img-name> .
```
2. Authenticate 
```
aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <aws-id>.dkr.ecr.<region>.amazonaws.com
```

3. Push the image to AWS ECR
```
docker tag <img-name>:<tag> <aws-id>.dkr.ecr.<aws-region>.amazonaws.com/<repo-name>:<tag-aws>
``` 
```
docker push <aws-id>.dkr.ecr.<aws-region>.amazonaws.com/<repo-name>:<tag-aws>
``` 
4. Build the lambda function from the ECR image 

