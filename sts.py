import boto3
Session= boto3.Session(profile_name="default")
sts_client= Session.client(service_name="sts",region_name="us-east-1")
iam_client= Session.client(service_name="iam")
sns_client = boto3.client('sns',region_name='ap-south-1')
sns_arn = 'arn:aws:sns:ap-south-1:218785759345:mfa'
iam_users=[]
email_body=[]
all_users=iam_client.list_users()['Users']
for each_user in all_users:
    #print(each_user['UserName'])
    response= iam_client.list_mfa_devices(UserName=each_user['UserName'])['MFADevices']
    if len(response) == 0:
        print(each_user['UserName'])
        #email = "Below users are not having MFA enabled :,{}".format(each_user['UserName'])
        email_body.append(each_user['UserName'])
print(email_body)
str1='\n'.join(email_body)
str2= 'Hi Team, \n Please find below users who are not having MFA enabled\n'
str= str2+str1
response=sns_client.publish(TopicArn=sns_arn,Message=str)


