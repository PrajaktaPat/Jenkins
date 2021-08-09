import boto3
session = boto3.Session(profile_name="default", region_name='us-east-1')
sns_client = boto3.client('sns',region_name='us-east-1')
client = boto3.client('ec2')
Ec2_client = session.client(service_name='ec2')
volumes = Ec2_client.describe_volumes()
all_regions = client.describe_regions()
sns_arn = 'arn:aws:sns:us-east-1:624746494870:abcd'
list_of_regions= []
unused_vols = []
email_body=[]
for each_reg in all_regions['Regions']:
    list_of_regions.append(each_reg['RegionName'])
#print(list_of_regions)
for each_reg in list_of_regions:
	session = boto3.Session(profile_name="default", region_name=each_reg)
	resource = session.client(service_name='ec2')
	volumes = resource.describe_volumes()
	print("list of unused volumes in",each_reg,"is:")
	#print(volumes)
	for each_volume in volumes['Volumes']:
		if each_volume['State']== 'available':
			unused_vols.append(each_volume['VolumeId'])
			#print()
		#,unused_vols)#each_volume['VolumeId'])
			print(unused_vols)
			if len(unused_vols) != 0:
				for each_vols in unused_vols:
					email = "Unused Volumes: VolumeId= {},{}".format(each_vols,each_reg)
				email_body.append(email)
print(email_body)
str=','.join(email_body)
response=sns_client.publish(TopicArn=sns_arn,Message=str)
