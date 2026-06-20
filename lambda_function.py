import boto3

def lambda_handler(event, context):

    client = boto3.client('codepipeline')

    response = client.start_pipeline_execution(
        name='AutoDeployBuild'
    )

    return {
        'statusCode': 200,
        'body': 'Pipeline Triggered Successfully'
    }
