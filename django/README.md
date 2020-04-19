---
description: Basics
---

# Django Views

Views:  mainly 2 types

1\) Function based view\(ok\)

2\) Class based view: 3 types

------------------------------------------------------------------------------------------------------------

1\) Base views\(ok\)

2\) Generic display view

3\) Generic editing view

------------------------------------------------------------------------------------------------------------

Base  views: 3 types

1\) view\(ok\) - generic one

2\) Redirect view 

3\) Template view - to render template

------------------------------------------------------------------------------------------------------------

Generic display view : 3 types

1\) List view\(ok\)

2\) Detail view\(ok\)

------------------------------------------------------------------------------------------------------------

Generic editing view: 4 types

1\) Form view - A view that displays a form. On error, redisplays the form with validation errors; on success, redirects to a new URL.

2\) Create view

3\) update view - A view that displays a form for editing an existing object, redisplaying the form with validation errors \(if there are any\) and saving changes to the object. This uses a form automatically generated from the object’s model class \(unless a form class is manually specified\).

4\) Delete view -  A view that displays a confirmation page and deletes an existing object. The given object will only be deleted if the request method is `POST`. If this view is fetched via `GET`, it will display a confirmation page that should contain a form that POSTs to the same URL.





