import boto3
import sys


ec2 = boto3.client('ec2')

#instances = ['i-0981cc07a384e03a0']
action = sys.argv[1] 
instances = [sys.argv[2]]
region = sys.argv[3]

def main():
        
    if action == "stop":
                
        stopInstance()
        
    elif action == "start":
        
        startInstance()
        
    else:
        print("Choose start or stop")
        
        
def startInstance():
    ec2.start_instances(InstanceIds=instances)
    print('starting...')
    
def stopInstance():
    ec2.stop_instances(InstanceIds=instances)
    print('stopping...')
    
if __name__ == '__main__':
    main()     

