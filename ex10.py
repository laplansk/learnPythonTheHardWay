__author__ = 'laplansk'

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# some escaped characters

print "\\ \' \" \a \b \f"

while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r",