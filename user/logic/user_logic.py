from ..models import User

def create_user(newUserData):
    
    name = newUserData.get('name')
    userName = newUserData.get('userName')
    email = newUserData.get('email')
    password = newUserData.get('password')

    newUser = User.objects.create(name = name, userName = userName, email = email, password=password)

    return newUser