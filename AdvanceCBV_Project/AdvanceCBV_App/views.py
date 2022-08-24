from django.shortcuts import render
from django.urls   import reverse_lazy
from django.views.generic import (View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from . import models
# Create your views here.

class CBView(TemplateView):
    template_name = 'AdvanceCBV_App/Base.html'



class SchoolListView(ListView):
    # taking everything from the model named school

    # note that the name of School will be returned in lower case and underscore and the name list wll be added on School name. e.g school_list this is what you going to see on the frontend
    model = models.School

    # to call the School name the way you want on the frontend put the following line of code
    context_object_name = 'schools'
    # the above line of code changes the the name of School from being school_list into schools "DON'T FORGET THIS"
    # we doing this for the frontend dude to understand what's going on here because they would be suprised when the see the School name changed into be school_list.
    # for me i'll keep the very first line because it is pretty clear to me, then on frontend i MUSTN'T FORGET TO NAME MY MODEL AS MODELNAME_LIST e.g school_list



class SchoolDetaiView(DetailView):
    # Giving my model a name that frontend dev will be able to understand
    # you you don't want you can ignor the following line, but know that your model name is going to be in lower case
    context_object_name = 'school_detail'
    # unlike ListView this the onlything it those is to lower your modeln name. e.g School= school
    model = models.School
    # creating a variable and  linking it with templates
    template_name = 'AdvanceCBV_App/School_details.html'


# Creating a class view, this allows the user to easily put new info into the database without using admin interface
class SchoolCreateView(CreateView):
    # parsing the same attributes that the model School have as a variable
    fields= ('name','principal','Location')
    model = models.School

# the following class will help the user to update the information inside the database
class SchoolUpdateView(UpdateView):
    # specifying the fields that the user will be able to update, in this case  i am going to give the user the permission of only updating the name and principal of the school
    fields = ('name','principal')
    model = models.School
    # the following view will allow the user to delete the specific data inside the database
class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("AdvanceCBV_App:list")
