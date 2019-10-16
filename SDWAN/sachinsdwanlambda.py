# -*- coding: utf-8 -*-
import random
import logging
import botocore.vendored.requests as requests
import requests

 
from typing import Union, List

from ask_sdk.standard import StandardSkillBuilder
from ask_sdk_core.dispatch_components import (
    AbstractRequestHandler, AbstractExceptionHandler,
    AbstractRequestInterceptor, AbstractResponseInterceptor)
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.utils import is_request_type, is_intent_name

from ask_sdk_model.services.monetization import (
    EntitledState, PurchasableState, InSkillProductsResponse, Error,
    InSkillProduct)
from ask_sdk_model.interfaces.monetization.v1 import PurchaseResult
from ask_sdk_model import Response, IntentRequest
from ask_sdk_model.interfaces.connections import SendRequestDirective

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Data for the skill

# Static list of facts across 3 categories that serve as
# the free and premium content served by the Skill
all_facts = [
    {
        "type": "science",
        "fact": "The current status of NSO is:"
    }
]

skill_name = "infinity labs"

#Utility functions

def get_all_entitled_products(in_skill_product_list):
    """Get list of in-skill products in ENTITLED state."""
    # type: (List[InSkillProduct]) -> List[InSkillProduct]
    entitled_product_list = [
        l for l in in_skill_product_list if (
                l.entitled == EntitledState.ENTITLED)]
    return entitled_product_list

def get_random_from_list(facts):
    """Return the fact message from randomly chosen list element."""
    # type: (List) -> str
    fact_item = random.choice(facts)
    return fact_item.get("fact")

def get_random_yes_no_question():
    """Return random question for YES/NO answering."""
    # type: () -> str
    questions = [
        "Do you want to know about current available automation packages, devices, VPN Or You want to create new vpn service.......?"
        ]
    return random.choice(questions)

def get_random_goodbye():
    """Return random goodbye message."""
    # type: () -> str
    goodbyes = ["OK.  Goodbye!", "Have a great day!", "Come back again soon!"]
    return random.choice(goodbyes)

def get_speakable_list_of_products(entitled_products_list):
    """Return product list in speakable form."""
    # type: (List[InSkillProduct]) -> str
    product_names = [item.name for item in entitled_products_list]
    if len(product_names) > 1:
        # If more than one, add and 'and' in the end
        speech = " and ".join(
            [", ".join(product_names[:-1]), product_names[-1]])
    else:
        # If one or none, then return the list content in a string
        speech = ", ".join(product_names)
    return speech

def get_resolved_value(request, slot_name):
    """Resolve the slot name from the request using resolutions."""
    # type: (IntentRequest, str) -> Union[str, None]
    try:
        return (request.intent.slots[slot_name].resolutions.
                resolutions_per_authority[0].values[0].value.name)
    except (AttributeError, ValueError, KeyError, IndexError):
        return None

def get_spoken_value(request, slot_name):
    """Resolve the slot to the spoken value."""
    # type: (IntentRequest, str) -> Union[str, None]
    try:
        return request.intent.slots[slot_name].value
    except (AttributeError, ValueError, KeyError, IndexError):
        return None

def is_product(product):
    """Is the product list not empty."""
    # type: (List) -> bool
    return bool(product)

def is_entitled(product):
    """Is the product in ENTITLED state."""
    # type: (List) -> bool
    return (is_product(product) and
            product[0].entitled == EntitledState.ENTITLED)

def in_skill_product_response(handler_input):
    """Get the In-skill product response from monetization service."""
    # type: (HandlerInput) -> Union[InSkillProductsResponse, Error]
    locale = handler_input.request_envelope.request.locale
    ms = handler_input.service_client_factory.get_monetization_service()
    return ms.get_in_skill_products(locale)
    


# def get_all_entitled_products(in_skill_product_list):
#     """Get list of in-skill products in ENTITLED state."""
#     # type: (List[InSkillProduct]) -> List[InSkillProduct]
#     entitled_product_list = [ l for l in in_skill_product_list if (l.entitled == EntitledState.ENTITLED)]
#     return entitled_product_list

# def get_random_from_list(facts):
#     """Return the fact message from randomly chosen list element."""
#     # type: (List) -> str
#     fact_item = random.choice(facts)
#     return fact_item.get("fact")

# def get_random_yes_no_question():
#     """Return random question for YES/NO answering."""
#     # type: () -> str
#     questions = [
#         "Do you want to know about current available automation packages, devices, VPN Or You want to create new vpn service.......?"
#         ]
#     return random.choice(questions)
        
###################################################################################################################################



def get_random_config():
    """Return random config message."""
    # type: () -> str
    questions = [
        "Do you want to know more about NSO ?"
        ]
    return random.choice(questions)

def get_random_configure():
    """Return random config message."""
    # type: () -> str
    questions = [
        "Do you want to know more about NSO ?"
        ]
    return random.choice(questions)

def get_random_configs():
    """Return random config message."""
    # type: () -> str
    questions = [
        "Do you want to know more about NSO?"
        ]
    return random.choice(questions)
    
