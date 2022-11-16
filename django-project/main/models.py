from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=80)
    age = models.IntegerField(blank=True, null=False)
    email = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_created=True)

    def __repr__(self):
        return f'<User {self.first_name} {self.last_name}>'

