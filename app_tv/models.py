from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self,post_data):
        errors = {}

        if len(post_data['title'])<2:
            errors['title']="El titulo tiene que ser mayor a 2 caracteres"

        if len(post_data['network'])<3:
            errors['network']="La televisora tiene que ser mayor a 3 caracteres"

        if len(post_data['description'])<10:
            errors['description']="La descripcion tiene que ser mayor a 10 caracteres"

        return errors
    


class Show(models.Model):
    title = models.CharField(max_length=50)
    network = models.CharField(max_length=50)
    release_date=models.DateField()
    description=models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=ShowManager()

    def __repr__(self):
        return f"< Show: Titulo = {self.title}, Network = {self.network}, Lanzamiento= {self.release_date}, Descripcion= {self.description}>"

