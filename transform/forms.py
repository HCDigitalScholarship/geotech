from django import forms
from django.db import models
from django.core.files.storage import FileSystemStorage

import random


class FileForm(forms.Form):
    your_file = forms.FileField(label='Your file', max_length=100, required=False)
