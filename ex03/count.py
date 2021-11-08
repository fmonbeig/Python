# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fmonbeig <fmonbeig@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/08 15:29:00 by fmonbeig          #+#    #+#              #
#    Updated: 2021/11/08 18:09:00 by fmonbeig         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

def text_analyzer(*args):

	""" A function who give you how many upper / lower / space
		and punctuation there is"""

	print(len(args))
	if len(args) > 1:
		print("ERROR : Too much argument")
		exit ()
	if  len(args) == 0 or len(args[0]) == 0:
		str = input("Please enter text :\n")
		total = len(str)
		upper = sum(1 for c in str if c.isupper())
		lower = sum(1 for c in str if c.islower())
		space = sum(1 for c in str if c.isspace())
		punctuation = 0
		for i in str:
			if i in string.punctuation:
				punctuation += 1
		print("The text contains", total, "characters:")
		print("-", upper, "upper letters")
		print("-", lower, "lower letters")
		print("-", punctuation, "punctuation marks")
		print("-", space, "spaces")
	else :
		total = len(args[0])
		upper = sum(1 for c in args[0] if c.isupper())
		lower = sum(1 for c in args[0] if c.islower())
		space = sum(1 for c in args[0] if c.isspace())
		punctuation = 0
		for i in args[0]:
			if i in string.punctuation:
				punctuation += 1
		print("The text contains", total, "characters:")
		print("-", upper, "upper letters")
		print("-", lower, "lower letters")
		print("-", punctuation, "punctuation marks")
		print("-", space, "spaces")

##########################
#          MAIN          #
##########################

#text_analyzer("")


