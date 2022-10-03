# from faker import Faker
# import json
 
# #Declare faker onject
# fake = Faker()
 
# def generate_user_data(records):
#     #Declare an empty dictionary
#     users = []
#     user ={}
#     #Iterate the loop based on the input value and generate fake data
#     for n in range(0, records):
#         new_user =  User(
#                 id =  fake.random_number(digits=5),
#                 name = fake.name(),
#                 email= fake.address(),
#                 address = str(fake.email())
#                 phone_number= str(fake.phone_number())
#                 )
#         new_user.save()
 
#     #Write the data into the JSON file
#     with open('users.json', 'w') as fp:
#         json.dump(users, fp)
 
#     print("File has been created.")
    
# def main():
#     return generate_user_data(1000)

# if __name__=='__main__':
#     main()
