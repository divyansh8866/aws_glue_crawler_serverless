try:
    import re
    import os
    import json
    import boto3
    import pyodbc
    from boto3.s3.transfer import TransferConfig
    from enum import Enum
    import threading
    import sys
    import math
except Exception as e:
    print("Error : {} ".format(e))


class AWSGlue(object):
    def __init__(self,aws_access_key_id, aws_secret_access_key, region_name):
        self.client = boto3.client(
            "glue",
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name,
        )
    def run_crawler(self, crawler_name=""):
        """Run the Crawlers"""
        try:
            response = self.client.start_crawler(Name=crawler_name)
            response = True
        except Exception as e:
            response = False
            print("Error : {}".format(e))
            print("{} is not running.")
        return response
    def delete_crawler(self, crawler_name=""):
        """Delete the crawler"""
        try:
            response = self.client.delete_crawler(Name=crawler_name)
            response = True
        except Exception as e:
            response = False
            print("Error : {}".format(e))
            print("{} is not deleted.")
        return response
    def get_crawlers(self):
        response = self.client.get_crawlers(
            MaxResults=100,
        )
        return response

        
def main():
    helper =AWSGlue(aws_access_key_id='',
                    aws_secret_access_key="",
                    region_name='us-east-1'
                    )
    resposne = helper.get_crawlers()
    crawlers = [x.get("Name") for x in resposne.get("Crawlers") if "pcomb" in x.get("Name") ]
    for x in crawlers:
        try:
            response = helper.run_crawler(crawler_name=x)
            print(response)
        except Exception as e:
            print("e", e)
