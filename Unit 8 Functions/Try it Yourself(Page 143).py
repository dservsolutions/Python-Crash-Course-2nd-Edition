# 8.6 City Names
# def city_country(name, country):
#     """Return the name and country of a City"""
#     print(f'"{name.title()}", "{country.title()}"')

# city_country('La Havana', 'Cuba')
# city_country('Colon', 'Panama')
# city_country('Paris', 'France')

# 8.7 Album
def make_album(aname, atitle, nsongs=None):
    music_album = {'artist_name': aname,
                   'album_title': atitle,
                   'number_of_songs': nsongs}
    print(f"{music_album.values()}")

# make_album('dido', 'white flag')
# make_album('coolplay', 'viva la vida')
# make_album('gander', 'rufus du sol')
# make_album('candyman', 'the chinese', 13)

# 8.8 User's Albums

print("Please enter 'quit' to close the program: ")
aname = input("\nEnter the artist name: ")
atitle = input("\nAdd the album title: ")
nsongs = input("\nNumber of songs: ")


while aname == 'quit':
    break
if aname != 'quit':
    make_album(aname, atitle, nsongs)
