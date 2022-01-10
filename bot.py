from  alpha_vantage import *
import requests
import discord
import os
client = discord.Client()



def price_checker(currency):
    currency=currency.upper()
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency='+currency+'&to_currency=USD&apikey='+os.getenv("API_key")
    r = requests.get(url)
    data = r.json()
    res=data['Realtime Currency Exchange Rate']['5. Exchange Rate']
    return res

def message_former(currency):
    price_checker(currency)
    
    str1=currency+" price in usd:  "+str(price_checker(currency))
    
    return str1
    

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('!help'):
        await message.channel.send('''
        **under development by yours truly**

        Available commands:
        !hello -->Hello back
        !btc   -->Btc price
        !eth   -->Ethereum price
        ''')
    if message.content.startswith('!btc'):
        
        await message.channel.send(message_former('btc'))
        
    if message.content.startswith('!eth'):

        await message.channel.send(message_former('eth'))
    
client.run(os.getenv('TOKEN'))