def get_random_configsz():
    """Return random config message."""
    # type: () -> str
    questions = [
        " "
        ]
    return random.choice(questions)    
    
def get_random_configz():
    """Return random config message."""
    # type: () -> str
    questions = [
        ""
        ]
    return random.choice(questions)

    
##############################################################################################

##########################      SDDEV functions   #########################################

###############################################################################################



# SD DEV DEVICE INFO

def sddevdevice_info():
    import requests
    import time
    import json
    response = requests.post("http://sddev.infinitylabs.in/api/login/", headers={"Content-Type": "application/x-www-form-urlencoded"}, data = "username=admin&password=admin@123")
    res = response.json()
    x = json.dumps(res)
    db = json.loads(x)
    y=db["token"]
    xyz= 'Bearer '+y
    code = requests.get("http://sddev.infinitylabs.in/api/devices", headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz}, timeout = 60)
    v=code.json()
    i=v['data']
    g = json.dumps(i)
    db = json.loads(g)
    items = []
    for item in db:
        items.append(item['name'])
    return "Current active devices are", items
print(sddevdevice_info())


# # DEVICE COUNT

def device_count():
    import requests
    import time
    import json
    response = requests.post("http://sddev.infinitylabs.in/api/login/", headers={"Content-Type": "application/x-www-form-urlencoded"}, data = "username=admin&password=admin@123")
    res = response.json()
    x = json.dumps(res)
    db = json.loads(x)
    y=db["token"]
    xyz= 'Bearer '+y
    code = requests.get("http://sddev.infinitylabs.in/api/devices", headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz}, timeout = 60)
    v=code.json()
    i=v['data']
    g = json.dumps(i)
    db = json.loads(g)
    items = []
    return "running device count is", len(db)
print(device_count())



# SDDEV SITES INFO

def sddevsites_info():
    import requests
    import time
    import json
    response = requests.post("http://sddev.infinitylabs.in/api/login/", headers={"Content-Type": "application/x-www-form-urlencoded"}, data = "username=admin&password=admin@123")
    res = response.json()
    x = json.dumps(res)
    db = json.loads(x)
    y=db["token"]
    xyz= 'Bearer '+y
    code = requests.get("http://sddev.infinitylabs.in/api/sites", headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz}, timeout = 60)
    v=code.json()
    i=v['data']
    g = json.dumps(i)
    db = json.loads(g)
    items = []
    for item in db:
        items.append(item['name'])
    return "Current active sites are", items
print(sddevsites_info())





# ### SITES COUNT



def sites_count():
    import requests
    import time
    import json
    response = requests.post("http://sddev.infinitylabs.in/api/login/", headers={"Content-Type": "application/x-www-form-urlencoded"}, data = "username=admin&password=admin@123")
    res = response.json()
    x = json.dumps(res)
    db = json.loads(x)
    y=db["token"]
    xyz= 'Bearer '+y
    code = requests.get("http://sddev.infinitylabs.in/api/sites", headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz}, timeout = 60)
    v=code.json()
    i=v['data']
    g = json.dumps(i)
    db = json.loads(g)
    return "running sites count is", len(db)
print(sites_count())



# # SDDEV PLID INFO

def sddevpid_count():
    
    import requests
    import time
    import json
    response = requests.post("http://sddev.infinitylabs.in/api/login/", headers={"Content-Type": "application/x-www-form-urlencoded"}, data = "username=admin&password=admin@123")
    res = response.json()
    x = json.dumps(res)
    indexY = 0
    db = json.loads(x)
    y=db["token"]
    xyz= 'Bearer '+y
    code = requests.get("http://sddev.infinitylabs.in/api/licenses", headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz}, timeout = 60)
    v=code.json()
    i=v['data']
    g = json.dumps(i)
    db = json.loads(g)
    #print(len(db['data'][0]['plid']
    items = []
    for item in db:
        items.append(item['plid'])
        indexY= indexY + 1
        
        
    return "my purchased licenses are", indexY
    return "Current running pid are", x
    #print(len(db['data'][0]['plid']
    #print(len(db['data'][0]['plid'])
#print(indexY)
#print(sddevdevice_info())
x= sddevpid_count()
print(x)



# # ### SDDEV USER INFO



def sddevuser_count():
    
    import requests
    import time
    import json
    response = requests.post("http://sddev.infinitylabs.in/api/login/", headers={"Content-Type": "application/x-www-form-urlencoded"}, data = "username=admin&password=admin@123")
    res = response.json()
    x = json.dumps(res)
    indexY = 0
    db = json.loads(x)
    y=db["token"]
    xyz= 'Bearer '+y
    code = requests.get("http://sddev.infinitylabs.in/api/users/0", headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz}, timeout = 60)
    v=code.json()
    i=v['data']
    g = json.dumps(i)
    db = json.loads(g)
    #print(len(db['data'][0]['plid']
    items = []
    for item in db:
        items.append(item['username'])
        indexY= indexY + 1
        
        
    #return "current active users are", indexY
    return "Current running users are", indexY
    #print(len(db['data'][0]['plid']
    #print(len(db['data'][0]['plid'])
