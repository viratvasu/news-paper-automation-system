import requests
# for creating customer
# url = 'http://127.0.0.1:8000/accounts/create/customer'
# data={
#     'email':'c4@gmail.com',
#     'password':'vasuVIRAT*1',
#     'name': 'c4',
#     'doorno':'4444',
#     'colony':'Main Road',
#     'landmarak':'M.P.P.U.P Schools 4',
#     'village':'Chittaluru 4',
#     'mandal':'Chejerla 4',
#     'pincode':'524441',
#     'card_no':'44444444444444',
#     'cvv':'111',
#     'month':'01',
#     'year':'2021',
# }
# response = requests.post(url,data=data)
# print(response.text)
# code for getting token
url_token = 'http://127.0.0.1:8000/api/token/'
data_token = {
    'email':'c4@gmail.com',
    'password':'vasuVIRAT*1'
}
response = requests.post(url_token,data=data_token)
url1='http://127.0.0.1:8000/checkout/'
token=response.text.split(":")[-1][1:-2]
header={'Authorization' : 'Bearer '+token}
# Testing For Customer Subscription model
url = 'http://127.0.0.1:8000/customer/subscription/'
data_add = {
    'title':'Andhra',
    'price':7
}
data_delete = {
    'id':5
}
files = {'image':open('image.png','rb')}
response = requests.delete(url,headers = header,data = data_delete,)
print(response.text)
