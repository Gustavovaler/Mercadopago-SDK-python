## Needs requests library 

$ pip install requests

## Basic Usage

```python

from mercadopago import Mercadopago

# Mercadopago instance
mp = Mercadopago()
    
mp.create_item("title", "description", int(quantity), "currency", float(unit_price))
#you can make all items you want
#or create a dict format item
	
item = {
	"title": "A title",
	"description": "A description for the product",
	"quantity": 1,
	"currency": "ARS",
	"unit_price": 100.50
	}
mp.create_item(item)
	
#also you can create items by list format
	
mp.create_item([item1, item2, ...])

# create and send the preference

preference = mp.create_preference([item1,item2])

#now you can send to your view the init_point 
# to finish your transaction 

init_point = preference['init_point']
	
```    