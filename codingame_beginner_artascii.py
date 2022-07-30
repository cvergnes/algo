import sys
import math

rows = []
rows.append(' #  ##   ## ##  ### ###  ## # # ###  ## # # #   # # ###  #  ##   #  ##   ## ### # # # # # # # # # # ### ### ')
rows.append('# # # # #   # # #   #   #   # #  #    # # # #   ### # # # # # # # # # # #    #  # # # # # # # # # #   #   # ')
rows.append('### ##  #   # # ##  ##  # # ###  #    # ##  #   ### # # # # ##  # # ##   #   #  # # # # ###  #   #   #   ## ')
rows.append('# # # # #   # # #   #   # # # #  #  # # # # #   # # # # # # #    ## # #   #  #  # # # # ### # #  #  #       ')
rows.append('# # ##   ## ##  ### #    ## # # ###  #  # # ### # # # #  #  #     # # # ##   #  ###  #  # # # #  #  ###  #  ')

l = 4 
h = 5
t = 'ManHaTtan'
   
for row in rows :
    for letter in t : 
        ascii = ord(letter.upper()) - 65
        if ascii < 0 or ascii >= 26 : 
            ascii = 26
        tmp = list(row)[ascii*l:(ascii+1)*l]
        print( ''.join(tmp), end='')
    print()

