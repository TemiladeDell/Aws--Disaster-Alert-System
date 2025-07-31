

**Disaster Alert System – AWS Cloud Project**
This is a real-time, serverless alert system that fetches live weather data and sends notifications when extreme weather conditions like storms or heavy rain are detected.



**Tools and Technologies Used**
1.Programming & Scripting
1b.Python (Lambda function logic)

2.Bash (project automation and CLI commands)

3.JSON (IAM policy documents and API responses)

4.Development Environment
4b.Ubuntu via Windows Subsystem for Linux (WSL)

5.Virtual Environment (venv) for Python dependency isolation

6.nano (for editing scripts and policy files)

7.zip (for packaging Lambda deployment)

8.AWS Services
8b.AWS Lambda – runs the Python code serverlessly

9.Amazon SNS (Simple Notification Service) – sends email alerts

10.Amazon EventBridge – schedules Lambda execution every 10 minutes

11.IAM (Identity and Access Management) – manages roles and permissions

12.AWS CLI
12b.Used extensively for:

13.Creating and deploying the Lambda function

14.Creating SNS topics and subscriptions

15.Creating EventBridge rules and targets

16.Attaching policies and setting permissions



**Third-Party API**
OpenWeatherMap API – provides real-time weather data



**Project Overview**
A Lambda function fetches weather data from the OpenWeatherMap API every 10 minutes.

If the weather description includes keywords like “storm,” “rain,” or “extreme,” it triggers an SNS email notification.

The system is fully automated and serverless, requiring no manual monitoring or EC2 instances.



**How It Was Built**
1.The project was developed using the AWS CLI, Bash, and Python within a Linux environment (Ubuntu via WSL). Key steps included:

2.Writing lambda_function.py for disaster detection and alerting.

3.Packaging the function using zip and deploying it via the AWS CLI.

4.Creating an SNS topic, subscribing an email address, and verifying it.

5.Creating an IAM role with permissions for Lambda to publish to SNS.

6.Writing and attaching a custom inline policy (sns-policy.json) using CLI.

7.Setting up a CloudWatch rule (via EventBridge) to schedule the Lambda function every 10 minutes.

8.Granting EventBridge permission to invoke the Lambda.

9.Testing end-to-end functionality and troubleshooting issues like:

10.Lambda not authorized to publish to SNS

11.Syntax errors in the Python code

12.EventBridge not triggering the function



**Usage Notes**
This project is for educational and demonstration purposes. API keys and sensitive data are excluded. You’ll need to:

Replace the placeholder API key and SNS topic ARN in the Lambda code

Ensure your IAM policies and roles are correctly configured

Disable or delete the EventBridge rule when testing is complete to avoid unnecessary charges



**Author**
Temilade
[LinkedIn](www.linkedin.com/in/temilade-akinyimika-dell001) | [Medium Post](https://medium.com/@temiladedell/aws-cloud-project-part-1-building-a-real-time-disaster-notification-system-6407b4d6b69b)

