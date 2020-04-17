---
description: abstract ideas on Class based views
---

# Django Class based Views\(View\)

A view is a callable which takes a request and returns a response. This can be more than just a function, and Django provides an example of some classes which can be used as views. These allow you to structure your views and reuse code by harnessing inheritance and mixins.

Class-based views provide an alternative way to implement views as Python objects instead of functions. They do not replace function-based views, but have certain differences and advantages when compared to function-based views:

* Organization of code related to specific HTTP methods \(`GET`, `POST`, etc.\) can be addressed by separate methods instead of conditional branching.
* Object oriented techniques such as mixins \(multiple inheritance\) can be used to factor code into reusable components.

### Using class-based views[¶](https://docs.djangoproject.com/en/3.0/topics/class-based-views/intro/#using-class-based-views)

At its core, a class-based view allows you to respond to different HTTP request methods with different class instance methods, instead of with conditionally branching code inside a single view function.

So where the code to handle HTTP `GET` in a view function would look something like:

```text
from django.http import HttpResponse

def my_view(request):
    if request.method == 'GET':
        # <view logic>
        return HttpResponse('result')
```

In a class-based view, this would become:

```text
from django.http import HttpResponse
from django.views import View

class MyView(View):
    def get(self, request):
        # <view logic>
        return HttpResponse('result')
```

Because Django’s URL resolver expects to send the request and associated arguments to a callable function, not a class, class-based views have an [`as_view()`](https://docs.djangoproject.com/en/3.0/ref/class-based-views/base/#django.views.generic.base.View.as_view) class method which returns a function that can be called when a request arrives for a URL matching the associated pattern. The function creates an instance of the class, calls [`setup()`](https://docs.djangoproject.com/en/3.0/ref/class-based-views/base/#django.views.generic.base.View.setup) to initialize its attributes, and then calls its [`dispatch()`](https://docs.djangoproject.com/en/3.0/ref/class-based-views/base/#django.views.generic.base.View.dispatch) method. `dispatch` looks at the request to determine whether it is a `GET`, `POST`, etc, and relays the request to a matching method if one is defined, or raises [`HttpResponseNotAllowed`](https://docs.djangoproject.com/en/3.0/ref/request-response/#django.http.HttpResponseNotAllowed) if not:

```text
# urls.py
from django.urls import path
from myapp.views import MyView

urlpatterns = [
    path('about/', MyView.as_view()),
]
```

 It is worth noting that what your method returns is identical to what you return from a function-based view, namely some form of [`HttpResponse`](https://docs.djangoproject.com/en/3.0/ref/request-response/#django.http.HttpResponse). This means that [http shortcuts](https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/) or [`TemplateResponse`](https://docs.djangoproject.com/en/3.0/ref/template-response/#django.template.response.TemplateResponse) objects are valid to use inside a class-based view.

While a minimal class-based view does not require any class attributes to perform its job, class attributes are useful in many class-based designs, and there are two ways to configure or set class attributes.

The first is the standard Python way of subclassing and overriding attributes and methods in the subclass. So that if your parent class had an attribute `greeting` like this:

```text
from django.http import HttpResponse
from django.views import View

class GreetingView(View):
    greeting = "Good Day"

    def get(self, request):
        return HttpResponse(self.greeting)
```

You can override that in a subclass:

```text
class MorningGreetingView(GreetingView):
    greeting = "Morning to ya"
```

Another option is to configure class attributes as keyword arguments to the [`as_view()`](https://docs.djangoproject.com/en/3.0/ref/class-based-views/base/#django.views.generic.base.View.as_view) call in the URLconf:

```text
urlpatterns = [
    path('about/', GreetingView.as_view(greeting="G'day")),
]
```

### Using mixins[¶](https://docs.djangoproject.com/en/3.0/topics/class-based-views/intro/#using-mixins)

Mixins are a form of multiple inheritance where behaviors and attributes of multiple parent classes can be combined.

### Handling forms with class-based views[¶](https://docs.djangoproject.com/en/3.0/topics/class-based-views/intro/#handling-forms-with-class-based-views)

A basic function-based view that handles forms may look something like this:

```text
from django.shortcuts import render

from .forms import MyForm

def myview(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')
    else:
        form = MyForm(initial={'key': 'value'})

    return render(request, 'form_template.html', {'form': form})
```

A similar class-based view might look like:

```text
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import MyForm

class MyFormView(View):
    form_class = MyForm
    initial = {'key': 'value'}
    template_name = 'form_template.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})
```

This is a minimal case, but you can see that you would then have the option of customizing this view by overriding any of the class attributes, e.g. `form_class`, via URLconf configuration, or subclassing and overriding one or more of the methods \(or both!\).

Decorating class-based views[¶](https://docs.djangoproject.com/en/3.0/topics/class-based-views/intro/#decorating-class-based-views)  


