import httpx
from tools.fakers import get_random_email

base_url = "http://localhost:8000"

create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = httpx.post(f"{base_url}/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
print(f"Status code: {create_user_response.status_code}")

login_user_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}

login_response = httpx.post(f"{base_url}/api/v1/authentication/login", json=login_user_payload)
login_response_data = login_response.json()
print(f"Status code: {login_response.status_code}")

update_user_payload = {
    "email": get_random_email(),
    "lastName": "updated",
    "firstName": "updated",
    "middleName": "updated"
}

update_user_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}

update_user_response = httpx.patch(f"{base_url}/api/v1/users/{create_user_response_data['user']['id']}",
                                 json=update_user_payload, headers=update_user_headers)
print(f"Status code: {update_user_response.status_code}")
