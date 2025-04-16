"""Django ORM Practice - Update Example"""

from core.models import Post


# 1. Update posts using the `update()` method.
posts = Post.objects.filter(title__icontains='post')
print('Before Update:')
for post in posts:
    print(f'({post.post_no}) Title: {post.title} / Content: {post.content}')

# Update posts with `update()` method.
posts.update(content='Updated content.')

print('After Update:')
for post in posts:
    print(f'({post.post_no}) Title: {post.title} / Content: {post.content}')

print('\n')


# 2. Update posts using the `save()` method.
posts = Post.objects.filter(title__icontains='post')
print('Before Update:')
for post in posts:
    print(f'({post.post_no}) Title: {post.title} / Content: {post.content}')

# Update posts with `save()` method.
for post in posts:
    post.content = f'The post number is {post.post_no}.'
    post.save()

print('After Update:')
for post in posts:
    print(f'({post.post_no}) Title: {post.title} / Content: {post.content}')

print('\n')
