import os
import json
import boto3

client_session = boto3.Session(
    region_name=os.getenv("AWS_REGION"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("AWS_SECRETE_KEY"),
)


def schedule_event(name=None, schedule_expression=None, action_after_completion="DELETE", **kwargs):
    """
    Function for schedule events on aws event bridge.
    """
    try:
        scheduler = client_session.client("scheduler")
        schedule_request = scheduler.create_schedule(
            ActionAfterCompletion=action_after_completion,
            FlexibleTimeWindow={
                'Mode': 'OFF'
            },
            Name=name,
            ScheduleExpression=schedule_expression,
            ScheduleExpressionTimezone="America/New_York",
            State='ENABLED',
            Target={
                'Arn': os.getenv("AWS_LAMBDA_ARN"),
                'Input': json.dumps({
                    'url': os.getenv("NOTIFICATION_API"),
                    'api_key': os.getenv("API_KEY"),
                    'product_url': kwargs.get("product_url", None),
                    'new_release_scheduler': False,
                    'new_notification_scheduler': True,
                    'notification_type': kwargs.get("notification_type"),
                    'notification_id': str(name),
                }),
                'RetryPolicy': {
                    'MaximumEventAgeInSeconds': 123,
                    'MaximumRetryAttempts': 123
                },
                'RoleArn': os.getenv("AWS_ROLE_ARN"),
            }
        )

        return json.loads(schedule_request.text)

    except BaseException as e:
        print(e)
