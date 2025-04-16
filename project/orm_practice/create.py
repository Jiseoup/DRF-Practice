"""Django ORM Practice - Create Example"""

from core.models import User, Post


# Replace `admin` with your superuser username.
USERNAME = 'admin'
MY_SUPERUSER = User.objects.get(username=USERNAME)


# 1. Create a post directly using field values.
"""Create a post directly using field values."""
Post.objects.create(
    title='First post title.',
    content='First post content.',
    author=MY_SUPERUSER,
)
print('First post created successfully.')


# 2. Create a post by unpacking a dictionary.
dict_post = {
    'title': 'Second post title.',
    'content': 'Second post content.',
    'author': MY_SUPERUSER,
}
Post.objects.create(**dict_post)
print('Second post created successfully.')


# 3. Create a post using the `save()` method.
my_post = Post(
    title='My favorite foods.',
    content='I love pizza and pasta.',
    author=MY_SUPERUSER,
)
my_post.save()
print('Third post created successfully.')
