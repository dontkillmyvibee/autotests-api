# import httpx
#
# # response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
# #
# # print(response.status_code)
# # print(response.json())
# #
# # data = {
# #     "title": "Новая задача",
# #     "completed": False,
# #     "userId": 1
# # }
# #
# # response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)
# # print(response.status_code)
# # print(response.json())
# #
# # data = {"username": "test_user", "password": "123456"}
# # response = httpx.post("https://httpbin.org/post", data=data)
# # print(response.json())
#
# # headers = {
# #     "Authorization": "Bearer test_token"
# # }
# # response = httpx.get("https://httpbin.org/get", headers=headers)
# # print(response.json())
# # print(response.request.headers)
# #
# # response = httpx.get("https://jsonplaceholder.typicode.com/todos?userId=1")
# #
# # print(response.json())
# # print(response.url)
#
# # files = {"file": ("ex.txt", open("ex.txt", "rb"))}
# # response = httpx.post("https://httpbin.org/post", files=files)
# #
# # print(response.json())
#
# # with httpx.Client() as client:
# #     response = client.get("https://httpbin.org/get")
# #     print(response.json())
#
# # client = httpx.Client(headers={"Authorization": "Bearer sdfghjkl"})
# # response = client.get("https://httpbin.org/get")
# # print(response.json())
#
# try:
#     response = httpx.get("https://jsonplaceholder.typicode.com/todos/invallls")
#     response.raise_for_status()
# except httpx.HTTPError as e:
#     print(f'Ошибка в запросе: {e}')
#
#
# try:
#     response = httpx.get("https://jsonplaceholder.typicode.com/delay5", timeout=2)
# except httpx.ReadTimeout as e:
#     print("Запрос превысил лимит ожидания")