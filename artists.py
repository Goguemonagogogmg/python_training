import albumsartists as al
import random

# artist=input("entrer le nom de votre artiste préféré:")

# al.album(artist)


# artist_album=input("entrer votre album préféré pour voir ces titres:")

# al.title(artist,artist_album)

artist=list(al.Artists.artists["gims"]["ceinture noire"])

print(("\n").join((random.choices(artist,weights=None,cum_weights=None,k=9))))

# print(random.choice(['red','black','white','green','brown']))