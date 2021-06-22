#!/usr/bin/python

import sys
import os
import time
import boto3.ec2

auth = {"aws_access_key_id": "ASIAZJFHE4UKWZRRW4KK", "aws_secret_access_key": "Uurgpvj7XZaV2nfCqvzb9VouI+uzvOrx6xtGLux9"}


def main():
        
    action = sys.argv[1] 
    names = sys.argv[2]
    region = sys.argv[3]
        
        
    if action == "stop":
                
        stopInstance()
        
    elif action == "start":
        
        startInstance()
        
    else:
        print("Choose start or stop")
            

def startInstance():
   
    print("Starting instance...")
    print("====================")

    try:
        ec2 = boto.ec2.connect_to_region("us-east-1", auth)

    except:
        print("Error 1")

      
    try:
        ec2.start_instances(instance_ids="i-0981cc07a384e03a0")

    except:
        print("Error 2")

            
def stopInstance():
        
    print("Stopping instance...")
    print("====================")
        
    try:
        ec2 = boto.ec2.connect_to_region("us-east-1", auth)
        
    except:
        print("Error 3")
    
    
    try:
        ec2.stop_instances(instance_ids="i-0981cc07a384e03a0")
        
    except:
        print("Error 4")
        
if __name__ == '__main__':
    main()        

    
        



    
        
