#this is an algorithm retuns the peak element in an array.
#a peak element is the largest value in an array compared to its neighbors
def findPeakInMountainArray(arr):
    arr.sort()
    l=1
    h=len(arr)-2
    while True:
        mid = l + int((h-l)/2)
        if arr[mid-1]<arr[mid]<arr[mid+1]:
            l = mid +1
        elif arr[mid-1]>arr[mid]>arr[mid+1]:
            h = mid-1
        else:
            return "array is {} and the largest peak element is {} at index {}".format(arr,arr[mid],mid)
print(findPeakInMountainArray([1,3,6,3,2]))