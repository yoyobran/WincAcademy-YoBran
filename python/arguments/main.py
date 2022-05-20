# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


# Part 1: Greet Template

def greet(name, greeting_template="Hello, <name>!"):
 
   """ greet should return a string
   where <name> in the greeting template is replaced by the name given in the first parameter.
   Greet these arguments
   A name ( str )
   A greeting template ( str )
   """
   greeting_template = greeting_template.replace("<name>", name)
   return greeting_template
 
# test function greet
print(greet(" Bobbie"))


# Part 2: Force

# function force 
# two arguments
# mass ( float )  
# body ( str ), with 'earth' as its default
# process these bodies with the correlated gravity factor in a dictionary.

def force(mass=0.0, body='earth'):

	""" define a dictonairy with the gravities of the planets and the sum of
	from https://www.smartconversion.com/otherInfo/gravity_of_planets_and_the_sun.aspx"""

	gravities = dict( 
		sun =274, 
		jupiter	= 24.92, 
		neptune	= 11.15,
		saturn = 10.44,
		earth	= 9.798,
		uranus =	8.87,
		venus	= 8.87,
		mars =	3.71,
		mercury	= 3.7,
		moon =	1.62,
		pluto =	0.58
	)

	# convert to 1 decimal,  not really necessary, but for testing
	gravities = {key : round(gravities[key], 1) for key in gravities}

	# calculate the grafity force
	force_planet = round(float(mass)*gravities[body], 1)


	return force_planet


# test function force
print(force(3000, "moon"))



# Part 3: Gravity

"""Write a function pull that takes three arguments:
m1 An object's mass in kg (float)
m2 Another object's mass in kg (float)
d Their distance in meters (float)
"""

def pull (massa1: float, massa2: float, distance: float):
	gravitational_constant = (6.674 * 10**-11)
	pull_power = gravitational_constant * ((massa1 * massa2)/ distance**2)
	return pull_power

# test function pull
print(pull( 5000, 6000, 2000))


