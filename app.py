#!/usr/bin/env python3
import os

import aws_cdk as cdk
from aws_cdk import Environment

from aws_cdk_lambda_canary.aws_cdk_lambda_canary_stack import AwsCdkLambdaCanaryStack


app = cdk.App()

environment_type = app.node.try_get_context("environmentType")
environment_context = app.node.try_get_context(environment_type)

if environment_context is not None:
    region = environment_context["region"]
else:
    region = "us-east-2"
account = app.node.try_get_context("account")

if environment_context is not None:
    tags = environment_context["tags"]
else:
    tags={"Environment": "TEST"}

stack_name = f'{app.node.try_get_context("prefix")}-{environment_type}'

AwsCdkLambdaCanaryStack(
        app, 
        stack_name,
        env = Environment(
            account = account,
            region = region
        ),
        tags=tags,
    )

app.synth()
