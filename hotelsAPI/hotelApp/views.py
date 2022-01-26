from django.shortcuts import render, redirect
import requests

# Create your views here.

API_KEY = "d84cac5344msh33270a08a1f925dp1a6804jsnc0e11ff8cd25"

def index(request):
    context = {}
    

    if request.method == 'POST':
        search = request.POST['location']
        if search:
            return redirect(f'/location/{search}')

    return render(request, "hotelApp/index.html", context)

def locationview(request, search):
    context = {}
    context['search'] = search
    locations = []

    url = "https://hotels4.p.rapidapi.com/locations/v2/search"

    querystring = {"query":search,"locale":"en_US","currency":"USD"}

    headers = {
        'x-rapidapi-host': "hotels4.p.rapidapi.com",
        'x-rapidapi-key': API_KEY
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    try:
        data = response.json()
    except:
        print("Nu a retras locatiile")

    if response.status_code == 200:
        for suggestion in data['suggestions']:
            if suggestion['group'] == "CITY_GROUP":
                locations = suggestion['entities']

    print(locations)
    context['locations'] = locations

    return render(request, "hotelApp/locations.html", context)

def hotelsView(request):
    if request.method == "POST":
        context = {}
        hotels = []
        try:
            location = request.POST['locations']
        except:
            print("Nu a primit locatia")
        try:
            dateInterval = request.POST['dates']
        except:
            print("Nu a primit data")
        try:
            adults = request.POST['adults']
        except:
            print("Nu a primit numarul de adulti")
        print(location)
        print(adults)

        dates = dateInterval.split(" - ")
        checkin = dates[0].replace("/", "-")
        checkout = dates[1].replace("/", "-")
        checkIn = checkin[6:10] + "-" + checkin[0:2] + "-" + checkin[3:5]
        checkOut = checkout[6:10] + "-" + checkout[0:2] + "-" + checkout[3:5]
        print(checkIn, checkOut)

        url = "https://hotels4.p.rapidapi.com/properties/list"

        querystring = {"destinationId":str(location),"pageNumber":"1","pageSize":"25","checkIn":checkIn,"checkOut":checkOut,"adults1":str(adults),"sortOrder":"PRICE","locale":"en_US","currency":"USD"}

        headers = {
            'x-rapidapi-host': "hotels4.p.rapidapi.com",
            'x-rapidapi-key': API_KEY
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        try:
            data = response.json()
        except:
            print("Nu a retras hotelurile")

        if response.status_code == 200:
            hotels = data['data']['body']['searchResults']['results']
            context['hotels'] = hotels
            print(hotels[0])
        

        return render(request, "hotelApp/hotels.html", context)

def hotelsImagesView(request, id):
    context = {}
    images = []

    url = "https://hotels4.p.rapidapi.com/properties/get-hotel-photos"

    querystring = {"id":id}

    headers = {
        'x-rapidapi-host': "hotels4.p.rapidapi.com",
        'x-rapidapi-key': API_KEY
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    try:
        data = response.json()
    except:
        print("Nu a retras imaginile")

    if response.status_code == 200:
        objects = data['hotelImages']
        if len(objects) > 20:
            images = objects[1:20]
        else:
            images = objects
    context['images'] = images

    
    return render(request, "hotelApp/images.html", context)