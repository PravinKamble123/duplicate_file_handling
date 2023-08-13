from rest_framework.response import Response
from rest_framework import status
from .models import File

def check_file_name_exists_or_not(name):
    print("check file method is called !!!!")
    file_name, extension = name.split('.')
    file_names = File.objects.filter(file_name__icontains=f"{file_name}")
    if file_names and len(file_names) > 0:
        print("inside the if statement: ")
        print(f" Lenght of file names : {len(file_names)}")
        name = file_name+f"({len(file_names)})"
        print("Name after modifying is : ==>  "+name+"."+extension)
        return name+"."+extension
    return file_name+"."+extension
        