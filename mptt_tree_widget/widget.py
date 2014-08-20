from django import forms
from django.template.loader import render_to_string
#from itertools import chain
#from django.utils.safestring import mark_safe
from django.conf import settings

class MpttTreeWidget(forms.SelectMultiple):
    def __init__(self, attrs=None):
        super(MpttTreeWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None, choices=()):
        return render_to_string('MpttTreeWidget.html',
                {'queryset': self.choices.queryset, 'STATIC_URL': settings.STATIC_URL, 'name': name, 'value': value,
                 'attrs': attrs})

    class Media:
        css = {
            'all': ('%sjquery-treeview/jquery.treeview.css' % settings.STATIC_URL,)
        }
        js = (
            '%sjquery-treeview/jquery.cookie.pack.js' % settings.STATIC_URL,
            '%sjquery-treeview/jquery.treeview.js' % settings.STATIC_URL,
            '%sjquery-treeview/treeview_init.js' % settings.STATIC_URL,
        )