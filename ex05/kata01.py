# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fmonbeig <fmonbeig@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/09 10:52:18 by fmonbeig          #+#    #+#              #
#    Updated: 2021/11/09 11:10:51 by fmonbeig         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

languages = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

for x in languages:
        print(x, "was created by", languages[x])