# I have to create views.py. Initially it doesn't exist while creating project.

from django.http import HttpResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


def index(request):
    html_data = requests.get("https://www.mohfw.gov.in/index.html").text
    # print(html_data)
    soup = BeautifulSoup(html_data, 'html.parser')
    info_name = soup.find('li', class_="bg-blue").find('span', class_='mob-show').get_text()
    info_num = soup.find('li', class_="bg-blue").contents[3].get_text(strip=True)

    info_name1 = soup.find('li', class_="bg-green").find('strong', class_='mob-hide').get_text()
    info_num1 = soup.find('li', class_="bg-green").contents[3].get_text(strip=True)

    info_name2 = soup.find('li', class_="bg-red").find('strong', class_='mob-hide').get_text()
    info_num2 = soup.find('li', class_="bg-red").contents[3].get_text(strip=True)

    return render(request, 'index.html', {'info_num': info_num, 'info_num1': info_num1, 'info_num2': info_num2})

