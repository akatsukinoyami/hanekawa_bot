from config import api_key, api_secret
import requests


def exchange(base, dest, num):
    currency = ["AED", "ARS", "AUD", "BGN", "BRL", "BSD", "CAD", "CHF", "CLP", "CNY", "COP", "CZK", "DKK", "DOP", "EGP", "EUR", "FJD", "GBP", "GTQ", "HKD", "HRK", "HUF", "IDR", "ILS", "INR", "ISK", "JPY", "KRW", "KZT", "MXN", "MYR", "NOK", "NZD", "PAB", "PEN", "PHP", "PKR", "PLN", "PYG", "RON", "RUB", "SAR", "SEK", "SGD", "THB", "TRY", "TWD", "UAH", "USD", "UYU", "VND", "ZAR"]
    r = requests.get('https://api.exchangerate-api.com/v4/latest/'+base)
    exch_dict = eval(r.text)
    

    if dest.lower() == 'auto':
        num = int(num)
        rateeur = exch_dict['rates']['EUR']
        sumeur = num * float(rateeur)
        rateusd = exch_dict['rates']['USD']
        sumusd = num * float(rateusd)
        raterub = exch_dict['rates']['RUB']
        sumrub = num * float(raterub)
        rateuah = exch_dict['rates']['UAH']
        sumuah = num * float(rateuah)

        result = '🇪🇺' + str(round(sumeur, 2)) +' \n' +'🇺🇸' + str(round(sumusd, 2)) +' \n' + '🇷🇺' + str(round(sumrub, 2)) +' \n' + '🇺🇦 ' + str(round(sumuah, 2))

    else:
        rate = exch_dict['rates'][dest]
        sum = float(num) * float(rate)
        result = str(num) +' '+ base + ' = ' + str(round(sum)) + ' ' + dest

    return result
