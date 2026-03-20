

no = [1,-3,-2,4,-5,6,7,-23,40,60,-56]
positive_num_count = 0
for number in no:
    if(number > 0):
        positive_num_count+=1
        print(number)
print("Final count of positive no. is :",positive_num_count)