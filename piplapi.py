__author__ = 'abhatna4'

from piplapis.search import SearchAPIRequest, SearchAPIError
from piplapis.data import Person
import piplapis.data
from piplapis.data import Name, Email, Address, Gender
import csv


my_key = u'9ztqbp5mxbuqdc3z6g6nckdy'

### Gets the schema of the file and saves it to list format
def get_schema():
    schema = []
    with open('M0388917/M0388917.Output.LCR.txt', 'r') as file:
        schemas = file.readline()
        col_names = schemas.split(",")
        for col in col_names:
            schema.append(col)

#### Reads the file and convert each line to a dictionary format
def read_the_files():
    row = {}
    with open('M0388917/M0388917.Output.LCR.txt', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            return row


def bind_pipl_object(row):
    raw_address = row['ADDRESS']+ " " + ", " + row['CITY'] + ", "+row['STATE']+ " " + row['ZIP5']
    person = Person()
    person.names.append(Name(first=row['FIRST NAME'], middle=row['MI'], last=row['LAST NAME']))
    person.addresses.append(Address())
    #person.emails.append(Email("abhatnagar.1610@gmail.com"))
    return person



def search_object(person):
    request = SearchAPIRequest(person=bind_pipl_object(read_the_files()))
    try:
        response = request.send()
        print(response.image.get_thumbnail_url(500, 500, zoom_face=True, favicon=False))
        print response.name
        print response.address
        print response.job
    except SearchAPIError as e:
        print e.http_status_code, e


def main():
    SearchAPIRequest.set_default_settings(api_key=my_key, minimum_probability=None, show_sources=None,
                                          minimum_match=None, hide_sponsored=None, live_feeds=None, use_https=True)
    search_object(read_the_files())

if __name__ == "__main__":
    #get_schema()
    main()
