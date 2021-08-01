from django import forms

class NewBookForm(forms.Form):
    title=forms.CharField(label='Title',max_length=100,label_suffix='  ',widget=forms.TextInput(attrs={'placeholder':'Enter book title','id':'title'}))
    author=forms.CharField(label='Author',max_length=100,label_suffix='  ',widget=forms.TextInput(attrs={'placeholder':'Author name','id':'author'}))
    price=forms.CharField(label='Price',label_suffix='  ',widget=forms.TextInput(attrs={'placeholder':'Book Price','id':'price'}))
    publisher=forms.CharField(label='Publisher',max_length=100,label_suffix='  ',widget=forms.TextInput(attrs={'placeholder':'Book publisher','id':'publisher'}))


class SearchForm(forms.Form):
    title=forms.CharField(label="Title",max_length=100)
