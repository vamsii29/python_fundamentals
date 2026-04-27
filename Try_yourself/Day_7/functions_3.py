# Question_1: City Names: Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the value
# that’s returned.
print('\nAnswer')
def city_names(name,country):
    print(f'"{name.title()}, {country.title()}"')

city_names('Bern', 'switzerland')
city_names('Zurich', 'switzerland')
city_names('Chennai', 'India')

# Question_2: Album: Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the
# album information correctly.
# Add an optional parameter to make_album() that allows you to store the
# number of tracks on an album. If the calling line includes a value for the num-
# ber of tracks, add that value to the album’s dictionary. Make at least one new
# function call that includes the number of tracks on an album.

print('\nAnswer')
def make_album(artist,album,num_of_track = ''):
    '''Builds a dictionary of music albums'''
    album_dic ={
       'name_artist' : artist,
       'name_album' : album
    }
    if num_of_track:
      album_dic['track_number'] = num_of_track

    return album_dic

album_1 = make_album('Anirudh','Coolie','6')
print(album_1)
album_2 = make_album('A R Rahman','Peddi')
print(album_2)
album_3 = make_album('Sai','Dude')
print(album_3)


# Question_3: User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.

print('\nAnswer')
def main():
   
   while True:
    artist = input('enter the name of the artist\nenter "q" to exit : ')
    if artist == 'q':
       break
    album = input('\nenter the name of the album\nenter "q" to exit : ')
    if album == 'q':
       break
    track = make_album(artist,album)
    print(f'{track}\n')
   
main()