#print(indexY)
#print(sddevdevice_info())
#x= sddevuser_count()
print(sddevuser_count())


### SDDEV INTERFACE INFO

def sddevinterface_info():
    import requests
    import time
    import json
    response = requests.post("http://sddev.infinitylabs.in/api/login/", headers={"Content-Type": "application/x-www-form-urlencoded"}, data = "username=admin&password=admin@123")
    res = response.json()
    x = json.dumps(res)
    db = json.loads(x)
    y=db["token"]
    xyz= 'Bearer '+y
    code = requests.get("http://sddev.infinitylabs.in/api/licenses/purchase", headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz}, timeout = 60)
    v=code.json()
    i=v['data']
    j=i[0]['Plan']
   
    #print(j)
    return "Current active interfaces are", j
print(sddevinterface_info())


### SDDEV ACTIVE LICENSE

def sddevactivelicense_count():
    
    import requests
    import time
    import json
    response = requests.post("http://sddev.infinitylabs.in/api/login/", headers={"Content-Type": "application/x-www-form-urlencoded"}, data = "username=admin&password=admin@123")
    res = response.json()
    x = json.dumps(res)
    indexY = 0
    db = json.loads(x)
    y=db["token"]
    xyz= 'Bearer '+y
    code = requests.get("http://sddev.infinitylabs.in/api/licenses", headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz}, timeout = 60)
    v=code.json()
    i=v['data']
    g = json.dumps(i)
    db = json.loads(g)
    #print(len(db['data'][0]['plid']
    items = []
    for item in db:
        if item['license']['isActive'] :
            indexY= indexY + 1
        
        
    #return indexY
    return "Current Active licenses are", indexY
    #print(len(db['data'][0]['plid']
    #print(len(db['data'][0]['plid'])
#print(indexY)
#print(sddevdevice_info())
x= sddevactivelicense_count()
print(x)



### SDDEV DEVICE DETAILS

def sddevdevicedetail_info():
    import requests
    import time
    import json
    response = requests.post("http://sddev.infinitylabs.in/api/login/", headers={"Content-Type": "application/x-www-form-urlencoded"}, data = "username=admin&password=admin@123")
    res = response.json()
    x = json.dumps(res)
    db = json.loads(x)
    y=db["token"]
    xyz= 'Bearer '+y
    code = requests.get("http://sddev.infinitylabs.in/api/devices/", headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz}, timeout = 60)
    v=code.json()
    i=v['data']
    g = json.dumps(i)
    db1 = json.loads(g)
    
    serialNo=db1[0]['serial']
    newURL = "http://sddev.infinitylabs.in/api/devices/"+serialNo
    #print(newURL)
    res1= requests.get(newURL, headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz}, timeout = 60)
    mess = res1.json()
   
    return "Current device installation status is", mess['message']
print(sddevdevicedetail_info())



### SDDEV DEVICE STATUS

def sddevdevicestatus_info():
    import requests
    import time
    import json
        
    response = requests.post("http://sddev.infinitylabs.in/api/login/", headers={"Content-Type": "application/x-www-form-urlencoded"}, data = "username=admin&password=admin@123")
    res = response.json()
    x = json.dumps(res)
    db = json.loads(x)
    y=db["token"]
    xyz= 'Bearer '+y
    code = requests.get("http://sddev.infinitylabs.in/api/devices/", headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz}, timeout = 60)
    v=code.json()
    i=v['data']
    g = json.dumps(i)
    db1 = json.loads(g)
    
    serialNo=db1[0]['serial']
    newURL = "http://sddev.infinitylabs.in/api/devices/"+serialNo
    #print(newURL)
    res1= requests.get(newURL, headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz}, timeout = 60)
    mess = res1.json()
    message = ''
    try :
        isActive = mess['data']['isActive']
        if isActive == '1':
            message = "Device Status is activated"
        else :
            message = "Device is Not Activated"
    except:
        message = "Service Not Available" 
         
    return  message
    
        
print(sddevdevicestatus_info())




# SDDEV LICENCSE UPDATE STATUS


def putinfo(request):
    import requests
    import time
    import json
    import collections
    
    slot_serial = request.intent.slots["serialNumber"].value
    
    # if slot_serial is not None:
    response = requests.post("http://sddev.infinitylabs.in/api/login/", headers={"Content-Type": "application/x-www-form-urlencoded"}, data = "username=admin&password=admin@123")
    res = response.json()
    x = json.dumps(res)
    db = json.loads(x)
    y=db["token"]
    xyz= 'Bearer '+y
    code = requests.get("http://sddev.infinitylabs.in/api/devices/", headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz}, timeout = 60)
    v=code.json()
    i=v['data']
    g = json.dumps(i)
    db1 = json.loads(g)
        
    serialNo=db1[1]['serial']
    param = {
                'serialNumber': slot_serial,
            }
    newURL = "http://sddev.infinitylabs.in/api/devices/"
    #print(newURL)
    res1 = requests.put(newURL, headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz},data=param, timeout = 60)
    #res1= requests.get(newURL, headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz})
    mess = res1.json()
    return mess['message']
    # else :
    #     return "Please Enter Serial Number"
    #return "working"
