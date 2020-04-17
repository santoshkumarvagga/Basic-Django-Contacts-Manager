---
description: >-
  Class based Generic views - provide interfaces to perform the most common
  tasks developers Detailview-Basically provides all detailed view of particular
  entity adds, extra context to that of Listview
---

# Class based Generic view - Detailview

Often you need to present some extra information beyond that provided by the generic view. For example, think of showing a list of all the books on each publisher detail page. The [`DetailView`](https://docs.djangoproject.com/en/3.0/ref/class-based-views/generic-display/#django.views.generic.detail.DetailView) generic view provides the publisher to the context, but how do we get additional information in that template?

The answer is to subclass [`DetailView`](https://docs.djangoproject.com/en/3.0/ref/class-based-views/generic-display/#django.views.generic.detail.DetailView) and provide your own implementation of the `get_context_data` method. The default implementation adds the object being displayed to the template, but you can override it to send more:

```text
from django.views.generic import DetailView
from books.models import Book, Publisher

class PublisherDetail(DetailView):

    model = Publisher

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = Book.objects.all()
        return context
```



