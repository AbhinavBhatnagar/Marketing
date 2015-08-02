__author__ = 'abhatna4'


import csv
from piplapis.search import SearchAPIRequest
from piplapis.data import Person, Name, Address, Email, Job
from piplapis.search import SearchAPIError


def search_file():
    with open('M0388917/M0388917.Output.LCR.txt', 'r') as file:
        reader = csv.DictReader(file)
        for lines in reader:
            #print lines
            search(lines)


def set_default():
    SearchAPIRequest.set_default_settings(api_key=u'9ztqbp5mxbuqdc3z6g6nckdy', minimum_probability=None,
                                          show_sources="all", minimum_match=None, hide_sponsored=None, live_feeds=None,
                                          use_https=True)


def search(row):

    fields = [Name(first=unicode(row['FIRST NAME'], "utf-8"), middle= unicode(row['MI'], "utf-8"),
              last=unicode(row['LAST NAME'], "utf-8")),
          Address(country=u'US', state=unicode(row['STATE'], "utf-8"), city=unicode(row['CITY'], "utf-8"),
                  zip_code=unicode(row['ZIP5'], "utf-8"))]
    request = SearchAPIRequest(person=Person(fields))
    try:
        response = request.send()
        print response.name
        #print response.address
        #print response.job
        if(response.email != None):
            email = response.email
            print email.username
        if(response.person != None):
            print response.sources[0].origin_url
            if(response.person.user_ids != None):
                print response.person.user_ids
    except SearchAPIError as e:
        print e.http_status_code, e


if __name__ == "__main__":
    set_default()
    search_file()