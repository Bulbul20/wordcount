from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request,'home.html')

def count(request):
    data= request.GET['textarea']
    word_list= data.split(" ")
    list_length = len(word_list)
    word_dictionary={}
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            word_dictionary[word] = 1
    # print(data)
    sorted_list = sorted(word_dictionary.items(),key=operator.itemgetter(1))
    return render(request,'count.html',{'data':data,'list_length':list_length,'word_dictionary':word_dictionary.items(),'sorted_list':sorted_list})

def about(request):
    return render(request,"about.html")