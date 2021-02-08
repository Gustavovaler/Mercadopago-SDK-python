## Needs requests library 

$ pip install requests

## Basic Usage

```python

# Mercadopago instance
mp = Mercadopago()
    
mp.create_item("title", "description", int(quantity), "currency", float(unit_price))
#you can make all items you want
#or create a dict format item
	
item = {
		"title": "A title",
		"description": "A description for the product",
		"quantity": 1
		"currency": "ARS",
		"unit_price": 100.50
	    }
mp.create_item(item)
	
#also you can create items by list format
	
mp.create_item([item1, item2, ...])
	
```    