import boto3
import uuid
from server import app

dynamo_client = boto3.resource('dynamodb',
                    aws_access_key_id = app.config['aws_access_key'],aws_secret_access_key=app.config['aws_secret'],
                    region_name='us-east-1')
dynamo_table = dynamo_client.Table('phonebook')

def get_items():
    response = dynamo_table.scan()
    return response['Items']

def create_item(newObject):
    return dynamo_table.put_item(
        Item = {
            'id': str(uuid.uuid4()),
            'name': newObject["name"],
            'number': newObject["number"]
        }
    )

def delete_item(id):

    return dynamo_table.delete_item(
        Key={
            'id': id
        }
    )  

def update_item(id,updateObject):
    return dynamo_table.update_item(
        Key={
           'id': id
        },
        UpdateExpression="SET #attr = :num",
        ExpressionAttributeNames={'#attr':'number'},
        ExpressionAttributeValues={
        ':num': updateObject['number']
        },
        
        ReturnValues="UPDATED_NEW"
    )      
    
