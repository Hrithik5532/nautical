from turtle import update
from django.urls import path,  include
from .views import *
urlpatterns=[
    path('',home,name='home'),
    path('form_post',form_submit,name='form_post'),
    path('admin_form',adminView,name='admin_form'),
    path('pdf1/<int:pk>', pdf1_view,name='pdf1'), 
        path('pdf_2/<int:pk>',pdf2_view,name="pdf2"),
        path('pdf_3/<int:pk>',pdf3_view,name="pdf3"),
        path('pdf_4/<int:pk>',pdf4_view,name='pdf4'),
        path('edit/<int:pk>',updateDetails.as_view(),name='updatedetails'),
        path('delete/<int:pk>',deleteDetails,name='delete'),

        path('Amptc_form_2/<int:pk>',pdf1_apmtc2_view,name="amptc2")



]