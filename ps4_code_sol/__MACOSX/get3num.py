import unittest

#O(n^2)  for function get3num

def mergeSort(alist):
    #splitting
    if len(alist)>1:

        mid = len(alist)//2
        #found mid by floor div
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf) #the recursive call after splitting
        mergeSort(righthalf) #the recursive call after splitting
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf): #to be used when index j is out of range of len(righthalf)
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):#to be used when index i is out of range of len(lefthalf)
            alist[k]=righthalf[j]
            j=j+1
            k=k+1


def get3num(arr,num):
    """
    After we sort the array and fix a number according to iteration 
    and start searching for next 2 numbers in the subarray 
    from the 2 ends towards each other 
    """
    print "THE  ARRAY OF NUMBERS",arr
    mergeSort(arr)
    
    print "The Given Sum should be %d" %(num)
    success = 0 #if successfully found 3 numbers
    
    for j in xrange(0,len(arr)-2):
        # the corner end are l an r
        l=0
        r=0
        l = j+1
        r = len(arr)-1
        while (l<r):
            if ( arr[j] + arr[l] + arr[r] == num):
                print "3 numbers are %d %d %d" %(arr[j],arr[l],arr[r]) 
                success = success + 1
                l = l+1
                r = r-1
   
            elif (arr[j] + arr[l] + arr[r] < num):
                l = l+1
                
            elif (arr[j] + arr[l] + arr[r] > num):
                r = r-1
                
    if (success > 0):
        print "Number of times success achieved : ",success
        print "\n"
        return True
    else:
        print "No such 3 numbers"
        print "\n"
        return False 



class MyTest(unittest.TestCase):
    """
    test cases for function get3num with arguments array
    and a given number which can be represented as sum of 3 numbers
    """
    def test1(self):
        self.assertEqual(get3num([1,2,3,4,5,9,6,7,8,10],6), True )
        
    def test2(self):
        self.assertEqual(get3num([1,2,4,5,6,9,10,13,15,20],6), False )
        
    def test3(self):
        self.assertEqual(get3num([5,2,-2,-3,3,0],5), True )
        
    def test4(self):
        self.assertEqual(get3num([-172,-177,-197,-152,-144,-117,-97,-88,-41,-11,8,12,51,56,90,94,149,123,129,101],-200), True )
        
    def test5(self):
        self.assertEqual(get3num([1,-2,3,-4,5,-6,7,-8,9,-10],-3), True )
        
    def test6(self):
        self.assertEqual(get3num([-6 ,-9, -10, -5, 1, -1, 0, -2],-6), True )
        
    def test7(self):
        self.assertEqual(get3num([100,-573,-971,-343,-323,-338 ,12,-21,-331,-471],-1004), True )
        
    def test8(self):
        self.assertEqual(get3num([-1,4,2,1,5,9,0,3,7,-6],2), True )
        
    def test9(self):
        self.assertEqual(get3num([4,0,-2,-1,-3,1,2,3,-4],0), True )
        
    
        
if __name__ == '__main__':
    unittest.main()