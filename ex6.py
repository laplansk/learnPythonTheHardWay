# These declare and instantiate string variables
# in the case of x, %d is replaced by 10
# in the case of y, the first %s is replaced by the value of binary
# and the second is replaced by the value of do_not
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# These put the values of x and y into stdout, which makes
# them display on the console
print x
print y

# self-explanatory at this point
print "I said: %r" % x
print "I also said: '%s'." % y

# this declare a boolean and assigns it the values false
hilarious = False
# This creates a string with a format variable within
# since no value is provided to go in its place, one will be needed
# at its time of use.  Otherwise the actual %r will remain as part of the string
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side"

# This prints the concatenation of the strings w and e
print w + e
