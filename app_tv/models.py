from django.db import models

class Show(models.Model):
    title = models.CharField(max_length=50)
    network = models.CharField(max_length=50)
    release_date=models.DateField()
    description=models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"< Show: Titulo = {self.title}, Network = {self.network}, Lanzamiento= {self.release_date}, Descripcion= {self.description}>"