print(put_info())



# ################## ZTP #####################


def ztp(request):
    import requests
    import time
    import json
    import collections
    
    slot_serial = request.intent.slots["serialNumber"].value
    slot_lid = request.intent.slots["lid"].value
    slot_latitude = request.intent.slots["latitude"].value
    slot_longitude = request.intent.slots["longitude"].value
    slot_name = request.intent.slots["name"].value
    slot_type = request.intent.slots["type"].value
    slot_dname = request.intent.slots["dname"].value
    
    # if slot_serial is not None:
    response = requests.post("http://sddev.infinitylabs.in/api/login/", headers={"Content-Type": "application/x-www-form-urlencoded"}, data = "username=admin&password=admin@123")
    res = response.json()
    x = json.dumps(res)
    db = json.loads(x)
    y=db["token"]
    xyz= 'Bearer '+y
    code = requests.get("http://sddev.infinitylabs.in/api/devices/", headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz}, timeout = 60)
    v=code.json()
    i=v['data']
    print(i)
    g = json.dumps(i)
    db1 = json.loads(g)
        
    serialNo=db1[0]['serial']
    payload = {
                'serialNumber': slot_serial,
                'lid': slot_lid,
                'latitude': slot_latitude,
                'longitude': slot_longitude,
                'name': slot_name,
                'type': slot_type,
                'dname': slot_dname,
            }

    
    newURL = "http://sddev.infinitylabs.in/api/devices/"

    print(newURL)

    res1 = requests.post(newURL, headers={"Content-Type": "application/x-www-form-urlencoded", 'Authorization': xyz},data=payload, timeout = 60)
    
    mess = res1.json()

    return mess['message']
    # else :
    #     return "Please Enter Serial Number"
    #return "working"
#print(ztp())


###############################################################3


def ztp_device():
    
    return "please provide serial number of device"
    
    

###############################################################################

############################  CLASSES FOR SD WAN ###############################

############################################################################


# Skill Handlers



class SddevdeviceinfoHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("SddevdeviceinfoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In SddevdeviceinfoIntentHandler")
        fact_rest = sddevdevice_info()
        return handler_input.response_builder.speak("{} {}".format(fact_rest, get_random_configsz())).ask(get_random_configsz()).response




class SddevsitesinfoHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("SddevsitesinfoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In SddevsitesinfoIntentHandler")
        fact_rest = sddevsites_info()
        return handler_input.response_builder.speak("{} {}".format(fact_rest, get_random_configsz())).ask(get_random_configsz()).response
        

class SitescountinfoHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("SitescountinfoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In SitescountinfoIntentHandler")
        fact_rest = sites_count()
        return handler_input.response_builder.speak("{} {}".format(fact_rest, get_random_configsz())).ask(get_random_configsz()).response
       
    
class DevicecountinfoHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("DevicecountinfoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In DevicecountinfoIntentHandler")
        fact_rest = device_count()
        return handler_input.response_builder.speak("{} {}".format(fact_rest, get_random_configsz())).ask(get_random_configsz()).response



        
class SddevpidinfoHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("SddevpidinfoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In SddevpidinfoIntentHandler")
        fact_rest = sddevpid_count()
        return handler_input.response_builder.speak("{} {}".format(fact_rest, get_random_configsz())).ask(get_random_configsz()).response
      


        
class SddevuserinfoHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("SddevuserinfoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In SddevuserinfoIntentHandler")
        fact_rest = sddevuser_count()
        return handler_input.response_builder.speak("{} {}".format(fact_rest, get_random_configsz())).ask(get_random_configsz()).response
        
        
        
class SddevinterfaceinfoHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("SddevinterfaceinfoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In SddevinterfaceinfoIntentHandler")
        fact_rest = sddevinterface_info()
        return handler_input.response_builder.speak("{} {}".format(fact_rest, get_random_configsz())).ask(get_random_configsz()).response
        
        
class SddevactivelicenseinfoHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("SddevactivelicenseinfoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In SddevactivelicenseinfoIntentHandler")
        fact_rest = sddevactivelicense_count()
        return handler_input.response_builder.speak("{} {}".format(fact_rest, get_random_configsz())).ask(get_random_configsz()).response


# class SddevdevicedetailinfoHandler(AbstractRequestHandler):
#     def can_handle(self, handler_input):
#         # type: (HandlerInput) -> bool
#         return is_intent_name("SddevdevicedetailinfoIntent")(handler_input)

#     def handle(self, handler_input):
#         # type: (HandlerInput) -> Response
#         logger.info("In SddevdevicedetailinfoIntentHandler")
#         fact_rest = sddevdevicedetail_info()
#         return handler_input.response_builder.speak("{} {}".format(fact_rest, get_random_configsz())).ask(get_random_configsz()).response      


    
# class SddevdevicestatusinfoHandler(AbstractRequestHandler):
#     def can_handle(self, handler_input):
#         # type: (HandlerInput) -> bool
#         return is_intent_name("SddevdevicestatusinfoIntent")(handler_input)

