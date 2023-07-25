from django.shortcuts import render
import datetime
import cx_Oracle
from django.db import connection
import json
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.
def dildata(request):
    cur = connection.cursor()
 
    sql2= """SELECT *  FROM tabelename """ #oracale database table name.
  
    cur.execute(sql2)
    row2= cur.fetchall()
   

    context={
     
       "obj2":row2
       
    }
    return render(request,'index.html', context)
  


