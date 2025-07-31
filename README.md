Disaster Alert System – AWS Cloud Project
This is a real-time, serverless alert system that fetches live weather data and sends notifications when extreme weather conditions like storms or heavy rain are detected.

Tools and Technologies Used
Programming & Scripting
Python (Lambda function logic)

Bash (project automation and CLI commands)

JSON (IAM policy documents and API responses)

Development Environment
Ubuntu via Windows Subsystem for Linux (WSL)

Virtual Environment (venv) for Python dependency isolation

nano (for editing scripts and policy files)

zip (for packaging Lambda deployment)

AWS Services
AWS Lambda – runs the Python code serverlessly

Amazon SNS (Simple Notification Service) – sends email alerts

Amazon EventBridge – schedules Lambda execution every 10 minutes

IAM (Identity and Access Management) – manages roles and permissions

AWS CLI
Used extensively for:

Creating and deploying the Lambda function

Creating SNS topics and subscriptions

Creating EventBridge rules and targets

Attaching policies and setting permissions

Third-Party API
OpenWeatherMap API – provides real-time weather data

Project Overview
A Lambda function fetches weather data from the OpenWeatherMap API every 10 minutes.

If the weather description includes keywords like “storm,” “rain,” or “extreme,” it triggers an SNS email notification.

The system is fully automated and serverless, requiring no manual monitoring or EC2 instances.

How It Was Built
The project was developed using the AWS CLI, Bash, and Python within a Linux environment (Ubuntu via WSL). Key steps included:

Writing lambda_function.py for disaster detection and alerting.

Packaging the function using zip and deploying it via the AWS CLI.

Creating an SNS topic, subscribing an email address, and verifying it.

Creating an IAM role with permissions for Lambda to publish to SNS.

Writing and attaching a custom inline policy (sns-policy.json) using CLI.

Setting up a CloudWatch rule (via EventBridge) to schedule the Lambda function every 10 minutes.

Granting EventBridge permission to invoke the Lambda.

Testing end-to-end functionality and troubleshooting issues like:

Lambda not authorized to publish to SNS

Syntax errors in the Python code

EventBridge not triggering the function

Usage Notes
This project is for educational and demonstration purposes. API keys and sensitive data are excluded. You’ll need to:

Replace the placeholder API key and SNS topic ARN in the Lambda code

Ensure your IAM policies and roles are correctly configured

Disable or delete the EventBridge rule when testing is complete to avoid unnecessary charges

Author
Temilade
[LinkedIn](www.linkedin.com/in/temilade-akinyimika-dell001) | Medium Post