#     def handle(self, handler_input):
#         # type: (HandlerInput) -> Response
#         logger.info("In SddevdevicestatusinfoIntentHandler")
#         fact_rest = sddevdevicestatus_info()
#         return handler_input.response_builder.speak("{} {}".format(fact_rest, get_random_configsz())).ask(get_random_configsz()).response      


###################### PUT INFO CLASS ###############################################

class SddevdevicelicenseinfoHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("SddevdevicelicenseinfoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In SddevdevicelicenseinfoIntentHandler")
        fact_rest = putinfo(handler_input.request_envelope.request)
        return handler_input.response_builder.speak("{} {}".format(fact_rest, get_random_configsz())).ask(get_random_configsz()).response   

# ########## ZTP CLASS #######################################################


class ZtpinfoHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("ZtpinfoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In ZtpinfoIntentHandler")
        fact_rest = ztp(handler_input.request_envelope.request)
        return handler_input.response_builder.speak("{} {}".format(fact_rest, get_random_configsz())).ask(get_random_configsz()).response   



        
class ZerotouchinfoHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("ZerotouchinfoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In ZerotouchinfoIntentHandler")
        fact_rest = ztp_device()
        return handler_input.response_builder.speak("{} {}".format(fact_rest, get_random_configsz())).ask(get_random_configsz()).response   



########################################################
##########################################################


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Launch Requests.

    The handler gets the in-skill products for the user, and provides
    a custom welcome message depending on the ownership of the products
    to the user.
    User says: Alexa, open <skill_name>.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In LaunchRequestHandler")

        in_skill_response = in_skill_product_response(handler_input)
        if isinstance(in_skill_response, InSkillProductsResponse):
            entitled_prods = get_all_entitled_products(in_skill_response.in_skill_products)
            if entitled_prods:
                speech = (
                    "Welcome to {}. You currently own {} products. "
                    "To hear a random fact, you could say, 'Tell me a fact', "
                    "or you can ask for a specific category you have "
                    "purchased, for example, say 'Tell me a science fact'. "
                    "To know what else you can buy, say, 'What can i buy?'. "
                    "So, what can I help you with?").format(
                        skill_name,
                        get_speakable_list_of_products(entitled_prods))
            else:
                logger.info("No entitled products")
                speech = (
                    "Welcome to infinity S D WAN, "
                    "This app helps in managing your S D WAN Service using Voice Commands."
                    # "Network Design and Deployment, IT Security,"
                    # "Data Centre Management, Cloud computing,"
                    # "Virtualization, machine learning and analytic,....."
                    # "What would you want me to help you with today ?"
                    
                ).format(skill_name)
            reprompt = "I didn't catch that. What can I help you with?"
        else:
            logger.info("Error calling InSkillProducts API: {}".format(
                in_skill_response.message))
            speech = "Something went wrong in loading your purchase history."
            reprompt = speech

        return handler_input.response_builder.speak(speech).ask(
            reprompt).response

class GetFactHandler(AbstractRequestHandler):
    """Handler for returning random fact to the user."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("GetFactIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In GetFactHandler")

        fact_text = get_random_from_list(all_facts)
        return handler_input.response_builder.speak(
            "Here's your random fact: {} {}".format(
                fact_text, get_random_yes_no_question())).ask(
            get_random_yes_no_question()).response

class YesHandler(AbstractRequestHandler):
    """If the user says Yes, they want another fact."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.YesIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In YesHandler")
        return GetFactHandler().handle(handler_input)


class NoHandler(AbstractRequestHandler):
    """If the user says No, then the skill should be exited."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.NoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In NoHandler")

        return handler_input.response_builder.speak(
            get_random_goodbye()).set_should_end_session(True).response

class GetCategoryFactHandler(AbstractRequestHandler):
    """Handler for providing category specific facts to the user.

    The handler provides a random fact specific to the category provided
    by the user. If the user doesn't own the category, a specific message
    to upsell the category is provided. If there is no such category,
    then a custom message to choose valid categories is provided, rather
    than throwing an error.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("GetCategoryFactIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In GetCategoryFactHandler")

        fact_category = get_resolved_value(
            handler_input.request_envelope.request, 'factCategory')
        logger.info("FACT CATEGORY = {}".format(fact_category))

        if fact_category is not None:
            # If there was an entity resolution match for this slot value
            category_facts = [
                l for l in all_facts if l.get("type") == fact_category]
        else:
            # If there was not an entity resolution match for this slot value
            category_facts = []

        if not category_facts:
            slot_value = get_spoken_value(
                handler_input.request_envelope.request, "factCategory")
            if slot_value is not None:
                speak_prefix = "I heard you say {}.".format(slot_value)
            else:
                speak_prefix = ""
            speech = (
                "{} I don't have facts for that category.  You can ask for "
                "science, space or history facts.  Which one would you "
                "like?".format(speak_prefix))
            reprompt = (
                "Which fact category would you like?  I have science, space, "
                "or history.")
            return handler_input.response_builder.speak(speech).ask(
                reprompt).response
        else:
            in_skill_response = in_skill_product_response(handler_input)
            if in_skill_response:
                subscription = [
                    l for l in in_skill_response.in_skill_products
                    if l.reference_name == "all_access"]
                category_product = [
                    l for l in in_skill_response.in_skill_products
                    if l.reference_name == "{}_pack".format(fact_category)]

                if is_entitled(subscription) or is_entitled(category_product):
                    speech = "Here's your {} fact: {} {}".format(
                        fact_category, get_random_from_list(category_facts),
                        get_random_yes_no_question())
                    reprompt = get_random_yes_no_question()
                    return handler_input.response_builder.speak(speech).ask(
                        reprompt).response
                else:
                    upsell_msg = (
                        "You don't currently own the {} pack. {} "
                        "Want to learn more?").format(
                        fact_category, category_product[0].summary)
                    return handler_input.response_builder.add_directive(
                        SendRequestDirective(
                            name="Upsell",
                            payload={
                                "InSkillProduct": {
                                    "productId": category_product[0].product_id,
                                },
                                "upsellMessage": upsell_msg,
                            },
                            token="correlationToken")
                    ).response


