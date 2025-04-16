"""Django ORM Practice - Read Example"""

from core.models import Post


# 1. Get all posts.
all_posts = Post.objects.all()
print(f'All Post Objects: {all_posts}')
print('All Posts:')
for post in all_posts:
    print(f'({post.post_no}) Title: {post.title} / Content: {post.content} / Author: {post.author.username}')
print('\n')


# 2. Get a single post by number.
post_no = 3
try:
    post = Post.objects.get(post_no=post_no)
    print(f'Single Post Object: {post}')
    print('Single Post:')
    print(f'({post.post_no}) Title: {post.title} / Content: {post.content} / Author: {post.author.username}')
except Post.DoesNotExist:
    print(f'Post number {post_no} does not exist.')
print('\n')


# 3. Get a multiple posts by filtering.
filtered_posts = Post.objects.filter(title__icontains='post')
print(f'Filtered Post Objects: {filtered_posts}')
print('Filtered Posts:')
for post in filtered_posts:
    print(f'({post.post_no}) Title: {post.title} / Content: {post.content} / Author: {post.author.username}')
print('\n')
