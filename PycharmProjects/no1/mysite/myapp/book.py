from django.forms import ModelForm
from .models import Book

class ArticleForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title','author','publisher','publication_date']
fom = ArticleForm()
print(fom)