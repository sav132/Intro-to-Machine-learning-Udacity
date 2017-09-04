#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = open("../final_project/poi_names.txt","r")
##email_addr = open("../final_project/poi_email_addresses.py","r")

count =0


for names in enron_data:
	
	
	if(names[1:2] =='y' or names[1:2] =='n'):
		count+=1

print(count)
