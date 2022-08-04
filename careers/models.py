import re

from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToCover

PHRASE_REGEX = re.compile(r'[\s_]')

ACCENTS = [
    ('e', ('é', 'è', 'ë', 'ê')),
    ('o', ('ô', 'ö')),
    ('a', ('à', 'ä', 'â')),
    ('u', ('ü', 'ù','ü', 'û'))
]

def create_slug(phrase: str):
    new_phrase = PHRASE_REGEX.sub(phrase, '-')
    
    def substitute_letter(letter: str):
        for accent in ACCENTS:
            if letter in accent:
                return letter[0]
        return letter

    letters = [substitute_letter(letter) for letter in phrase]
    new_phrase = ''.join(letters)
    return new_phrase.lower()


class Illustration(models.Model):
    url = ProcessedImageField(
        processors=[ResizeToCover(800, 800)]
    )

    def __str__(self):
        return self.url


class Job(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=500)
    illustrations = models.ManyToManyField(Illustration, limit_choices_to=3)
    slug = models.SlugField()
    modified_on = models.DateField(auto_now=True)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def clean(self):
        if self.slug is None:
            title = self.title.lower()
            self.slug = create_slug(self.title)
