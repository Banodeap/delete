from django.shortcuts import render
from django.http import HttpResponse
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
config = {
  "type": "service_account",
  "project_id": "sales-10f74",
  "private_key_id": "c0d7f9d9379b9e9e3c4b72fe9337bab37cae848f",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDqD3tRisFB7QIf\nbtUjjmOTyFDIZuklSYD2YDLFHycaAT6ZurwoYkYcNhFbFa3AfrkeGYpqm+FfyWxc\nnL6Ebff4hjYnZPmXoKYe9WLrhzUdrrahWqBsNvyDZttvJVah4u+Q1to4gMPyOtBa\neanWfsFFHbBAZLi+9NgF/Mx4wwEGzMNQNDaqjqaYKH7FE13r+V2ZYzZ0XxmQseMz\nhgRuWf2/Wu0o6IkN/IxXDuGHa7E5sx6TNs31tY3v5JJsDV+CIbnkhPA5GSdShJlt\nrYMp9wmUA/e3/gtQxQmIqmnTbcGC5iPi1VnNe7I+zofseXTZvuJhwOnncHERvDXe\nmCtWcpgnAgMBAAECggEAav06rHJVlpIFB2M9MCyVHedR7dkEt5OazIP6kRqFYCCz\ngcfW3ErXq2uXkWAedUA31Cdumv64DXXf/5FykMxHriWDOYyxfnrjlIEsf2blg7Tq\nLGVlsTGNSW9J3Mtfh05ZnYZoZ62MY/w4YzL7zF1ScQp6F2UzAa6f1FTTDlxs6rLs\npeQt4GixxqHSJz1Z12k/tcnac8nfDljh/3/TLeEjpBh2L+XvVWoR19wY9MBaYUp3\n1E8IDsV+4GiicudKYwV7Js5U2ijHzVwocvUw/1tzWegetNzdB9eT+t3hHN/flQe6\nrwalsPdKXyGhieWpxB4YStgDhXGjpoa30T6TGw6KgQKBgQD9TP70XQnHiIiwxtA5\nGfMhOMcXMsyqW2/O1eVFNjkyAleIm65EZg9CdE5e+UeSCs6oUqO/B5FtYnN032Js\nlN8R+498I27Q1/fsRW5jdLB/gX5yGsIIA88pNv+dL9stS2NXyhsugNMczq3Eb0P9\nlnSvU5OTXNKjfFG9J468Mb4E5wKBgQDsjf+Rr61gNSa9wY8HJMU8s6jYKyMYaKBK\nqT2hJl4fgAf2VhLJHjhO3lE9UfpBgVmcvlLpfDTp54IHQgzLGgpUmu76lFBlWMlI\nhgDTsvKDXGtz4dvvkkbqX5Sh3tPn8oCwXkbiE159m/vgCz5FTHgPYMsNXJsKwpN+\n9k4T7CUqwQKBgFrev2w84GBDu/3nJRYHGDDn5IyO/dtzuBW0qG5++F/XdT2d1BPX\npUvK2764oRNkayT5mKLUfTiHpDHeXbnkYm5aF+yJ7ZxgjiGl+ucVGqhzdUBMFyW2\n8B+yCluCqpeCPx5kdAHn11SzVKVu4S5dRnkLe5rXJv3dgJliUpNzKN8rAoGAYyF+\noEbGmTKs8YhTr+Kw5SdE8pHhOzFdOuyBby7s8rZsn8aiSLXpUuPHl7Lq9NiH/S+k\n/0OVyQ/DZddAFTzsZ1gmHcxZhJ8YetPtNMog5vur6/wSdusN3NoBJ3SByQnO9BoO\nCl+jkW/0tYcAqXnKNmeRsB/GuVOhC+ub/K1RRgECgYA98yOgltoRqXBmnuJRQlaB\nEuc+G8fsiylYHZ3vAV6u136R5u6t6JK99oKFYbZYfT23eynSt4BDGyjVW9N+7DUV\nDWAgsxQDaGozb0TOrilcPDLRl7X68Tnk2WKDPGGrBCM2kiQHL9EUDYMPlBGF/0kU\n+Q27HbW6UhP0ap1v5ypn6w==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-sh3sz@sales-10f74.iam.gserviceaccount.com",
  "client_id": "105761078711488330423",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-sh3sz%40sales-10f74.iam.gserviceaccount.com"
}

cred = credentials.Certificate(config)
firebase_admin.initialize_app(cred)
database = firestore.client()


def index(request):
    n = '11'
    prod_name = database.child(n).child('prod_name').get().val()
    all_products = database.child('products').child('prod_id').order_by_child('prod_type').equal_to('smartphone').get()
    products = {}
    for i in all_products.each():
        products[i.key()] = i.val()
    return render(request, 'index.html', {"products": products})

