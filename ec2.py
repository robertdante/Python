import boto3
import sys


ec2 = boto3.client('ec2')

#instances = ['i-0981cc07a384e03a0']
action = sys.argv[1] 
instances = [sys.argv[2]]
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
    print('starting...')
    
def stopInstance():
    ec2.stop_instances(InstanceIds=instances)
    print('stopping...')
    
def listInstances():
    response = ec2.describe_instances()
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            print(instance["InstanceId"])
    
if __name__ == '__main__':
    main()     

