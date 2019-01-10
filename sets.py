#Create an empty set named showroom.
#Add four of your favorite car model names to the set.
#Print the length of your set.
#Pick one of the items in your show room and add it to the set again.
#Print your showroom. Notice how there's still only one instance of that model in there.
#Using update(), add two more car models to your showroom with another set.
#You've sold one of your cars. Remove it from the set with the discard() method.

#1
showroom = set()
#2
showroom.add('supra')
showroom.add('gtr')
showroom.add('rsx')
showroom.add('string ray')
#3
print("The length of my showroom list is " + str(len(showroom)))
#4
showroom.add('supra')
#5
print("showroom after adding existing car", showroom)
#6
showroom.update('batmobile')
showroom.update('hot dog car')
print("showroom after using update", showroom)
#7
showroom.discard('supra')
print("showroom after using discard", showroom)