class ShoppingHandler(AbstractRequestHandler):
    """
    Following handler demonstrates how skills can handle user requests to
    discover what products are available for purchase in-skill.
    User says: Alexa, ask Premium facts what can I buy.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("ShoppingIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In ShoppingHandler")

        # Inform the user about what products are available for purchase
        in_skill_response = in_skill_product_response(handler_input)
        if in_skill_response:
            purchasable = [l for l in in_skill_response.in_skill_products
                           if l.entitled == EntitledState.NOT_ENTITLED and
                           l.purchasable == PurchasableState.PURCHASABLE]

            if purchasable:
                speech = ("Products available for purchase at this time are {}.  "
                          "To learn more about a product, say 'Tell me more "
                          "about' followed by the product name.  If you are ready "
                          "to buy say 'Buy' followed by the product name. So what "
                          "can I help you with?").format(
                    get_speakable_list_of_products(purchasable))
            else:
                speech = ("PLease try again."
                          )
            reprompt = "I didn't catch that. What can I help you with?"
            return handler_input.response_builder.speak(speech).ask(
                reprompt).response


class ProductDetailHandler(AbstractRequestHandler):
    """Handler for providing product detail to the user before buying.

    Resolve the product category and provide the user with the
    corresponding product detail message.
    User says: Alexa, tell me about <category> pack
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("ProductDetailIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In ProductDetailHandler")
        in_skill_response = in_skill_product_response(handler_input)

        if in_skill_response:
            product_category = get_resolved_value(
                handler_input.request_envelope.request, "productCategory")
            all_access = get_resolved_value(
                handler_input.request_envelope.request, "allAccess")

            if all_access is not None:
                product_category = "all_access"

            # No entity resolution match
            if product_category is None:
                speech = ("I don't think we have a product by that name.  "
                          "Can you try again?")
                reprompt = "I didn't catch that. Can you try again?"
                return handler_input.response_builder.speak(speech).ask(
                    reprompt).response
            else:
                if product_category != "all_access":
                    product_category += "_pack"

                product = [l for l in in_skill_response.in_skill_products
                           if l.reference_name == product_category]
                if is_product(product):
                    speech = ("{}.  To buy it, say Buy {}".format(
                        product[0].summary, product[0].name))
                    reprompt = (
                        "I didn't catch that. To buy {}, say Buy {}".format(
                            product[0].name, product[0].name))
                else:
                    speech = ("I don't think we have a product by that name.  "
                              "Can you try again?")
                    reprompt = "I didn't catch that. Can you try again?"

                return handler_input.response_builder.speak(speech).ask(
                    reprompt).response

class BuyHandler(AbstractRequestHandler):
    """Handler for letting users buy the product.

    User says: Alexa, buy <category>.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("BuyIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In BuyHandler")

        # Inform the user about what products are available for purchase
        in_skill_response = in_skill_product_response(handler_input)
        if in_skill_response:
            product_category = get_resolved_value(
                handler_input.request_envelope.request, "productCategory")

            # No entity resolution match
            if product_category is None:
                product_category = "all_access"
            else:
                product_category += "_pack"

            product = [l for l in in_skill_response.in_skill_products
                       if l.reference_name == product_category]
            return handler_input.response_builder.add_directive(
                SendRequestDirective(
                    name="Buy",
                    payload={
                        "InSkillProduct": {
                            "productId": product[0].product_id
                        }
                    },
                    token="correlationToken")
            ).response

class CancelSubscriptionHandler(AbstractRequestHandler):
    """
    Following handler demonstrates how Skills would receive Cancel requests
    from customers and then trigger a cancel request to Alexa
    User says: Alexa, ask premium facts to cancel <product name>
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("CancelSubscriptionIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In CancelSubscriptionHandler")

        in_skill_response = in_skill_product_response(handler_input)
        if in_skill_response:
            product_category = get_resolved_value(
                handler_input.request_envelope.request, "productCategory")

            # No entity resolution match
            if product_category is None:
                product_category = "all_access"
            else:
                product_category += "_pack"

            product = [l for l in in_skill_response.in_skill_products
                       if l.reference_name == product_category]
            return handler_input.response_builder.add_directive(
                SendRequestDirective(
                    name="Cancel",
                    payload={
                        "InSkillProduct": {
                            "productId": product[0].product_id
                        }
                    },
                    token="correlationToken")
            ).response

