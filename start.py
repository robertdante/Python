#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import argparse
import boto3
from botocore.exceptions import ClientError


def get_arguments():
   
    parser = argparse.ArgumentParser("start_stop_ec2.py: \
    Start and stop your EC2 instance.\n")
    parser.add_argument(
        '-s', '--status', help="start/stop instance", type=str, required=True)
    parser.add_argument('-r', '--region',
                        help="Region for instance", type=str, required=True)
    parser.add_argument(
        '-n', '--name', help="Name instance", type=str, required=True)
    args = parser.parse_args()
    return args


def start_ec2(ec2, id):
    print("------------------------------")
    print("Try to start the EC2 instance.")
    print("------------------------------")
    try:
        print("Start dry run...")
        ec2.start_instances(InstanceIds=[id], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
    # Dry run succeeded, run start_instances without dryrun
    try:
        print("Start instance without dry run...")
        response = ec2.start_instances(InstanceIds=[id], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)


def get_instance_id(ec2, instance_name):
    instances = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': [instance_name]
            },
        ],
    )
    first_array = instances["Reservations"]
    first_index = first_array[0]
    instances_dict = first_index["Instances"]
    instances_array = instances_dict[0]
    print(instances_array['InstanceId'])
    return instances_array


def stop_ec2(ec2, id):
    print("------------------------------")
    print("Try to stop the EC2 instance.")
    print("------------------------------")

    try:
        ec2.stop_instances(InstanceIds=[id], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise

    
    try:
        response = ec2.stop_instances(InstanceIds=[id], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)


def get_public_ip(ec2, name):
    print()
    print("Waiting for public IPv4 address...")
    print()
    time.sleep(45)
    instances = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': [name]
            },
        ],
    )
    first_array = instances["Reservations"]
    first_index = first_array[0]
    instances_dict = first_index["Instances"]
    instances_array = instances_dict[0]
    ip_address = instances_array["PublicIpAddress"]
    print()
    print("Public IPv4 address of the EC2 instance: {0}".format(ip_address))
    print()


def main():
    args = get_arguments()
    ec2 = boto3.client('ec2', args.region)
    instance = (get_instance_id(ec2, args.name))
    id = str(instance['InstanceId'])
    if args.status == 'start':
        start_ec2(ec2, id)
        get_public_ip(ec2, args.name)
    else:
        stop_ec2(ec2, id)


if __name__ == '__main__':
    main()