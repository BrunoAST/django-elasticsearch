from django.urls import path
from demo.apis import HelloApi


urlpatterns = [
    path('hello/', HelloApi.as_view(), name='hello')
]