class BuyResponseHandler(AbstractRequestHandler):
    """This handles the Connections.Response event after a buy occurs."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("Connections.Response")(handler_input) and
                handler_input.request_envelope.request.name == "Buy")

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In BuyResponseHandler")
        in_skill_response = in_skill_product_response(handler_input)
        product_id = handler_input.request_envelope.request.payload.get(
            "productId")

        if in_skill_response:
            product = [l for l in in_skill_response.in_skill_products
                       if l.product_id == product_id]
            logger.info("Product = {}".format(str(product)))
            if handler_input.request_envelope.request.status.code == "200":
                speech = None
                reprompt = None
                purchase_result = handler_input.request_envelope.request.payload.get(
                    "purchaseResult")
                if purchase_result == PurchaseResult.ACCEPTED.value:
                    category_facts = all_facts
                    if product[0].reference_name != "all_access":
                        category_facts = [l for l in all_facts if
                                          l.get("type") ==
                                          product[0].reference_name.replace(
                                              "_pack", "")]
                    speech = ("You have unlocked the {}.  Here is your {} "
                              "fact: {}  {}").format(
                        product[0].name,
                        product[0].reference_name.replace(
                            "_pack", "").replace("all_access", ""),
                        get_random_from_list(category_facts),
                        get_random_yes_no_question())
                    reprompt = get_random_yes_no_question()
                elif purchase_result in (
                        PurchaseResult.DECLINED.value,
                        PurchaseResult.ERROR.value,
                        PurchaseResult.NOT_ENTITLED.value):
                    speech = ("Thanks for your interest in {}.  "
                              "Would you like another random fact?".format(
                        product[0].name))
                    reprompt = "Would you like another random fact?"
                elif purchase_result == PurchaseResult.ALREADY_PURCHASED.value:
                    logger.info("Already purchased product")
                    speech = " Do you want to hear a fact?"
                    reprompt = "What can I help you with?"
                else:
                    # Invalid purchase result value
                    logger.info("Purchase result: {}".format(purchase_result))
                    return FallbackIntentHandler().handle(handler_input)

                return handler_input.response_builder.speak(speech).ask(
                    reprompt).response
            else:
                logger.log("Connections.Response indicated failure. "
                           "Error: {}".format(
                    handler_input.request_envelope.request.status.message))

                return handler_input.response_builder.speak(
                    "There was an error handling your purchase request. "
                    "Please try again or contact us for help").response

class CancelResponseHandler(AbstractRequestHandler):
    """This handles the Connections.Response event after a cancel occurs."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("Connections.Response")(handler_input) and
                handler_input.request_envelope.request.name == "Cancel")

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In CancelResponseHandler")
        in_skill_response = in_skill_product_response(handler_input)
        product_id = handler_input.request_envelope.request.payload.get(
            "productId")

        if in_skill_response:
            product = [l for l in in_skill_response.in_skill_products
                       if l.product_id == product_id]
            logger.info("Product = {}".format(str(product)))
            if handler_input.request_envelope.request.status.code == "200":
                speech = None
                reprompt = None
                purchase_result = handler_input.request_envelope.request.payload.get(
                        "purchaseResult")
                purchasable = product[0].purchasable
                if purchase_result == PurchaseResult.ACCEPTED.value:
                    speech = ("You have successfully cancelled your "
                              "subscription. {}".format(
                        get_random_yes_no_question()))
                    reprompt = get_random_yes_no_question()

                if purchase_result == PurchaseResult.DECLINED.value:
                    if purchasable == PurchasableState.PURCHASABLE:
                        speech = ("You don't currently have a "
                              "subscription. {}".format(
                            get_random_yes_no_question()))
                    else:
                        speech = get_random_yes_no_question()
                    reprompt = get_random_yes_no_question()

                return handler_input.response_builder.speak(speech).ask(
                    reprompt).response
            else:
                logger.log("Connections.Response indicated failure. "
                           "Error: {}".format(
                    handler_input.request_envelope.request.status.message))

                return handler_input.response_builder.speak(
                        "There was an error handling your cancellation "
                        "request. Please try again or contact us for "
                        "help").response

