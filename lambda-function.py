import json
import requests
import boto3

def lambda_handler(event, context):
	API_KEY = "a0da05df5a31fac16992bd7f7fd2937b"
	CITY = "Lagos"
	URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"

	response = requests.get(URL)
	weather_data = response.json()


	if 'weather' in weather_data:
		description = weather_data['weather'][0]['description']
		if 'storm' in description or 'rain' in description or 'extreme' in description:
			sns = boto3.client('sns')
			sns.publish(
				TopicArn ='arn:aws:sns:us-east-1:274603885640:disaster-alert-topic',
				Message = f"Weather alert for {CITY}: {description}",
				Subject = 'Disaster Alert System'
			)
	return {
		'statusCode':  200,
		'body':json.dumps('Function executed successfully')

	}

if __name__ == "__main__":
	print(lambda_handler({}, {}))
