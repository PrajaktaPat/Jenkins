import boto3
Session= boto3.Session(profile_name="default")
ec2_client= Session.client(service_name="ec2",region_name='ap-south-1')
sns_client = boto3.client('sns',region_name='ap-south-1')
sns_arn = 'arn:aws:sns:ap-south-1:218785759345:mfa'
email_body=[]
response= ec2_client.describe_security_groups()['SecurityGroups']
for each_SG in response:
    for each_security in each_SG['IpPermissionsEgress']:
        for each in each_security['IpRanges']:
            if each['CidrIp'] == '0.0.0.0/0':
                email_body.append(each_SG['GroupName'])
                #print("{} security group is not secure".format(each_SG['GroupName']))
str1='\n'.join(email_body)
str2= 'Hi Team, \n Please find below non complaint security groups \n'
str= str2+str1
response_sns=sns_client.publish(TopicArn=sns_arn,Message=str)
print(response_sns)