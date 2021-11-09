# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fmonbeig <fmonbeig@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/09 16:15:32 by fmonbeig          #+#    #+#              #
#    Updated: 2021/11/09 17:09:28 by fmonbeig         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


#Pas fini j' ai juste enlever la ponctuation

import sys
import string

try:
	words = str(sys.argv[1])
	len = int(sys.argv[2])
except:
	print("ERROR")
	exit()

for i in string.punctuation:
	words = words.replace(i, '')

words = words.split(' ')



print(words)


