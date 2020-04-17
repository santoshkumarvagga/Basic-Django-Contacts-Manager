---
description: >-
  Class based Generic views - provide interfaces to perform the most common
  tasks developers encounter. Listview - basically lists all objects of
  particular class rendered.
---

# Class based Generic view - Listview

### Generic views of objects[¶](https://docs.djangoproject.com/en/3.0/topics/class-based-views/generic-display/#generic-views-of-objects)

[`TemplateView`](https://docs.djangoproject.com/en/3.0/ref/class-based-views/base/#django.views.generic.base.TemplateView) certainly is useful, but Django’s generic views really shine when it comes to presenting views of your database content. Because it’s such a common task, Django comes with a handful of built-in generic views to help generate list and detail views of objects.

Let’s start by looking at some examples of showing a list of objects or an individual object.

We’ll be using these models:

```text
# models.py
from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name

class Author(models.Model):
    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='author_headshots')

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()
```

Now we need to define a view:

```text
# views.py
from django.views.generic import ListView
from books.models import Publisher

class PublisherList(ListView):
    model = Publisher
```

Finally hook that view into your urls:

```text
# urls.py
from django.urls import path
from books.views import PublisherList

urlpatterns = [
    path('publishers/', PublisherList.as_view()),
]
```

 This template will be rendered against a context containing a variable called `object_list` that contains all the publisher objects. A template might look like this:

```text

{% extends "base.html" %}

{% block content %}
    <h2>Publishers</h2>
    <ul>
        {% for publisher in object_list %}
            <li>{{ publisher.name }}</li>
        {% endfor %}
    </ul>
{% endblock %}
```

That’s really all there is to it. All the cool features of generic views come from changing the attributes set on the generic view. The [generic views reference](https://docs.djangoproject.com/en/3.0/ref/class-based-views/) documents all the generic views and their options in detail; the rest of this document will consider some of the common ways you might customize and extend generic views.

#### Making “friendly” template contexts[¶](https://docs.djangoproject.com/en/3.0/topics/class-based-views/generic-display/#making-friendly-template-contexts)

`object_list` or `publisher_list` also can be available from django side.

```text
# views.py
from django.views.generic import ListView
from books.models import Publisher

class PublisherList(ListView):
    model = Publisher
    context_object_name = 'my_favorite_publishers'
```

Providing a useful `context_object_name` is always a good idea. Your coworkers who design templates will thank you.  


