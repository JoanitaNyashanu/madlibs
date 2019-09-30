# MadLibs - Practice Input and Output
#
# Template:
#    I enjoy practice! I find it helps me to __(verb)__ better.
#    Without practice, my __(noun)__ would probably not even work.
#    My code is getting more __(adjective)__ every single day!


# TODO: Prompt the user for parts of speech and store them in variables
my_verb = input("Pease enter a verb: ")
my_noun = input("Pease enter a noun: ")
my_adjective = input("Pease enter an adjective: ")

template = "I enjoy practice. I find that it helps me to {} better. Without practice, my {} would probably not even work. My code is getting more {} every single day!".format(my_verb, my_noun, my_adjective)
print(template)

# TODO: Output the template to the screen with the blanks filled out with what the user stated
print(template)
