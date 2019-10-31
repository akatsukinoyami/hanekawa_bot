import shelve
import requests
class Exchange:
    file = 'exchange_db'
    standart = ['EUR', 'USD', 'RUB', 'UAH']
    currency = ["AED", "ARS", "AUD", "BGN", "BRL", "BSD", "CAD", "CHF", "CLP", "CNY", "COP", "CZK", "DKK", "DOP", "EGP", "EUR", "FJD", "GBP", "GTQ", "HKD", "HRK", "HUF", "IDR", "ILS", "INR", "ISK", "JPY", "KRW", "KZT", "MXN", "MYR", "NOK", "NZD", "PAB", "PEN", "PHP", "PKR", "PLN", "PYG", "RON", "RUB", "SAR", "SEK", "SGD", "THB", "TRY", "TWD", "UAH", "USD", "UYU", "VND", "ZAR"]

    def exchange_run(self, base, dest, num, mmbr_id):
        r = requests.get('https://api.exchangerate-api.com/v4/latest/'+base.upper())
        exch_dict = eval(r.text)
        dest = dest.upper()

        if dest in self.currency:
            rate = exch_dict['rates'][dest]
            sum = float(num) * float(rate)
            result = str(num) +' '+ base.upper() + ' = ' + str(round(sum)) + ' ' + dest
            return result
        else:
            rates_list = []
            with shelve.open(self.file) as db:
                if mmbr_id not in db:
                    db[mmbr_id] = self.standart
                db_id = db[mmbr_id]
                for i in db_id:
                    num = int(num)
                    rate = exch_dict['rates'][i]
                    sum = num * float(rate)
                    rates_list.append(i+' '+str(round(sum, 2)))
                res = '\n'.join(rates_list)  
                db[mmbr_id] = db_id
                return res    


    def exchange_add(self, base, mmbr_id):
        mmbr_id = str(mmbr_id)
        with shelve.open(self.file) as db:
            if mmbr_id not in db:
                db[mmbr_id] = self.standart
            db_id = db[mmbr_id]
            count = db_id.count(base.upper())
            if count == 0:
                db_id.append(base.upper())
                add1 = ', '.join(db_id) 
                added = 'Валюты в вашем списке:\n'+add1
            else:
                added = 'Валюта уже есть в списке'
            db[mmbr_id] = db_id
        return added

    def exchange_del(self, base, mmbr_id):
        mmbr_id = str(mmbr_id)
        with shelve.open(self.file) as db:
            if mmbr_id not in db:
                db[mmbr_id] = self.standart
            db_id = db[mmbr_id]
            try:
                db_id.remove(base.upper())
                remove = ', '.join(db_id) 
                removed = 'Валюты в вашем списке:\n'+remove
            except ValueError:
                removed = ('Валюты нет в списке')
            db[mmbr_id] = db_id
        return removed