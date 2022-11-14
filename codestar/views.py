from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf.urls import url
from codestar import views
import sys
import numpy as np
from array import *
from codestar.models import User,Level
# Create your views here.
def greetings(request):
    res = render(request,'codestar/Home.html')
    return res
def form(request,id):
    res = render(request,'codestar/form.html',{"prize":id})
    return res
def createUser(request):
    name = request.POST['name']
    email = request.POST['email']
    phone_number = request.POST['phone']
    education = request.POST['education']
    level = "0"
    prize = request.POST['prize']
    newUser =  User(name=name,email=email,phone_number=phone_number,education=education,level=level,prize=prize )
    newUser.save()
    res = redirect('/level-one/')
    return res

def levelOne(request):
    levelOne = open('ex1.txt', 'r').read()
    code_part = open('Q1.txt', 'r').read() 
    res = render(request,'codestar/levelOne.html',{"levelOne":levelOne,"code":code_part})
    return res
def levelTwo(request):
    code_part = open('Q2.txt', 'r').read()
    res = render(request,'codestar/levelTwo.html',{"levelOne":levelOne,"code":code_part})
    return res
def levelThree(request):
    code_part = open('Q3.txt', 'r').read()
    res = render(request,'codestar/levelThree.html',{"code":code_part})
    return res


def levelOneRuncode(request):
    levelOne =open('ex1.txt', 'r').read()
    if request.method == 'POST':
        code_part = request.POST['code_area']
        try:
            orig_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(code_part)
            sys.stdout.close()
            sys.stdout=orig_stdout
            if open('file.txt', 'r').read() ==  open('ex1.txt', 'r').read():
                output = open('file.txt', 'r').read() 
                level =  Level(user_id= User.objects.last().id,level="1" )
                level.save()
                return  redirect('/level-two/')
            else:
                output="wrong answer \n"+open('file.txt', 'r').read()
                return       render(request,'codestar/levelOne.html',{"code":code_part,"output":output,"levelOne":levelOne})
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
        print(output)
    
    res = render(request,'codestar/levelOne.html',{"code":code_part,"output":output,"levelOne":levelOne})
    return res

def levelTwoRuncode(request):
    levelOne =open('ex2.txt', 'r').read()
    if request.method == 'POST':
        code_part = request.POST['code_area']
        input_part =[[7 ,69, 2, 221, 8974],[1, 2, 3, 4, 5],[10, 12, 31, 400, 58],[51, 0, 63, 41,70]]
        y = input_part
        # input_part = input_part.replace("\n"," ").split("")
        def input():
      
            return input_part
        try:
            orig_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(code_part)
            sys.stdout.close()
            sys.stdout=orig_stdout
            if open('file.txt', 'r').read() ==  open('ex2.txt', 'r').read():
                output = open('file.txt', 'r').read() 
                level =  Level(user_id= User.objects.last().id,level="2" )
                level.save()
                return   redirect('/level-three/')
            else:
                output="wrong answer \n"+open('file.txt', 'r').read()
               
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
        print(output)
    
    res =   render(request,'codestar/levelTwo.html',{"code":code_part,"output":output,"levelOne":levelOne})
    return res


def levelThreeRuncode(request):
    levelOne =open('ex1.txt', 'r').read()
    if request.method == 'POST':
        code_part = request.POST['code_area']
        input_part =[[100,100,70,50],[10,60,80,101]]

        y = input_part 
        # input_part = input_part.replace("\n"," ").split("")
        def input():
      
            return input_part 
            
        try:
            orig_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(code_part)
            sys.stdout.close()
            sys.stdout=orig_stdout
            if open('file.txt', 'r').read() ==  open('ex3.txt', 'r').read():
                output = open('file.txt', 'r').read() 
                level =  Level(user_id= User.objects.last().id,level="3" )
                level.save()
                return  redirect('/')
            else:
                output="wrong answer \n"+open('file.txt', 'r').read()
                return  render(request,'codestar/levelThree.html',{"code":code_part,"output":output})
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = e
        print(output)
    
    return  render(request,'codestar/levelThree.html',{"code":code_part,"output":output})
 

