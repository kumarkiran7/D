from django.shortcuts import render

# Create your views here.
def cal(request):
    x=int(input("ENTER FRST NUMBER :"))
    y=int(input("ENTER SCND NUMBER :"))
    
    k=x+y
    l=x-y
    m=x*y
    n=x/y
    
    a={ 'num1':x,'num2':y,'res':k }
    b={ 'num1':x,'num2':y,'res':l }
    c={ 'num1':x,'num2':y,'res':m }
    d={ 'num1':x,'num2':y,'res':k }
    # a={ 'num1', ':',x,'num2'  ':', y, 'res',':',k }
    # b={ 'num1', ':', x,'num2' ':', y, 'res',':',l }
    # c={ 'num1', ':', x,'num2' ':', y, 'res',':',m }
    # d={ 'num1', ':', x,'num2' ':', y, 'res',':',k }
    
    return render(request,'display.html',a,b,c,d)
