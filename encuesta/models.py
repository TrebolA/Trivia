from django.db import models

# Create your models here.

class Pregunta(models.Model):
    id = models.AutoField(primary_key=True)
    enunciado = models.CharField(max_length=50)
    opcion1 = models.CharField(max_length=20)
    opcion2 = models.CharField(max_length=20)
    opcion3 = models.CharField(max_length=20)
    opcion4 = models.CharField(max_length=20)
    
    DIAS = (
        ('0', 'Ninguno'),
        ('1', 'Viernes'),
        ('2', 'Sabado'),
        ('3', 'Domingo'),
        ('4', 'Combo'),
    )
    
    ARTISTAS = (
        ('-', 'Ninguno'),
        ('TK', 'The Killers'),
        ('G', 'Gorillaz'),
        ('LDR', 'Lana Del Rey'),
        ('LCD', 'LCD Soundsystem'),
        ('DJ', 'DJ Snake'),
    )
    
    referencia_dia_opcion_1 = models.CharField(max_length=1, choices=DIAS)
    referencia_artista_opcion_1 = models.CharField(max_length=3, choices=ARTISTAS)
    
    referencia_dia_opcion_2 = models.CharField(max_length=1, choices=DIAS)
    referencia_artista_opcion_2 = models.CharField(max_length=3, choices=ARTISTAS)
    
    referencia_dia_opcion_3 = models.CharField(max_length=1, choices=DIAS)
    referencia_artista_opcion_3 = models.CharField(max_length=3, choices=ARTISTAS)
    
    referencia_dia_opcion_4 = models.CharField(max_length=1, choices=DIAS)
    referencia_artista_opcion_4 = models.CharField(max_length=3, choices=ARTISTAS)
    
    def __str__(self):
        return self.enunciado 