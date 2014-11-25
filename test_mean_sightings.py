from mean_sightings import get_sightings

filename = 'sightings_animal.csv'

def test_pig_is_correct():
	pigrec, pigmean = get_sightings(filename, 'Pig')
	assert pigrec == 1, 'Number of records for Pig is wrong'
	assert pigmean == 4, 'mean sightings for pig is wrong'

def test_cow_is_correct():
	cowrec, cowmean = get_sightings(filename, 'Cow')
	assert cowrec == 2, 'Number of cow is wrong'
	assert cowmean == 22, 'Mean sightings for cow is wrong'

def test_lion_is_correct():
        lionrec, lionmean = get_sightings(filename, 'Lion')
        assert lionrec == 2, 'Number of lion is wrong'
        assert lionmean == 25.5, 'Mean sightings for lion is wrong'

def test_anonymous_is_correct():
	anirec, animean = get_sightings(filename, 'NotPresent')
	assert anirec == 0,'Number of anonymous records is wrong'
	assert animean == 0, 'Mean of anonymous animal recs is wrong'
