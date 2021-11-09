# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fmonbeig <fmonbeig@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/09 12:16:31 by fmonbeig          #+#    #+#              #
#    Updated: 2021/11/09 16:14:15 by fmonbeig         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

cookbook = {
	'sandwich' : {
	"ingredient" : ["ham", "bread", "cheese", "tomatoes"],
	'meal' : 'lunch',
	'prep_time' : ' 10 ',
	},
	'cake' : {
	'ingredient' : ["flour", "sugar", "eggs"],
	'meal' : 'dessert',
	'prep_time' : ' 60 ',
	},
	'salad' : {
	'ingredient' : ["avocado", "arugula", "tomatoes", "spinach"],
	'meal' : 'lunch',
	'prep_time' : ' 10 ',
	}
}

def print_recipe(recipe):

	if recipe in cookbook:
		print(f"Recipe for {recipe}:")
		print(f"Ingredients list :{cookbook[recipe]['ingredient']}")
		print(f"To be eaten for {cookbook[recipe]['meal']}.")
		print(f"Take {cookbook[recipe]['prep_time']} minutes of cooking.")

	else :
		print("Sorry, recipe not found")

def delete_recipe(recipe):

	if recipe in cookbook:
		del cookbook[recipe]
	else:
		print("Sorry, recipe not found")

def add_recipe(recipe, ingredients, meal, prep_time):

	temp = { recipe : {
		"ingredient" : ingredients,
		"meal" : meal,
		"prep_time" : prep_time
					}
	}
	cookbook.update(temp)

def print_cookbook():

	for i in cookbook:
		print_recipe(i)
		print("\n")

def take_choice():

	while (1):
		tmp = input("\nYour choice :")
		if (tmp.isnumeric() == True):
			tmp = int(tmp)
			if (tmp < 1 or tmp > 5):
				print("Not a good number")
				continue
			else:
				return tmp
		else:
			print("Not number...")
			continue


##########################
#          MAIN          #
##########################

tmp = 0
while tmp != 5:
	print("\n=============================================")
	print("Please select an option by typing the corresponding number:")
	print("1: Add a recipe")
	print("2: Delete a recipe")
	print("3: Print a recipe")
	print("4: Print the cookbook")
	print("5: Quit")

	tmp = take_choice()
	if (tmp == 1):
		name = input("What is the name of the recipe ?\n")
		ingredient = input ("List the ingredients for the recipe, each one separate by a ,\n")
		ingredient = ingredient.split(", ")
		meal = input ("For what moment is your meal ?\n")
		prep_time = input ("How many time for preparation?\n")
		add_recipe(name, ingredient, meal, prep_time)
	elif (tmp == 2):
		recipe = input("Please enter the recipe's you want to DELETE\n")
		delete_recipe("cake")
	elif (tmp == 3):
		recipe = input("Please enter the recipe's name to get its details:\n")
		print_recipe(recipe)
	elif (tmp == 4):
		print_cookbook()

print("Cookbook closed")
