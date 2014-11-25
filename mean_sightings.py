import matplotlib.mlab as ml
import numpy as np

def get_sightings(filename, animal):
	
	# Loading table
	tab=ml.csv2rec(filename) # this function converts csv file - knows that line 1 is the headers and 2- is the data

	# Find total number of records for animal and calculate mean sightings
	isfocus=(tab['animal']== animal) #stores as a boulean value- i.e. how many rows match the following criteria
	total_rec=np.sum(isfocus)
	if total_rec == 0:
		meancount=0
	else:
		meancount=np.mean(tab['count'][isfocus]) #This then says, whats the count for each of the matching rows found 2 lines previous
	
	# Return number of records and animals seen
	return total_rec, meancount
	

