api_response = {
    "first_name": "Prachitosh",
    "age": 28,
    "last_name": "Nayak",
    "email": "Prachitosh@live.com",
    "password": "Test@4321",
    "commission": 10
}
print(api_response)
print(type(api_response))
print(api_response.get('password'))

api_response['password'] = "Linkon"  # mutuable
print(api_response)

for k,v in api_response.items():
    print(k,'-',v)
