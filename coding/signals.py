'''
***************************************************************************************
*    Title: django-quiz-app
*    Author: swapnil shindemeshram 
*    Date: 2019
*    Code version: master/2d70588
*    Availability: https://github.com/sswapnil2/django-quiz-app
*    Part of the code is referenced from the source code above
***************************************************************************************
'''
import django.dispatch

csv_uploaded = django.dispatch.Signal(providing_args=["user", "csv_file_list"])