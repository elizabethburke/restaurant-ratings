# your code goes here

restaurant_ratings = {}

scores = open("./scores.txt")
for line in scores:
    restaurant, ratings = line.split(":")
    restaurant_ratings[restaurant.strip()] = ratings.strip()


for restaurant in sorted(restaurant_ratings):
    ratings = restaurant_ratings[restaurant]
    print "Restaurant %s is rated at %s" % (restaurant, ratings)



 