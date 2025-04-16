"""Django ORM Practice - Delete Example"""

from core.models import Post


# 1. Delete posts using the `delete()` method.
all_posts = Post.objects.all()
posts = all_posts.filter(title__icontains='post')

print('Before Delete:')
for post in all_posts:
    print(f'({post.post_no}) Title: {post.title} / Content: {post.content}')

# Delete posts with `delete()` method.
posts.delete()

# Get all posts after deletion.
all_posts = Post.objects.all()

print('After Delete:')
for post in all_posts:
    print(f'({post.post_no}) Title: {post.title} / Content: {post.content}')
