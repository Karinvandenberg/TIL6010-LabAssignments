import math

def variance(data): 
    #number of data points
    number_data = len(data)
    #mean of the data
    mean = sum(data)/number_data
    #square deviation
    deviations = [(p - mean)**2 for p in data]
    #variance
    variance = sum(deviations) / number_data
    return variance
    
def stddev(data):
    #variance of data
    variance_data = variance(data)
    #standard deviation of the data 
    stddev_data = math.sqrt(variance_data)
    return stddev_data

waterhight = ([3,5,8,9])
print(variance(waterhight))
print(stddev(waterhight))
