from django.shortcuts import render
import requests
import json

# Create your views here.
def home(request):    
    
    # Grab Crypto price
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD,EUR,INR", verify=False)
    price = json.loads(price_request.content.decode('utf-8'))

    # Grab News
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN", verify=False)
    api = json.loads(api_request.content.decode('utf-8'))

    return render(request, 'home.html', {"api": api, 'price': price})

def prices(request):
    if request.method == 'POST':
        import requests
        import json
        quote = request.POST['quote']
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+ quote.upper() +"&tsyms=USD,EUR,INR", verify=False)
        crypto = json.loads(crypto_request.content.decode('utf-8'))
        return render(request, 'prices.html', {'quote': quote, 'crypto': crypto})
    else:
        notfound = "Enter a Cryptocurrency Symbol"
        return render(request, 'prices.html', {"notfound": notfound})
