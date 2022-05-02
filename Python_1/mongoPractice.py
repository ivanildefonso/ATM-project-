from pymongo import mongo_client

client = mongo_client()

#setting db_week4 to our week4 db on Mongodb
db_week4 = client.week4 

movies = db_week4.movies

movie = movies.find_one({'title' : 'Fight Club'})

print(movie)


