# print('Welcome! This tool will help you convert USD to other currencies.')
# print('You will be asked to input the amount of USD you wish to convert','\n','as well as one foreign currency from a given list.')
# print('Press enter to continue: ')

# Data, and following block of code, from exchangerate.host
import requests

url = 'https://api.exchangerate.host/latest'
response = requests.get(url)
data = response.json()

print(data)
# End of code from exchangerate.host

# desiredCurrecy = 'EUR'
amountUSD = float(input('Please input the amount of USD you want to convert: '))
allRates = data['rates']
listCurrencies = list(allRates.keys())

print('\n')
print('Please type one of the following options:')
print('\n', listCurrencies,'\n')

desiredCurrecy = input('What is your desired currency?: ').upper()
value = data['rates'][desiredCurrecy] # value of desired currencies to 1.00 EUR

# USD to EUR
valueUSD = data['rates']['USD']
amountEUR = round((amountUSD / valueUSD), 2)
amountDesiredCurrency = round(amountEUR*value, 2)

print("%.2f" % amountUSD, 'USD ~=', amountDesiredCurrency, desiredCurrecy + '.')
print('Friendly reminder: Exchange fees may be applied by the seller.')