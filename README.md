# Django Kikeou

A Django app to handle your festival.

WARNING: status of the project is currently not stable => contact us if you want to have a try

## Setup your own Kikeou project

- Make sure you installed django-kikeou module with `pip install django-kikeou` 
- Create a Django project (more info: https://docs.djangoproject.com/fr/4.0/intro/tutorial01/)
- Make sure you set up a database for your django project
- Add kikeou app in your installed apps (settings.py)
    ```
    INSTALLED_APPS = [
      ...
      "kikeou",
      ...  # add your django apps
    ]
    ```
- Minimum urls in your main urls.py
    ```
    from django.contrib import admin
    from django.urls import include, path
  
    urlpatterns = [
        path("admin/", admin.site.urls),
        path("accounts/", include(("django.contrib.auth.urls", "accounts"), namespace="accounts")),
        path("", include((kikeou.urls, "kikeou"), namespace="kikeou")),  # not necessarily root
    ]
    ```


## Developers - Help us to hack django-kikeou

### Tests

We do our best to test the features as best as we can and to keep full test coverage.
Before to create your pull request, please run the tests as follow and make sure you cover your code.

```bash
coverage run manage/run_tests.py
coverage report
```
