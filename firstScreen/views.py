from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import TemplateView, FormView, CreateView, View
from .forms import ModelForm#, PaintingForm, BallonForm#, SampleForm
from .myImagePoint_Edit import PaintingCreate

class CoverPage(TemplateView):
    template_name = 'firstScreen/coverpage.html'

class MannerPage(CreateView):
    template_name = 'firstScreen/manner.html'
    form_class = ModelForm
    success_url = reverse_lazy('coverpage')

    def form_valid(self, form):
        form.Create('2_manner.png')
        return super().form_valid(form)

class ReadingPage(CreateView):
    template_name = 'firstScreen/reading.html'
    form_class = ModelForm
    success_url = reverse_lazy('coverpage')

    def form_valid(self, form):
        form.Create('3_reading.png')
        return super().form_valid(form)

class ArcheryPage(CreateView):
    template_name = 'firstScreen/archery.html'
    form_class = ModelForm
    success_url = reverse_lazy('coverpage')

    def form_valid(self, form):
        # content = (
        #     form.fields["title"],
        #     form.fields["text"],
        #     form.fields["ballon_type"],
        #     form.fields["ballon_height"],
        #     form.fields["ballon_wight"],
        # )
        # PaintingCreate.merge(content)
        form.Create('4_archery.png')
        return super().form_valid(form)

class IaiPage(CreateView):
    template_name = 'firstScreen/iai.html'
    form_class = ModelForm
    success_url = reverse_lazy('coverpage')

    def form_valid(self, form):
        form.Create('5_iai.png')
        return super().form_valid(form)

class JujutsuPage(CreateView):
    template_name = 'firstScreen/jujutsu.html'
    form_class = ModelForm
    success_url = reverse_lazy('coverpage')

    def form_valid(self, form):
        form.Create('6_jujutsu.png')
        return super().form_valid(form)

class SojutsuPage(CreateView):
    template_name = 'firstScreen/sojutsu.html'
    form_class = ModelForm
    success_url = reverse_lazy('coverpage')

    def form_valid(self, form):
        form.Create('7_sojutsu.png')
        return super().form_valid(form)

class RidingPage(CreateView):
    template_name = 'firstScreen/riding.html'
    form_class = ModelForm
    success_url = reverse_lazy('coverpage')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)

    #     init_dict = {
    #         'title' :        '',
    #         'title'         :'',
    #         'text'          :'',
    #         'ballon_type'   :'', 
    #         'ballon_height' :'', 
    #         'ballon_wight'  :'', 
    #         'point_x'       :'', 
    #         'point_y'       :'',
    #         'painting_name' :'a'
    #     }
    #     form_class = ModelForm(initial=init_dict)
    #     context['form_class'] = form_class
    #     return context

    def form_valid(self, form):
        form.Create('8_riding')
        return super().form_valid(form)

class ArtilleryPage(CreateView):
    template_name = 'firstScreen/artillery.html'
    form_class = ModelForm
    success_url = reverse_lazy('coverpage')

    def form_valid(self, form):
        painting_data = form.save(commit=False)
        painting_data.save()
        form.Create('1_artillery.png')
        return super().form_valid(form)

class TestPage(View):
    template_name = 'firstScreen/test.html'
    form_class = ModelForm
    success_url = reverse_lazy('coverpage')
    fields = ()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'ballon_form': forms.BallonForm(**self.get_form_kwargs()),
            'painting_form': forms.PaintingForm(**self.get_form_kwargs()),
        })
        return context

    def form_valid(self, form):
        painting_data = form.save(commit=False)
        painting_data.save()
        form.Create('1_artillery.png')
        return super().form_valid(form)


def cover(request):
    return render(request, 'firstScreen/coverpage.html')
