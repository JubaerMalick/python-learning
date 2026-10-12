'''
Given the variable my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
Create a while loop that prints all elements of the my_list variable 3 times
When printing the elements use a for loop to print the elemenrts
However, if the element of the for loop is equal to monday, continue without printing
'''
my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
i = 0

while(i<3):
    i += 1
    print("---------")
    for day in my_list:
        if (day == "Monday"):
            continue
        
        print(day)