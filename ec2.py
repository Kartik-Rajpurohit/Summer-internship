import boto3

# Replace these with your actual credentials and config
AWS_ACCESS_KEY = 'Your Access Key'
AWS_SECRET_KEY = 'Your Secret Key'
REGION = 'ap-south-1'

ec2 = boto3.client(
    'ec2',
    region_name=REGION,
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

try:
    response = ec2.run_instances(
        ImageId='ami-0d9462a653c34dab7',  # Amazon Linux 2 AMI in ap-south-1 (confirm latest)
        InstanceType='t2.micro',
        MinCount=1,
        MaxCount=1,
        KeyName='mykey',           # Your EC2 key pair name
        SecurityGroupIds=['sg-082b710b2e8a15082']  # Your security group ID(s)
    )

    instance_id = response['Instances'][0]['InstanceId']
    print(f"Launched EC2 Instance with ID: {instance_id}")

except Exception as e:
    print("Error launching EC2 instance:", e)
