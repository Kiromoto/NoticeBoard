from django.contrib.auth.models import User
from django_filters import FilterSet, CharFilter, ModelChoiceFilter, DateFilter, ChoiceFilter
from .models import Ad
from django.forms import DateInput


class AdFilter(FilterSet):
    title = CharFilter(lookup_expr='icontains',
                       label='Поиск в заголовке',
                       )
    text = CharFilter(lookup_expr='icontains',
                      label='Поиск в тексте',
                      )

    category = ChoiceFilter(choices=Ad.TYPE,
                            label='Категория',
                            empty_label='Все категории',
                            )

    author = ModelChoiceFilter(queryset=User.objects.all(),
                               label='Автор',
                               empty_label='Все авторы',
                               )

    dt_create = DateFilter(field_name='dt_create',
                           lookup_expr='gt', label='Опубликовано после',
                           widget=DateInput(attrs={'type': 'date'}),
                           )

    dt_create.field.error_messages = {'invalid': 'Введите дату в формате DD.MM.YYYY. Например: 23.10.2022'}
    dt_create.field.widget.attrs = {'placeholder': 'DD.MM.YYYY'}

    class Meta:
        fields = {'title': ['icontains'],
                  'text': ['icontains'],
                  'category': ['exact'],
                  'author': ['exact'],
                  'dt_create': ['gt'],
                  }


class MyAdFilter(FilterSet):
    title = CharFilter(lookup_expr='icontains',
                       label='Поиск в заголовке',
                       )
    text = CharFilter(lookup_expr='icontains',
                      label='Поиск в тексте',
                      )

    category = ChoiceFilter(choices=Ad.TYPE,
                            label='Категория',
                            empty_label='Все категории',
                            )

    dt_create = DateFilter(field_name='dt_create',
                           lookup_expr='gt', label='Опубликовано после',
                           widget=DateInput(attrs={'type': 'date'}),
                           )

    dt_create.field.error_messages = {'invalid': 'Введите дату в формате DD.MM.YYYY. Например: 23.10.2022'}
    dt_create.field.widget.attrs = {'placeholder': 'DD.MM.YYYY'}

    class Meta:
        fields = {'title': ['icontains'],
                  'text': ['icontains'],
                  'category': ['exact'],
                  'dt_create': ['gt'],
                  }


class ResponseFilter(FilterSet):
    user = ModelChoiceFilter(queryset=User.objects.all(),
                             label='От пользователя',
                             empty_label='от всех',
                             )
    ad = ModelChoiceFilter(queryset=Ad.objects.all(),
                           label='По вашим объявлениям',
                           empty_label='по всем',
                           )
    text = CharFilter(lookup_expr='icontains',
                      label='Поиск в тексте',
                      )
    dt_create = DateFilter(field_name='dt_create',
                           lookup_expr='gt', label='Опубликовано после',
                           widget=DateInput(attrs={'type': 'date'}),
                           )

    dt_create.field.error_messages = {'invalid': 'Введите дату в формате DD.MM.YYYY. Например: 23.10.2022'}
    dt_create.field.widget.attrs = {'placeholder': 'DD.MM.YYYY'}

    class Meta:
        fields = []
        fields = {'user': ['exact'],
                  'ad': ['exact'],
                  'text': ['icontains'],
                  'dt_create': ['gt'],
                  }
