# django-bootstrap-messages

### Goal

The goal of this project is to show how to turn standard [django messages](https://docs.djangoproject.com/en/1.8/ref/contrib/messages/) into pretty [Bootstrap CSS](http://getbootstrap.com/css/) messages, and also allow the User to hide them `onclick` like many modern websites do, and is an expected User experience.

This project demostrates these aspects of **Django**:
  * [django messages](https://docs.djangoproject.com/en/1.8/ref/contrib/messages/)
    * how to add custom tag values to messages -> [here](https://github.com/aronysidoro/django-boostrap-messages/blob/master/bootstrap_message/settings.py#L112)
    * how to reference the tag value to use as a CSS class name -> [here](https://github.com/aronysidoro/django-boostrap-messages/blob/master/templates/django_messages.html#L3)
  * [include template tag](https://docs.djangoproject.com/en/1.8/ref/templates/builtins/#include)
  * [how django uses static files](https://docs.djangoproject.com/en/1.8/howto/static-files/)

This project uses **pure javascript** to hide messages `onclick`, so jQuery is not required.

### Requirements

Must have [django](https://www.djangoproject.com/download/) installed.

### Setup

```
git clone https://github.com/aronysidoro/django-boostrap-messages.git
cd django-bootstrap-messages
./manage.py migrate
```

### License

MIT