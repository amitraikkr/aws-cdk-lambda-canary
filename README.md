# AWS CDK Lambda Canary Deployment Stack

This project demonstrates how to create a serverless application stack using AWS Cloud Development Kit (CDK) with a focus on implementing a canary deployment strategy for AWS Lambda functions. The stack includes a Lambda function, an API Gateway to expose the Lambda function, CloudWatch Alarms to monitor the function, and a CodeDeploy deployment group to manage the deployment process.

## Features

- **AWS Lambda**: A Lambda function is defined to handle backend logic. It uses Python 3.11 runtime and supports versioning and aliases.
- **API Gateway**: A RESTful API is created as a front to the Lambda function, making it accessible via HTTP.
- **CloudWatch Alarm**: Monitors the Lambda function for errors. If errors exceed a threshold, it triggers alarms.
- **CodeDeploy Canary Deployment**: Deploys new versions of the Lambda function gradually to a subset of users before full deployment, using the canary deployment strategy.

## Project Structure

- `lambda/`: This directory contains the Lambda function code. The handler defined in the function is `handler.lambda_handler`.
- `lib/aws_cdk_lambda_canary_stack.py`: Defines the CDK stack, including the Lambda function, API Gateway, CloudWatch Alarm, and CodeDeploy deployment group.

## Getting Started

### Prerequisites

- AWS CLI: Configure your AWS credentials using the AWS CLI.
- AWS CDK: Install the AWS CDK Toolkit globally via npm: `npm install -g aws-cdk`.
- Python 3.x: Ensure Python 3.11 or later is installed along with `pip`.

### Setup

1. **Clone the repository**:

```bash
git clone https://github.com/your-github-username/aws-cdk-lambda-canary.git
cd aws-cdk-lambda-canary
