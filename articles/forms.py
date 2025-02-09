from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
    
    def clean(self):
        data = self.cleaned_data   
        title = data.get('title')
        qs = Article.objects.filter(content__contains=title)
        if qs.exists():
            self.add_error('title', 'This title is already taken. Please try another one.')

    

class ArticleFormOld(forms.Form):
    title = forms.CharField(label='Title')
    content = forms.CharField(label='Content', widget=forms.Textarea)

    def clean_title(self):
        cleaned_data = self.cleaned_data
        print("cleaned_data", cleaned_data) 
        title = cleaned_data.get('title')
        print("title", title)
        return title

    