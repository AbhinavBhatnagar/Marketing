__author__ = 'abhatna4'

import urllib2
import json
import xml.dom.minidom
import time
import csv

addresses = open("addresses.txt", 'rb')

def clean_address():
    for lines in addresses:
        line = lines.split("\t")
        name = line[0]
        address = line[1][1:-2].split("),")
        i = 0
        while i < len(address):
            addressed = address[i][8:-1]

            street = ''
            city = ''
            state = ''
            if 'street' in addressed:
                print addressed
                x = addressed.find('street')
                y = addressed.find("',", x)
                street = addressed[x+9:y]
                x = addressed.find('city')
                y = addressed.find("',", x)
                city = addressed[x+7:y]
                x = addressed.find('state')
                y = addressed.find("',", x)
                state = addressed[x+8:y]
                address = get_formatted_address(street, city, state)
                lat, lang = get_coordinates(address)
                print lat, lang
            i += 1


def get_formatted_address(street, city, state):
    street = street.replace(' ', '+')
    city = city.replace(' ', '+')
    address = street + ',+' + city + ',+' + state
    return address

def get_coordinates(address):
    key = 'AIzaSyBxt3zjZjb7eN1rJuwrhAj-EjyIX5X8cnQ'
    str = 'https://maps.googleapis.com/maps/api/geocode/json?address='+address+'&key='
    url = str+key

    time.sleep(0.2)
    request = urllib2.urlopen(url)

    response = json.load(request)

    #for k,v in response.iteritems():
        #print k,v

    res_dict = response['results'][0]

    lat = res_dict['geometry']['location']['lat']
    lng = res_dict['geometry']['location']['lng']
    return lat,lng

def func2():
    with open(path,'rb') as file:
        file.readline()
        final_list = []
        for line in file:

            final_addr = ''
            line_list = line.split(',')
            addr = line_list[5]
            if 'PO BOX' in addr:
                print 'shit'
                continue

            addr_list =  line_list[5][1:-1].split(' ')

            city = line_list[15][1:-1]
            state = line_list[16][1:-1]
            #print addr_list,len(addr_list)
            for ele in addr_list:
                final_addr = final_addr+ ele + '+'

            final_addr = final_addr[:-1] + ',+' + city + ',+' + state
            final_list.append(final_addr)

        return final_list


def KML(data):
    #kml file generator
    f = open('csv2kml_1040.kml', 'w')

    #Writing the kml file.
    f.write("<?xml version='1.0' encoding='UTF-8'?>\n")
    f.write("<kml xmlns='http://earth.google.com/kml/2.2'>\n")
    f.write("<Document>\n")
    f.write("   <name>" + 'test' + '.kml' +"</name>\n")
    for row in data:
        lat = row[0]
        lng = row[1]
        addr = row[2]
        name = row[3]
        func4(f, lat, lng, name, addr)
    f.write("</Document>\n")
    f.write("</kml>\n")
    f.close()

def func4(f,lat,lng,name,addr):
    f.write("   <Placemark>\n")
    f.write("       <name>" + name + "</name>\n")
    f.write("       <description>" + ''.join(addr.split('+')) + "</description>\n")
    f.write("       <Point>\n")
    f.write("           <coordinates>" + str(lng) + "," + str(lat)  + ", 0</coordinates>\n")
    f.write("       </Point>\n")
    f.write("   </Placemark>\n")


if __name__ == '__main__':
    clean_address()
    # addr = '1600+Amphitheatre+Parkway,+Mountain+View,+CA'
    # lat, lang = func1(addr)
    # print lat
    # print lang
    #
    # addr_list = func2()
    # data_list = []
    # cnt = 0
    # f = open('data_list1040.txt','wb')
    # writer = csv.writer(f)
    # for addr in addr_list:
    #     cnt += 1
    #     name = 'name_' + str(cnt)
    #     lat,lng = func1(addr)
    #     data_list.append([lat,lng,addr,name])
    #     writer.writerow([lat,lng,addr,name])
    #
    # func3(data_list)
