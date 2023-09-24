
import requests

def signup(account_data):
    signup_endpoint = "http://127.0.0.1:8000/auth/users/"
    res = requests.post(signup_endpoint, account_data)
    print(res)


def login(login_credentials):
    endpoint = "http://127.0.0.1:8000/auth/token/login/"
    res = requests.post(endpoint, login_credentials)
    print(res.status_code)
    if res.status_code == 200:
        auth_token = res.json()['auth_token']
        return auth_token
        

def client(auth_token, endpoint):
    headers = {"Authorization": f"Token {auth_token}"}
    res = requests.get(endpoint, headers=headers)
    if res.status_code == 200:
        return res.json()

if __name__ == "__main__":
    # # Login
    # login_credentials = {
    #     "username": "admin",
    #     "password": "admin"
    #     }
    # auth_token = login(login_credentials=login_credentials)
    
    # endpoint = "http://127.0.0.1:8000/api/v1/post/"
    # res = client(auth_token=auth_token, endpoint=endpoint)
    # print(res)
    
    # # Signup
    # account_data = {
    #     "username":"user1",
    #     "password":"my-user-pass",
    #     "re_password":"my-user-pass",
    # }
    # signup(account_data)
    pass