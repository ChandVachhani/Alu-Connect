from django.shortcuts import render,redirect
from .algorithms import lcs,sort
from django.contrib.auth.models import User
# Create your views here.

def search_for_person(request):
    if request.GET:
        para_dict = request.GET
        value = para_dict['people']
        total_person = User.objects.all().order_by('username')
        search_count=0
        search_list = []
        max_match = 0
        for person in total_person:
            full_name = person.first_name+person.last_name
            lcs_val = lcs(str(full_name),value)
            max_match = max(max_match,lcs_val)
        if max_match>len(value)/2:
            for person in total_person:
                full_name = person.first_name + person.last_name
                person_tuple = (person,lcs(str(full_name),value))
                if(person_tuple[1]>int(max_match/2)):
                    search_list.append(person_tuple)
                    search_count+=1
        sort(search_list)
        final_search_list=[]
        for i in search_list:
            final_search_list.append(i[0])
        context_dict = {'result':final_search_list,'total_result':search_count,'search_result':value}
        return render(request, 'user/people.html',context_dict)
    else:
        return redirect('main-page')