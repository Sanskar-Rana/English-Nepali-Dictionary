from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs


# Create your views here.

def index(request):
    if request.method == 'POST':
        data = request.POST
        words = data['word']
        payload = {'q': words}
        r = requests.get('https://www.englishnepalidictionary.com/', params=payload).text
        soup = bs(r, 'lxml')
        meaning = soup.find('div', class_='search-result').h3.text
        context = {
            'meaning': meaning
        }
        return render(request, 'index.html', context)

    return render(request, 'index.html')
