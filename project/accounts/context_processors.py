from .models import Avatar

def user_avatar(request):
    avatar = None
    if request.user.is_authenticated:
        print(request.user)
        avatar = Avatar.objects.filter(user=request.user).last()
    return {'user_avatar': avatar}