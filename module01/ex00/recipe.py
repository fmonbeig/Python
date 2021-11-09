# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fmonbeig <fmonbeig@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/09 17:34:09 by fmonbeig          #+#    #+#              #
#    Updated: 2021/11/09 18:34:34 by fmonbeig         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class recipe:
	def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type    ):
		self.name = name
		if self.name == " ":
			print("name can't be empty")
			exit()
		self.cooking_lvl = cooking_lvl
		try:
			cooking_lvl = int (cooking_lvl)
		except:
			print("ERROR : not an integer")
			exit()
		if self.cooking_lvl < 1 or self.cooking_lvl > 5:
			print("ERROR : lvl not between 1 - 5")
			exit()
		self.cooking_time  = cooking_time
		try:
			cooking_time = int (cooking_time)
		except:
			print("ERROR : not an integer")
			exit()
		if self.cooking_time < 0:
			print("ERROR : time is negative")
			exit()
		self.ingredients  = ingredients
		self.description  = description
		self.recipe_type = recipe_type




recipe1 = recipe("raclette", "d", 20, ["patate", "fromage", "cornichon"],"", "dinner")

print(recipe1.name)
print(recipe1.cooking_lvl)
print(recipe1.ingredients)
print(recipe1.description)
print(recipe1.recipe_type)



#  name (str),
# • cooking_lvl (int): range 1 to 5,
# • cooking_time (int): in minutes (no negative numbers),
# • ingredients (list): list of all ingredients each represented by a string,
# • description (str): description of the recipe,
# • recipe_type (str): can be "starter", "lunch" or "dessert".

# You have to initialize the object Recipe and check all its values, only the description
# can be empty. In case of input errors, you should print what they are and exit properly.
# You will have to implement the built-in method __str__. This is the method that is
# called when the following code is executed
