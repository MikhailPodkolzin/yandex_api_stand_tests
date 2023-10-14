import configuration
import requests
import data
def post_products_kits(product_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
    json=product_ids,
    headers=data.headers)
response = post_products_kits(data.product_ids);
print(response.status_code)
print(response.json())

def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
    json=user_body,
    headers=data.headers)
response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)
    response = get_users_table()
    print(response.status_code)