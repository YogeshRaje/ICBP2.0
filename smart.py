import requests
 
API_KEY = "zdu6lVZjlevjdKW0x0SRTmDOrnYvAfA-lf-cq4ehalW1"
 
token_response = requests.post(
    'https://iam.cloud.ibm.com/identity/token', 
    data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'}
)
mltoken = token_response.json()["access_token"]
 
header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
 
content = "Give me 2 days veg diet plan."
role = "user"
 
payload_scoring = {
    "messages": [
        {"content": content, "role": role}
    ]
}
 
response_scoring = requests.post(
    'https://eu-de.ml.cloud.ibm.com/ml/v4/deployments/d1b177f7-8823-4cc4-a936-6d3fbe1237ec/ai_service?version=2021-05-01',
    json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken}
)
 
print("Scoring response")
try:
    print(response_scoring.json())
except ValueError:
    print(response_scoring.text)
except Exception as e:
    print(f"An unexpected error occurred: {e}")