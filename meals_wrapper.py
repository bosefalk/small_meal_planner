import meals
import sys

# Select four random meals and print them
meal_list = meals.random()
print('\n')
print('\n')
print('\n')
print('Four chosen meals:')
print(meal_list)
print('\n')

allowed_numbers = [1,2,3,4]
selecting = True
while selecting == True:
    user_input = input("select " + str(allowed_numbers) +", All, Exit" + '\n')
    if (user_input == 'Exit'):
        selecting = False
    if (user_input == "All"):
        for i in allowed_numbers:
            meals.update(meal_list, position=i)
        selecting = False
    if (user_input in str(allowed_numbers)):
        meals.update(meal_list, position = int(user_input))
        allowed_numbers.remove(int(user_input))
