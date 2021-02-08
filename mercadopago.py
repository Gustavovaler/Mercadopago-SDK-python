import json
from version import Version
try:
    import requests
except  ImportError as e:
    print(e)
    
class  MercadoPago:
    
    def __init__(self, access_token):
        self.access_token = access_token
        self.bearer = "Bearer "+ self.access_token
        print(Version.get_version())  
    
    def generate_preference(self, items):
        preference_data = {
            "headers" : {
                        "Content-Type": "application/json",
                        "Authorization": ""
                        },
            "data":{
                "items": [],
                    }            
        }
        
        try:
            preference_data["data"]["auto_return"] = self.auto_return
            preference_data["data"]["back_urls"] = {
                "failure":self.failure_url,
                "pending":self.pending_url,
                "success":self.success_url
                }
        except:
            preference_data["data"]["auto_return"] = ""
            preference_data["data"]["back_urls"] = {
                "failure":"",
                "pending":"",
                "success":""
            }   
        try:
            preference_data["data"]["payer"] = self.payer
            print("agregado al data")
        except:
             preference_data["data"]["payer"] = {}
            
        preference_data["headers"]["Authorization"] = "Bearer "+self.access_token
        if isinstance(items, list):
            preference_data["data"]["items"] = items
        else:
            preference_data["data"]["items"].append(items)
        
        return preference_data
    
    
    def create_item(self, title, description, quantity,currency_id, unit_price):
        item = {"title": title, 
                "description": description,
                "quantity": quantity ,
                "currency_id":currency_id,
                "unit_price": unit_price,
                "picture_url": "https://www.mercadopago.com/org-img/MP3/home/logomp3.gif",
                }
        return item
    
    def create_preference(self,  items):
        self.base_url = "https://api.mercadopago.com"
        self.preference_data = self.generate_preference(items)
        url = self.base_url+"/checkout/preferences"
        response = requests.post(url,data=json.dumps(self.preference_data["data"]), headers=self.preference_data["headers"])
        response_json = json.loads(response.text)
        return response_json
    
    def set_back_urls(self, success = None, failure = None, pending = None , auto_return = "approved"):
        try:
            self.success_url = success
            self.failure_url = failure
            self.pending_url = pending
            self.auto_return = auto_return
            return True
        except:
            return False
        
    def create_payer(self, payer):
        try:
            self.payer = payer
            return True
        except:
            return False
        
        
    
