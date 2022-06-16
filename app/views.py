from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    url = "https://sandbox.cashfree.com/pg/api/v1/order/create"
    payload = {
     "appId":"17792263f8ad3b41a90673b52f229771",
     "secretkey":"00f09ad3074140b18466ebbb092f8e6066917028",
     "order_id":"order_id_new_0909090",
     "orderAmount":"1",
     "orderCurrency":"INR",
     "orderNote":"This is an optional field",
     "customerName":"armaan",
     "customerEmail":"armaanalam65@gmail.com",
     "customerPhone":"9973884727",
     "returnurl":"https://cashfree.com",
     "notifyUrl":""
}



    return render(request,'BASE/base.html')

