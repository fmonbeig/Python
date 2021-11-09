# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fmonbeig <fmonbeig@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/08 14:24:45 by fmonbeig          #+#    #+#              #
#    Updated: 2021/11/08 15:26:57 by fmonbeig         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def whois(x):
	if x == 0:
		print("I'm Zero.")
	elif x % 2 == 0:
		print("I'm Even.")
	else:
		print("I'm Odd.")

##########################
#          MAIN          #
##########################

if len(sys.argv) > 2:
	print("ERROR : Too much argument")
elif len(sys.argv) == 2:
	if (sys.argv[1][0] == '-'):
		if (sys.argv[1][1:].isnumeric() == True):
			x = int (sys.argv[1])
			whois(x)
		else:
			print("ERROR : Not an int")
	elif (sys.argv[1].isnumeric() == True):
		x = int (sys.argv[1])
		whois(x)
	else:
		print("ERROR : Not an int")
		exit()
else:
	exit()

