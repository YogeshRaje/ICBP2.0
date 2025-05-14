import requests
 
API_KEY = "Paste_Your_IBMAPIKEY"
 
token_response = requests.post(
    'https://iam.cloud.ibm.com/identity/token', 
    data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'}
)
mltoken = token_response.json()["access_token"]
 
header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
 
content = "My weight is 91 kg and height is 182 cm . I don't have any allergy. Suggest me the nutrition plan."
role = "user"
 
payload_scoring = {
    "messages": [
        {"content": content, "role": role}
    ]
}
 
response_scoring = requests.post(
    'https://eu-de.ml.cloud.ibm.com/ml/v4/deployments/224b60a0-1a71-44ff-8a09-c6af388d9182/ai_service?version=2021-05-01',
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
