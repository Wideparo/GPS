# GPS converter
import ssl
from urllib.request import urlopen as OPEN
from urllib.parse import urlencode as ENCODE
from xml.etree import ElementTree as XML


# from urllib.request import Request

def get_coordinates(address):
    # The API request
    api_url = 'https://maps.googleapis.com/maps/api/geocode/xml?&key=AIzaSyD46BuL7Eb65FsC-6bMXNEf0ScMeKIvT5U&'

    # ask for user input
    #address = input('Enter address: ')
    if len(address) < 1:
        address = 'Warsaw, Poland'

    # putting the parts together in UTF-8 format
    url = api_url + ENCODE({'address': address})

    # getting the data
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    data = OPEN(url, context=ssl_context).read()

    # digging into the XML tree
    tree = XML.fromstring(data)
    # let's see the results now
    res = tree.findall('result')

    # dig into the XML tree to find 'latitude'
    lat = res[0].find('geometry').find('location').find('lat').text
    # find longitude
    lng = res[0].find('geometry').find('location').find('lng').text

    # convert the response from XML to float and add the cardinal directions
    lat = float(lat)
    lng = float(lng)
    lat_c = 'S' if lat < 0 else 'N'
    lng_c = 'W' if lng < 0 else 'E'

    # the actual object found by the API
    location = res[0].find('formatted_address').text

    # The results
    print("==>", location, "<==")
    print('Latitude: {0:.5f}{1}'.format(abs(lat), lat_c))
    print('Longitude: {0:.5f}{1}'.format(abs(lng), lng_c))