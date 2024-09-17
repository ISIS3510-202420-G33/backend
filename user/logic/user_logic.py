from ..models import User

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