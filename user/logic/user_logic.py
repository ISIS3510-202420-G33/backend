from ..models import User
from ..models import Artwork

def create_user(newUserData):
    
    name = newUserData.get('name')
    userName = newUserData.get('userName')
    email = newUserData.get('email')
    password = newUserData.get('password')


    try:
        newUser = User.objects.create(name = name, userName = userName, email = email, password=password)
        return newUser

    except:
        return "Problema"
    
def authenticate_user(userData):
    try:
        userName = userData.get('userName')
        password = userData.get('password')
    
        user = User.objects.get(userName=userName)
        
        if user.password == password:
            return user
        else:
            return "PassError"
    except User.DoesNotExist:
        return "UserError"

def like_artwork(data):

    userId = data.get("userId")
    artworkId = data.get("artworkId")

    user = User.objects.get(pk=userId)
    artwork = Artwork.objects.get(pk=artworkId)

    user.likedArtowks.add(artwork)

    return user


def liked_arworks(var_pk):
    user = User.objects.get(pk=var_pk)
    liked = user.likedArtowks.all()

    return liked



def get_users():
    users = User.objects.all()
    return users