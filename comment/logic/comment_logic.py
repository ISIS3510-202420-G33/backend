from ..models import User
from ..models import Comment
from ..models import Artwork


def comment_create(data):

    content = data.get('content')
    date = data.get('date')
    artworkId = data.get('artwork')
    userId = data.get('user')

    user = User.objects.get(pk = userId)
    artwork = Artwork.objects.get(pk = artworkId)

    newComment = Comment.objects.create(content = content, date = date, artwork = artwork, user = user)

    comment = Comment.objects.get(pk = newComment.pk)

    return comment
