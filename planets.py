planets = [{'name':'Mercury', 'position':1, 'moons':0, 'rings':False},
           {'name':'Venus', 'position':2, 'moons':0, 'rings':False}, 
           {'name':'Earth', 'position':3, 'moons':1, 'rings':False}, 
           {'name':'Mars', 'position':4, 'moons':2, 'rings':False}, 
           {'name':'Jupiter', 'position':5, 'moons':6, 'rings':True}, 
           {'name':'Saturn', 'position':6, 'moons':6, 'rings':True}, 
           {'name':'Uranus', 'position':7, 'moons':2, 'rings':True}, 
           {'name':'Neptune', 'position':8, 'moons':1, 'rings':True}
          ]

def find_ringed_planets(planets):
    """ Find all planets that have rings around them. """
    return filter(lambda p: p['rings'], planets)

def find_mooned_planets(planets):
    """ Find all planets that have rings around them. """
    return filter(lambda p: p['moons'] > 0, planets)
	
if __name__ == '__main__':
    print(planets)
	