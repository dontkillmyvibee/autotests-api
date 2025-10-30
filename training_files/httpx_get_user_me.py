import httpx

login_payload = {
    "email": "user@example.com",
    "password": "user"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)

login_response_json = login_response.json()
login_response_access_token = login_response_json['token']["accessToken"]

get_me_response = httpx.get("http://localhost:8000/api/v1/users/me",
                            headers={"Authorization": f"Bearer {login_response_access_token}"})
get_me_response_json = get_me_response.json()

print(f"User info: {get_me_response_json}")
print(f"Status code: {get_me_response.status_code}")
