mptttreewidget
==============

javascript tree widget for mptt

Usage example
-------------

    from django.contrib import admin
    from django.db import models
    from mptttreewidget.widget import MpttTreeWidget
    
    class ProductAdmin(admin.ModelAdmin):
      formfield_overrides = {
        models.ManyToManyField: { 'widget': MpttTreeWidget }
      }
      
or

    from django.contrib import admin
    from django import forms
    from mptttreewidget.widget import MpttTreeWidget

    class ProductForm(forms.ModelForm)
      categories = forms.ModelMultipleChoiceField(required=False, queryset=Category.objects.all(), widget=MpttTreeWidget)

      class Meta:
          model = Product
    
    class ProductAdmin(admin.ModelAdmin):
      form = ProductForm