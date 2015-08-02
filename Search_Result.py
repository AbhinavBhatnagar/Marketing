__author__ = 'abhatna4'

from piplapis.search import SearchAPIRequest, SearchAPIError
from piplapis.data import Person
import piplapis.data
from piplapis.data import Name, Email, Address, Gender
import csv


my_key = u'9ztqbp5mxbuqdc3z6g6nckdy'

output = open('address.txt','wb')

# ### Reads the file and convert each line to a dictionary format
def read_the_files():
    row = {}
    with open('twitter_data.txt', 'r') as file:
        for lines in file:
            search_object(lines.rstrip())


def search_object(name):
    user = name + '@twitter'
    try:
        request = SearchAPIRequest(username=user, country='US')
        response = request.send()

        if response.person != None and response.person.addresses != None:
            print response.person.names
            #print response.person.addresses
            output.write(str(response.person.names)+ "\t" + str(response.person.addresses)+ "\n")
    except SearchAPIError as e:
        print e.http_status_code, e

def main():
    SearchAPIRequest.set_default_settings(api_key=my_key, minimum_probability=None, show_sources=None,
                                          minimum_match=None, hide_sponsored=None, live_feeds=None, use_https=True)
    #search_object(read_the_files())
    read_the_files()


if __name__ == "__main__":
    main()
