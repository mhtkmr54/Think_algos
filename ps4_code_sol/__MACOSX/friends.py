import json
from math import radians, cos, sin, asin, sqrt,atan2

#initializing
data = [] #for all friends 
invites = [] # for selected ones

def readjson():
    with open('customers.json') as f:
        for line in f:
            data.append(json.loads(line))
        

def cal_distance(longitude1, latitude1, longitude2, latitude2):
    """
    Convert degrees to radians and then use haversine formula
    """
    longitude1, latitude1, longitude2, latitude2 = map(radians, [longitude1, latitude1, longitude2, latitude2]) 
    # haversine formula 
    difflat = radians(latitude2-latitude1)
    difflon = radians(longitude2-longitude1)
   
    needsqrt = sin(difflat/2) * sin(difflat/2) + cos(radians(latitude1)) * cos(radians(latitude2)) * sin(difflon/2) * sin(difflon/2)
    dsigma = 2 * asin(sqrt(needsqrt))
    radius = 6371 # Radius of the EARTH in kms
    return dsigma * radius

def sort_invites(invites):
    """
    sorting the dictionary using key = user_id
    """
    key = 'user_id'
    to_be_sorted_dict = [(_dictn_[key], _dictn_) for _dictn_ in invites]
    to_be_sorted_dict.sort() #O(nlogn) python uses timsort similar to mergesort (mentioned in the other python file)
    result = [_dictn_ for (key, _dictn_) in to_be_sorted_dict]
    #printing out final results
    for k in xrange(0,len(result)):
        print result[k]['user_id'],result[k]['name']
        
def main():
    readjson() #read json file
    for friend in xrange(0,len(data)):
        #latitude and longitude of the office
        latitude2 = 12.9611159
        longitude2 = 77.6362214
        longitude1 = float(data[friend]['longitude']) #getting longitude
        latitude1 = float(data[friend]['latitude'])  #getting latitude
        distance = cal_distance(longitude1, latitude1, longitude2, latitude2)
        # selecting friends for inviting
        if (distance < float(100)):
            invites.append(data[friend])
           
    sort_invites(invites) #arranging friends according to user_ids
   
if __name__ == "__main__":
    """
    calculate running time  for various function calls using cProfile
    """
    import cProfile
    cProfile.run("main()")
    