class UpsellResponseHandler(AbstractRequestHandler):
    """This handles the Connections.Response event after an upsell occurs."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("Connections.Response")(handler_input) and
                handler_input.request_envelope.request.name == "Upsell")

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In UpsellResponseHandler")

        if handler_input.request_envelope.request.status.code == "200":
            if handler_input.request_envelope.request.payload.get(
                    "purchaseResult") == PurchaseResult.DECLINED.value:
                speech = ("Ok. Here's a random fact: {} {}".format(
                    get_random_from_list(all_facts),
                    get_random_yes_no_question()))
                reprompt = get_random_yes_no_question()
                return handler_input.response_builder.speak(speech).ask(
                    reprompt).response
        else:
            logger.log("Connections.Response indicated failure. "
                       "Error: {}".format(
                handler_input.request_envelope.request.status.message))
            return handler_input.response_builder.speak(
                "There was an error handling your Upsell request. "
                "Please try again or contact us for help.").response

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for help message to users."""
    def can_handle(self, handler_input):
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In HelpIntentHandler")
        in_skill_response = in_skill_product_response(handler_input)

        if isinstance(in_skill_response, InSkillProductsResponse):
            speech = (
                "To hear a random fact you can say "
                "'Tell me a fact', or to hear about the premium categories "
                "for purchase, say 'What can I buy'. For help, say , "
                "'Help me'... So, what can I help you with?"
            )
            reprompt = "I didn't catch that. What can I help you with?"
        else:
            logger.info("Error calling InSkillProducts API: {}".format(
                in_skill_response.message))
            speech = "Something went wrong in loading your purchase history."
            reprompt = speech

        return handler_input.response_builder.speak(speech).ask(
            reprompt).response


class FallbackIntentHandler(AbstractRequestHandler):
    """Handler for fallback intent.

    2018-July-12: AMAZON.FallbackIntent is currently available in all
    English locales. This handler will not be triggered except in that
    locale, so it can be safely deployed for any locale. More info
    on the fallback intent can be found here: https://developer.amazon.com/docs/custom-skills/standard-built-in-intents.html#fallback
    """
    def can_handle(self, handler_input):
        return is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = (
                "Sorry. I cannot help with that. I can help you with "
                "some facts. "
                "To hear a random fact you can say "
                "'Tell me a fact', or to hear about the premium categories "
                "for purchase, say 'What can I buy'. For help, say , "
                "'Help me'... So, what can I help you with?"
            )
        reprompt = "I didn't catch that. What can I help you with?"

        return handler_input.response_builder.speak(speech).ask(
            reprompt).response


class SessionEndedHandler(AbstractRequestHandler):
    """Handler for session end request, stop or cancel intents."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("SessionEndedRequest")(handler_input) or
                is_intent_name("AMAZON.StopIntent")(handler_input) or
                is_intent_name("AMAZON.CancelIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In SessionEndedHandler")
        return handler_input.response_builder.speak(
            get_random_goodbye()).set_should_end_session(False).response

# Skill Exception Handler
class CatchAllExceptionHandler(AbstractExceptionHandler):
    """One exception handler to catch all exceptions."""
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speech = "Sorry, I can't understand the command. Please try again!!"
        handler_input.response_builder.speak(speech).ask(speech)

        return handler_input.response_builder.response

# Request and Response Loggers
class RequestLogger(AbstractRequestInterceptor):
    """Log the request envelope."""
    def process(self, handler_input):
        # type: (HandlerInput) -> None
        logger.info("Request Envelope: {}".format(
            handler_input.request_envelope))

class ResponseLogger(AbstractResponseInterceptor):
    """Log the response envelope."""
    def process(self, handler_input, response):
        # type: (HandlerInput, Response) -> None
        logger.info("Response: {}".format(response))


sb = StandardSkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(GetFactHandler())
sb.add_request_handler(YesHandler())
sb.add_request_handler(NoHandler())
sb.add_request_handler(GetCategoryFactHandler())
sb.add_request_handler(BuyResponseHandler())
sb.add_request_handler(CancelResponseHandler())
sb.add_request_handler(UpsellResponseHandler())
sb.add_request_handler(ShoppingHandler())
sb.add_request_handler(ProductDetailHandler())
sb.add_request_handler(BuyHandler())
sb.add_request_handler(CancelSubscriptionHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedHandler())

sb.add_exception_handler(CatchAllExceptionHandler())
sb.add_global_request_interceptor(RequestLogger())
sb.add_global_response_interceptor(ResponseLogger())


#########################   SD WAN   #########################

sb.add_request_handler(SddevdeviceinfoHandler())

sb.add_request_handler(DevicecountinfoHandler())

sb.add_request_handler(SddevsitesinfoHandler())

sb.add_request_handler(SitescountinfoHandler())

sb.add_request_handler(SddevpidinfoHandler())

sb.add_request_handler(SddevuserinfoHandler())

sb.add_request_handler(SddevinterfaceinfoHandler())

sb.add_request_handler(SddevactivelicenseinfoHandler())

# sb.add_request_handler(SddevdevicedetailinfoHandler())

# sb.add_request_handler(SddevdevicestatusinfoHandler())

sb.add_request_handler(SddevdevicelicenseinfoHandler())

sb.add_request_handler(ZtpinfoHandler())

sb.add_request_handler(ZerotouchinfoHandler())


###############################################################


lambda_handler = sb.lambda_handler()