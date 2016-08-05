#!/usr/bin/env/python

# ex39_firstex.py
# Code written by Robin Goyal
# Created on 05-08-2016
# Last updated on 05-08-2016

# Canadian Provinces Mapping

provinces = {
        'Ontario': 'ON',
        'Saskatchewan': 'SK',
        'Alberta': 'AB',
        'Quebec': 'QC',
        'British Columbia': 'BC',
        'Prince Edward Island': 'PE',
        'Manitoba': 'MB',
        'Newfoundland': 'NL',
        'Nova Scotia': 'NS',
        'New Brunswick': 'NB'
        }

capital = {
        'ON': 'Toronto',
        'SK': 'Regina',
        'AB': 'Edmonton',
        'QC': 'Quebec City',
        'BC': 'Victoria',
        'PE': 'Charlottetown',
        'MB': 'Winnipeg',
        'NL': 'St. John\'s',
        'NS': 'Halifax',
        'NB': 'Fredericton'
        }

for province, abbrev in provinces.items():
    print "The abbreviation of %s is %s and has the capital %s" % (province, abbrev, capital[abbrev])

print '-' * 12

# Checks if key is in the dictionary
if 'Ontario' in provinces:
    print "Ontario is a province in Canada"

if not('CB' in provinces):
    print "CB is not a province in Canada"

# format is key in dict
if 'BC' in provinces and 'BC' in capital:
    print "BC is a province in Canada"


# Adding an element to dicitionary
provinces['Yukon'] = 'YT'
print provinces

# Popping a key from a dictionary
provinces.pop('Yukon')
print provinces
