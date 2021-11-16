from django.contrib.auth.decorators import login_required
from django.forms.widgets import DateInput
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic.list import ListView
from django.utils.text import slugify 
from First.models import Flight,Comment
from django.views.generic import DetailView
from django.contrib import messages
from Flightio.settings import TIME_ZONE
from .models import Flight
from .forms import AddCommentFlight, AddSchaduleForm,AddReplyForm
from jalali_date import datetime2jalali, date2jalali


class schaduleHome(ListView):
    template_name = 'First/schadule.html'
    model = Flight #return all of class
    queryset = Flight.objects.filter() #object_list
    context_object_name = 'Flight' 
    ordering = ['-created']

def DetailFlight(request,flight_id):
    flight = get_object_or_404(Flight,pk=flight_id)
    reply_form = AddReplyForm()
    comment = Comment.objects.filter(Flight=flight, is_reply=False)
    if request.method == 'POST':
        form = AddCommentFlight(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.Flight = flight 
            new_comment.user = request.user
            new_comment.save()
            messages.success(request,'پیگیری شما ثبت شد')
    else:
        form = AddCommentFlight()
    return render(request,'First/detail_schadule.html',{'flight':flight,'comments':comment,'form':form,'reply':reply_form})


def add_Schadule(request):    
   
        if request.method == 'POST':
            form = AddSchaduleForm(request.POST)
            if form.is_valid():
                new_schadule = form.save(commit=False)
                new_schadule.slug = slugify(f"{form.cleaned_data['Flight_Origin']}-{form.cleaned_data['Flight_Distination']}-{form.cleaned_data['Flight_Airline']}-{form.cleaned_data['Flight_Nomber']}-{form.cleaned_data['Flight_Date']}")            
                
                new_schadule.save()
                messages.success(request, 'submited')
                return redirect('first:index')
            else:
                messages.warning(request, 'ridi')

        else:
            form = AddSchaduleForm()
        return render(request,'First/add_Schadule.html', {'form':form} )
    
@login_required
def add_reply(request,flight_id,comment_id):
    flight= get_object_or_404(Flight,id=flight_id)
    comment = get_object_or_404(Comment,id=comment_id)
    if request.method == 'POST':
        form = AddReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.user = request.user
            reply.Flight = flight
            reply.reply = comment
            reply.is_reply = True
            reply.save()
            messages.success(request, 'your reply submitted successfully', 'success')
    return redirect('first:flight_detail', flight_id)
