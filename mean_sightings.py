import matplotlib.mlab as ml
import numpy as np


def get_sightings(filename,ani):

    #Loading table
    tab = ml.csv2rec(filename)
    
    #Allow for case insensitivity
    ani=ani.capitalize();
    
    #Find total number of records for animals and calculate mean sightings
    isfocus = (tab['animal'] == ani)					#Check the input animal matches that in the library
    total_records = np.sum(isfocus)
    
    if total_records == 0:
	meancount = 0							#Mean is zero if the list is zero size
    else:
        meancount = np.mean(tab['count'][isfocus])			#Only uses the numbers if the animals match
    
    #return number of records and animals seen
    return total_records,meancount