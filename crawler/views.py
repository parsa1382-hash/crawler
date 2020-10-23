from django.shortcuts import render
from django.http import HttpResponse
import requests
import csv

def get(request):
	url = 'http://www.tsetmc.com/tsev2/data/Export-txt.aspx?t=i&a=1&b=0&i=26014913469567886'
	r = requests.get(url, allow_redirects = True)
	open('ghadir.csv', 'wb').write(r.content)

	# 2020/10/20

	c = []
	with open('ghadir.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter = ',')
		for row in csv_reader:
			row = row[1:6]
			row[0] = row[0][:4] + '/' + row[0][4:6] + '/' + row[0][6:]
			c.append(row)
	#print(c[:5])

	context = {
		'data': c[1:101]
	}


	return render(request, 'crawler/home.html', context)

# Create your views here.
