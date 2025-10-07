from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

class Video(models.Model):
    GENRE_CHOICES = [
        ('COMEDY','Comedy'), ('ROMANCE','Romance'), ('ACTION','Action'),
        ('DRAMA','Drama'), ('THRILLER','Thriller'), ('SCIFI','Sci-Fi'),
        ('HORROR','Horror'), ('OTHER','Other'),
    ]

    MovieID       = models.CharField(max_length=20, unique=True)
    MovieTitle    = models.CharField(max_length=200)
    Actor1Name    = models.CharField(max_length=120)
    Actor2Name    = models.CharField(max_length=120, blank=True)
    DirectorName  = models.CharField(max_length=120)
    MovieGenre    = models.CharField(max_length=20, choices=GENRE_CHOICES)
    ReleaseYear   = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1888),
            MaxValueValidator(datetime.date.today().year + 1)
        ]
    )

    class Meta:
        ordering = ['-ReleaseYear','MovieTitle']

    def __str__(self):
        return f"{self.MovieTitle} ({self.ReleaseYear})"

# Create your models here.
