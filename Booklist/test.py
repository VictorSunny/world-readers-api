import requests

# dets = {"username": "testuser", "password": "Abcd@1234"}
tk = {"access": "Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM3NTM3Mzc5LCJpYXQiOjE3Mzc1MzcwNzksImp0aSI6ImEwMGFiNTkwMGViMzQ1MzQ4ZjlhMzhmYmZlZDhiZDA3IiwidXNlcl9pZCI6Mn0.gmqD3-f5hlLvQZdsjkB1XlKFR4qZdiGQ4Gi4cFouRzk"}

t = requests.post('http://127.0.0.1:8000/api/user/manager/', json= tk).text
print(t)