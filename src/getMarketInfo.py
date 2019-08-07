from binance.client import Client
import getAPIKey

client = Client(getAPIKey.getAPIkey(), getAPIKey.getAPIsecret())

print(client.get_all_tickers())