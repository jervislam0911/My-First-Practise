__author__ = 'jervis'
import django
import os

# In your live server environment, you’ll need to tell your WSGI application what settings file to use
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
from django.contrib.auth.models import User
from django.utils import timezone
# Django version over 1.7 we need the command below
# Otherwise it will throw an error saying django.core.exceptions.AppRegistryNotReady: Models aren't loaded yet.
if django.VERSION >= (1, 7):
    django.setup()


def main():
    from blog.models import post
    file_dir = os.path.dirname(os.path.abspath(__file__))
    file = open(file_dir+'/batchprocessDATA.txt')
    me = User.objects.get(username='jervislam')
    for line in file:
        title, type, text = line.split('****')
        post.objects.get_or_create(title=title, type=type, text=text, author=me, publish_date=timezone.now())
    file.close()


if __name__ == "__main__":
    main()
    print('Done!')


