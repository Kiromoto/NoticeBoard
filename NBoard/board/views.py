from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Ad, Response
from .forms import AdForm, ResponseForm
from .filters import AdFilter, ResponseFilter, MyAdFilter

LOGINURL = 'http://127.0.0.1:8000/accounts/login/'


class AdEdit(PermissionRequiredMixin, UpdateView):
    permission_required = ('board.change_ad')
    form_class = AdForm
    model = Ad
    template_name = 'ad_edit.html'
    context_object_name = 'adnew'


class AdDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('board.delete_ad')
    model = Ad
    template_name = 'ad_delete.html'
    success_url = reverse_lazy('ads_list')


class AdList(ListView):
    model = Ad
    ordering = '-dt_create'
    template_name = 'ads.html'
    context_object_name = 'ads'
    paginate_by = 5

    def get_filter(self):
        return AdFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            'filterset': self.get_filter(),
        }


class MyAdList(PermissionRequiredMixin, ListView):
    permission_required = ('board.view_ad',
                           'board.delete_ad',
                           'board.change_ad',
                           'board.view_response',
                           'board.delete_response',
                           'board.change_response',
                           )
    model = Ad
    ordering = '-dt_create'
    template_name = 'myads.html'
    context_object_name = 'myads'
    paginate_by = 5

    def get_filter(self):
        queryset = super().get_queryset()
        return MyAdFilter(self.request.GET, queryset=queryset.filter(author=self.request.user))

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            'filterset': self.get_filter(),
        }


class AdDetail(DetailView):
    model = Ad
    template_name = 'ad.html'
    context_object_name = 'ad'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        file = get_object_or_404(Ad, pk=self.kwargs.get('pk'))
        if Response.objects.filter(ad=file).exists():
            context['adresponses'] = Response.objects.filter(ad=file)

        if file.uploads:
            context['file_name'] = file.uploads.name
            context['file_url'] = file.uploads.url
            context['file_path'] = file.uploads.path

        else:
            context['file_name'] = 'Нет файлов'
            context['file_url'] = ''
        return context


class ResponseDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('board.delete_response')
    model = Response
    template_name = 'response_delete.html'
    success_url = reverse_lazy('my_responses')


class MyResponsesList(PermissionRequiredMixin, ListView):
    permission_required = ('board.view_response',
                           'board.delete_response',
                           'board.change_response',
                           )
    model = Response
    ordering = '-dt_create'
    template_name = 'myresponses.html'
    context_object_name = 'myresp'
    paginate_by = 5

    def get_filter(self):
        queryset = super().get_queryset()
        return ResponseFilter(self.request.GET, queryset=queryset.filter(ad__author=self.request.user))

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            'filterset': self.get_filter(),
        }


@login_required(login_url=LOGINURL)
def ad_create(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = AdForm()
            return render(request, 'ad_edit.html', {'form': form})

        if request.method == 'POST':
            form = AdForm(request.POST)
            ad = form.save(commit=False)
            ad.author = request.user

        ad.save()

        return redirect(ad.get_absolute_url())

    else:
        return HttpResponseRedirect(LOGINURL)


@login_required(login_url=LOGINURL)
def response_create(request, pk):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = ResponseForm()

            return render(request,
                          'response_edit.html',
                          {
                              'form': form,
                              'ad': get_object_or_404(Ad, id=pk),
                          }
                          )

        if request.method == 'POST':
            form = ResponseForm(request.POST)
            response = form.save(commit=False)
            response.user = request.user
            ad_response = get_object_or_404(Ad, id=pk)
            response.ad = ad_response

        response.save()
        return redirect(ad_response.get_absolute_url())

    else:
        return HttpResponseRedirect(LOGINURL)


@login_required(login_url=LOGINURL)
def accept_response(request, pk):
    response = Response.objects.get(pk=pk)
    response.accept = True
    response.save()
    return redirect('my_responses')


@login_required(login_url=LOGINURL)
def reject_response(request, pk):
    response = Response.objects.get(pk=pk)
    response.reject = True
    response.save()
    return redirect('my_responses')
