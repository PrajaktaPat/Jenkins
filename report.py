import boto3
from pprint import pprint
Session= boto3.Session(profile_name="default",region_name='us-east-1')
ec2_client= Session.client(service_name="ec2")
import pandas as pd

instances=ec2_client.describe_instances()['Reservations']
for each in instances:
    for each in each['Instances']:
        volumes = ec2_client.describe_volumes(
            Filters=[{'Name': 'attachment.instance-id', 'Values': [each['InstanceId']]}])
        for disk in volumes['Volumes']:
            print("VolumeID: ",disk['VolumeId'])
            print("VolumeType: ", disk['VolumeType'])
            print("VolumeSize(in GB): ", disk['Size'])
        print("InstanceID: ", each['InstanceId'])
        print("InstanceType: ", each['InstanceType'])
        print("KeyName: ", each['KeyName'])
        print("State: ", each['State']['Name'])
        for each in each['Tags']:
            print("{}:".format(each['Key']),each['Value'])
        print("************************************************************")



#pprint(instances)
