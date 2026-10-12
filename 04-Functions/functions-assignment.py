'''
Create a function that takes in 3 parameters (firstname, lastname, age) and returns a dictionary based on those values
'''

def c_dict(firstname, lastname, age):
    f_dict = {
        "firstname" : firstname,
        "lastname" : lastname,
        "age" : age
    }

    return f_dict

n_dict = c_dict("Jubaer", "Malick", 25)
print(n_dict)