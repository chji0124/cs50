import requests
import sys
import json

if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit()
else:
    try: 
        num = float(sys.argv[1]) 
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = response.json()
        bitcoin = o["bpi"]["USD"]["rate_float"]
        price = float(bitcoin)
        total = price * num
        print(f"${total:,.4f}")
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit()
    except requests.RequestException:
        sys.exit() 


    
    
    

    



