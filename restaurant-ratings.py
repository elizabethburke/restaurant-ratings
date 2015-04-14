# your code goes here

restaurant_ratings = {}

scores = open("./scores.txt")
for line in scores:
    restaurant, ratings = line.split(":")
    restaurant_ratings[restaurant.strip()] = ratings.strip()


for restaurant in sorted(restaurant_ratings):
    ratings = restaurant_ratings[restaurant]
    print "Restaurant %s is rated at %s" % (restaurant, ratings)

for restaurant in sorted(restaurant_ratings):
    ratings = restaurant_ratings[restaurant]
    print "Please tell us what your favorite restaurant is."
    restaurant = raw_input()
    print "What rating would you give to this restaurant?"
    ratings = int(raw_input())
    restaurant_ratings[restaurant] = ratings 

    print restaurant 
    print ratings 
    print restaurant_ratings

    
  


