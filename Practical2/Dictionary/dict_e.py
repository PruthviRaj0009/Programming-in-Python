#20CS068
#Pruthvi Raj
# e. Write a Python script to concatenate following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

#function to concatenate following dictionaries
def concatenatedict(dicts):
    Result = {}
    for dict in dicts:
        for key in dict.keys():
            Result[key] = dict[key]
    return Result

dic1={1:10, 2:20}

dic2={3:30, 4:40}

dic3={5:50,6:60}

Result = concatenatedict([dic1,dic2,dic3])
#printing Result
print(Result)