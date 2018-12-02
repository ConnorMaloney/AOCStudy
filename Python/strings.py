# Sandbox for messing around with strings
# By Connor Maloney

'''
sandbox_title = """

  ___ _       _              
 / __| |_ _ _(_)_ _  __ _ ___
 \__ \  _| '_| | ' \/ _` (_-<
 |___/\__|_| |_|_||_\__, /__/
                    |___/    
'''

sandbox_art = """
                         ____
                  /^\   / -- )
                 / | \ (____/
                / | | \ / /
               /_|_|_|_/ /
                |     / /
 __    __    __ |    / /__    __    __
[  ]__[  ]__[  ].   / /[  ]__[  ]__[  ]
|__            ____/ /___           __|
   |          / .------  )         |
   |         / /        /          |
   |        / /        /           |
   ---------------------------------
   """
# print(sandbox_art)
#alphabet = 'abcdefghijklmnopqrstuvwxyz'
#print(alphabet)

#rint(len(alphabet))

#Challenge, only get the humps shovel from the sandcastle

# Note: The tip ^ is at position 50.
# Sandbox_art is 443 characters long


# So this is me manually trying it
'''
sandbox_art_shovel2 = sandbox_art[55:61]
print(sandbox_art_shovel2)
print(sandbox_art_shovel2)
print(sandbox_art[25:35])
'''

# I think I can just replace the characters, because the
# shovel has different chars then most of the sandcastle

print(sandbox_art)

# First, replace what we CAN replace safely (characters that shovel does not have)
s_art = sandbox_art
s_art = s_art.replace('\\', ' ') # 2 backslashes escapes backslash
s_art = s_art.replace('|', ' ')
s_art = s_art.replace('^', ' ')
s_art = s_art.replace('[', ' ')
s_art = s_art.replace(']', ' ')
s_art = s_art.replace('.', ' ')
print(s_art)
s_art = s_art[100:300].replace('_', ' ')

#s_art = s_art.replace('_', ' ', 34)
'''
s_art = s_art.replace('.', ' ')
s_art = s_art.replace('/', ' ', 8)
'''
#print(s_art)