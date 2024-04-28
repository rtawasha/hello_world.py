# 1. TASK: print "Hello World"
print("hello Damn fucking world: Worthless full of bastards!") 

# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print("Hello", name)		
print("Hello" + name)	

# 3. print "Hello 42!" with the number in a variable
name = "42"
print("Hello", name)		
print("Hello" + name)				    # TypeError: can only concatenate str (not "int") to str 	
                                        # prior to making 42 a string...

# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}".format(fave_food1, fave_food2))
print(f"I love to eat {fave_food1} and {fave_food2}")
print("I love to eat %s and %s" %(fave_food1, fave_food2))

# 5. Store 2 of your favorite foods in variables, and then use them to print the string use f-strings (#4b)
intro = "I love eating in general especially"
fave_food3 = "falafel"
fave_food4 = "shawerma"
print(f"{intro} {fave_food3} and {fave_food4}")