def home(request):
  return render(request, 'home.html')

def smartphone(request):
  smartphones = []
  all_smartphones = database.collection('smartphone').get()
  for i in all_smartphones:
    i = i.to_dict()
    smartphones.append(i)
  return render(request, 'smartphone.html', {'smartphones': smartphones})
    

def laptop(request):
  laptops = []
  all_laptops = database.collection('laptop').get()
  for i in all_laptops:
    i = i.to_dict()
    laptops.append(i)
  return render(request, 'laptop.html', {'laptops': laptops})

def watch(request):
  watches = []
  all_watches = database.collection('watch').get()
  for i in all_watches:
    i = i.to_dict()
    watches.append(i)
  return render(request, 'watch.html', {'watches': watches})

def headphone(request):
  headphones = []
  all_headphones = database.collection('headphone').get()
  for i in all_headphones:
    i = i.to_dict()
    headphones.append(i)
  return render(request, 'headphone.html', {'headphones': headphones})

def checkout(request):
  cart_price = 0
  customer_id = 0

  if request.method == "POST":
    name = request.POST["name"]
    email_id = request.POST["email_id"]
    address = request.POST["address"]
    prod_id = request.POST["prod_id"]
    prod_color = request.POST["prod_color"]
    prod_qn = request.POST["prod_qn"]
    prod_id = int(prod_id)
    prod_qn = int(prod_qn)
    
    user_info = {
      'name': name, 'email_id': email_id, 'address': address, 'prod_id': prod_id, 'prod_color': prod_color, 'prod_qn': prod_qn
    }

    #generate a random customer id
    customer_id = database.collection('sales').document().id

    if prod_id in range(1,11):
      #update the product quantity in inventory
      current_prod_qn = database.collection('smartphone').document(str(prod_id)).get(field_paths = {'prod_qn'}).to_dict().get('prod_qn')
      new_prod_qn = current_prod_qn - prod_qn
      database.collection('smartphone').document(str(prod_id)).update({'prod_qn': new_prod_qn})

      #calculate cart price
      prod_price = database.collection('smartphone').document(str(prod_id)).get(field_paths = {'prod_price'}).to_dict().get('prod_price')
      cart_price = prod_qn*prod_price
      user_info['amount'] = cart_price

      #add user information to sales database
      database.collection('sales').document(customer_id).set(user_info)

    elif prod_id in range(11,21):
      #update the product quantity in inventory
      current_prod_qn = database.collection('laptop').document(str(prod_id)).get(field_paths = {'prod_qn'}).to_dict().get('prod_qn')
      new_prod_qn = current_prod_qn - prod_qn
      database.collection('laptop').document(str(prod_id)).update({'prod_qn': new_prod_qn})

      #calculate cart price
      prod_price = database.collection('laptop').document(str(prod_id)).get(field_paths = {'prod_price'}).to_dict().get('prod_price')
      cart_price = prod_qn*prod_price
      user_info['amount'] = cart_price

      #add user information to sales database
      database.collection('sales').document(customer_id).set(user_info)

    elif prod_id in range(21,31):
      #update the product quantity in inventory
      current_prod_qn = database.collection('watch').document(str(prod_id)).get(field_paths = {'prod_qn'}).to_dict().get('prod_qn')
      new_prod_qn = current_prod_qn - prod_qn
      database.collection('watch').document(str(prod_id)).update({'prod_qn': new_prod_qn})

      #calculate cart price
      prod_price = database.collection('watch').document(str(prod_id)).get(field_paths = {'prod_price'}).to_dict().get('prod_price')
      cart_price = prod_qn*prod_price
      user_info['amount'] = cart_price

      #add user information to sales database
      database.collection('sales').document(customer_id).set(user_info)

    elif prod_id in range(31,41):
      #update the product quantity in inventory
      current_prod_qn = database.collection('headphone').document(str(prod_id)).get(field_paths = {'prod_qn'}).to_dict().get('prod_qn')
      new_prod_qn = current_prod_qn - prod_qn
      database.collection('headphone').document(str(prod_id)).update({'prod_qn': new_prod_qn})

      #calculate cart price
      prod_price = database.collection('headphone').document(str(prod_id)).get(field_paths = {'prod_price'}).to_dict().get('prod_price')
      cart_price = prod_qn*prod_price
      user_info['amount'] = cart_price

      #add user information to sales database
      database.collection('sales').document(customer_id).set(user_info)
      
    request.session['cart_price'] = cart_price
    request.session['customer_id'] = customer_id
    return HttpResponseRedirect('confirm')
  return render(request, 'checkout.html')

def confirm(request):
  
  cart_price = request.session['cart_price'] 
  customer_id = request.session['customer_id'] 

  summary = {
    'amount': cart_price,
    'customer_id': customer_id
  }
  
  return render(request, 'confirm.html', summary )