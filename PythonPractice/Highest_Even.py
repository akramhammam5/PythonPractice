def highest_even(li):
    for number in li:
        maximum = max(li)
        if number % 2 == 0 and maximum - number <= 1: 
            print(number)                
highest_even([1,2,3,4,5,6,7,8,9,10])             
