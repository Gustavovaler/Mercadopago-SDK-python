from mercadopago import MercadoPago

access_token = 'ACCESS TOKEN'       
mp = MercadoPago(access_token)
items = [
            {
                "title": "Remera de mujer",
                "description": "Remera modelo clasico manga corta",
                "quantity": 3,
                "currency_id": "ARS",
                "unit_price": 10.0
            },
            {
                "title": "Remera de Hombre",
                "description": "Remera modelo clasico manga corta",
                "quantity": 2,
                "currency_id": "ARS",
                "unit_price": 120
            }
        ]

item1 = mp.create_item("remera de mujer"," Remera manga corta de mjer", 3, "ARS", 500)
item2 = mp.create_item("remera de hombre"," Remera manga corta de hombre", 1, "ARS", 280)

mp.set_back_urls("https://some.com/success", "http://some.com/failure", "https://some.com/pending")

# item = {
#                 "title": "Remera de mujer",
#                 "description": "Remera modelo clasico manga corta",
#                 "quantity": 3,
#                 "currency_id": "ARS",
#                 "unit_price": 10.0
#             }

preference = mp.create_preference([item1,item2])


print(preference)
print(preference['init_point'])
try:
    print(preference['id'])
except:
    print()

