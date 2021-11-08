# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fmonbeig <fmonbeig@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/08 18:10:05 by fmonbeig          #+#    #+#              #
#    Updated: 2021/11/08 18:43:06 by fmonbeig         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def	check_arg(*args):

	i = 1
	while i < 3:
		if (sys.argv[i][0] == '-'):
			if (sys.argv[i][1:].isnumeric() == False):
				return False
		elif (sys.argv[i].isnumeric() == False):
				return False
		i += 1
	return True

def	operations(x, y):

	print("Sum:       ", x + y)
	print("Difference:", x - y)
	print("Product:   ", x * y)
	if y == 0:
		print("ERROR (div by zero)")
	else:
		print("Quotient:  ", x / y)
	if y == 0:
		print("ERROR (modulo by zero)")
	else:
		print("Remainder: ", x % y)

##########################
#          MAIN          #
##########################

if len(sys.argv) > 3:
	print("ERROR : Too many arguments")
	exit ()
elif len(sys.argv) < 3:
	print("Usage: python operations.py <number1> <number2>")
	exit ()
else :
	if check_arg() == True:
		x = int (sys.argv[1])
		y = int (sys.argv[2])
	elif check_arg() == False:
		print("ERROR : not an integer")
		exit ()
operations(x, y)
