"""
***************************************
*        Boilerplate Generator        *
*  Created by: Tommy H. Yeargin, Jr.  *
*            July 3, 2022             *
***************************************

This is the first version of this app, written in Python3,
which generated a boilerplate for your app like the one
above. It still needs to be tweaked some, to put enough
padding around each element, but at this time, you can just
add another space manually when you paste the generated
boilerplate to your app. Thank you for your support, and
may God bless!

"""

title_bp = input("Title of app: ")
author_bp = input("Your name: ")
author_bp = "Created by: " + author_bp
date_bp = input("Today's date: ")

dict_bp = {
	title_bp: len(title_bp),
	author_bp: len(author_bp),
	date_bp: len(date_bp)
}

max_value = max(dict_bp, key=dict_bp.get)

max_value = len(max_value)+4

title_space_bp = int((max_value - len(title_bp))/2)
author_space_bp = int((max_value - len(author_bp))/2)
date_space_bp = int((max_value - len((date_bp)))/2)
hor_border_bp = "*"*(max_value+2)

print(hor_border_bp)
print("*" + (" " * title_space_bp) + title_bp + (" " * title_space_bp) + "*")
print("*" + (" " * author_space_bp) + author_bp + (" " * author_space_bp) + "*")
print("*" + (" " * date_space_bp) + date_bp + (" " * date_space_bp) + "*")
print(hor_border_bp)
