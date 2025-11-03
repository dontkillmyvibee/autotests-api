import httpx

login_payload = {
    "email": "user@example.com",
    "password": "user"
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()



client = httpx.Client(
    base_url="http://localhost:8000",
    timeout=100,
    headers={"Authorization": f"Bearer {login_response_data['token']['accessToken']}"},
)

get_get_user_me = client.get("/api/v1/users/me")
get_user_me_data = get_get_user_me.json()
print(f"Status code: {get_get_user_me.status_code}")
print(get_user_me_data)