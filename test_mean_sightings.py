from mean_sightings import get_sightings


filename = 'sighting_animal.csv'

def test_pig_is_correct():
    pigrec,pigmean = get_sightings(filename,'Pig')
    assert pigrec == 1, 'Number of records for Pig is wrong'
    assert pigmean == 4, 'mean number of pigs is wrong'
    
def test_cow_is_correct():
    cowrec,cowmean = get_sightings(filename,'Cow')
    assert cowrec == 2, 'Number of records for cow is wrong'
    assert cowmean == 17, 'mean number of cows is wrong'
    
def test_anonymous_is_correct():
    anirec,animean = get_sightings(filename,'NotPresent')
    assert anirec == 0, 'Number of anonymous records is wrong'
    assert animean == 0, 'mean for anonymous animal recs is wrong'