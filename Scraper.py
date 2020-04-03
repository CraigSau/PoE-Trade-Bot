def main():
	import requests
	url = "https://poe.ninja/api/Data/GetCurrencyOverview?league=Deliruim"
	response = requests.get(url, headers={'User-Agent' : 'Mozilla/5.0'})
	html = response.content
	print(html)

main()
