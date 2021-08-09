import boto3
Session= boto3.Session(profile_name="default")
s3= boto3.client('s3')

Buckets= s3.list_buckets()['Buckets']
for each_bucket in Buckets:
    print(each_bucket['Name'])

bucket_Name=input("Enter your bucket name:\n")
response = s3.list_objects(Bucket=bucket_Name)['Contents']
print('Objects in {} are as below\n'.format(bucket_Name))
for each in response:
    print(each['Key'])

