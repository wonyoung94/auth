from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        # fields = '__all__'
        exclude = ('user', ) # 동일한 의미 fields = ('title', 'context',)