import boto3
import sys


ec2 = boto3.client('ec2')

action = sys.argv[1] 
instances = [sys.argv[2]] if len(sys.argv) > 2 else '.'
#region = sys.argv[3]

def main():
    
        
    if action == "stop":
                
        stopInstance()
        
    elif action == "start":
        
        startInstance()
        
    elif action == "list":
    
        listInstances()
        
    else:
        print("Choose start, stop or list")
        
        
def startInstance():
    ec2.start_instances(InstanceIds=instances)
    print('starting instance...')
    
def stopInstance():
    ec2.stop_instances(InstanceIds=instances)
    print('stopping instance...')
    
def listInstances():
    response = ec2.describe_instances()
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            print(instance["InstanceId"])
            print(instance["State"])
            
    
if __name__ == '__main__':
    main()     

