
import re
from django.shortcuts import render,redirect,  get_object_or_404
from django.http import Http404
from .models import *
from django.contrib import messages
from .forms import *
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect



def  home(request):
    forms={
        'ATOCform':ATOCForm,
        'personaldetailsform':profileDetailsForm,
        'Nkd_deForm':Nkd_deForm,
        'PassportDetailsForm':PassportDetailsForm,
        'CDCSBForm':CDCSBForm,
        'AcademicDetailsForm':AcademicDetailsForm,
        'LCOCForm':LCOCForm,
        'STCWCertificatesForm': STCWCertificatesForm,
        'AboutUSForm':AboutUSForm,
        'LDWForm':LDWForm,
        'PersonalDetailsForm':PersonalDetailsForm,
        'Additional_infoForm':Additional_infoForm,
        'Reason_for_appForm':Reason_for_appForm,
        'DeclarationForm':DeclarationForm
    }
    return render(request,'nautical_form.html',{'forms':forms})



def save_nkd(request,user):
        nkd_name_no=request.POST.getlist(f'name0')
        nkd_rela_no=request.POST.getlist(f'relation0')
        nkd_dob_no=request.POST.getlist(f'dob0')

        nkd_ppno_no=request.POST.getlist(f'ppno0')
        for i,j,q,z in zip(nkd_name_no,nkd_rela_no,nkd_dob_no,nkd_ppno_no):
            if i !='':
                print(i,j,q,z)
                NKD(name=user,nkd_name_no=i,nkd_rela_no=j,nkd_dob_no=q,nkd_ppno_no=z).save()


def nkd_de(request,user):
    form= Nkd_deForm(request.POST)
    if form.is_valid():
            form2=form.save(commit=False)
            form2.name = get_object_or_404(profileDetails,id=user.id)
            return form2
    else:
        return form
def atoc(request,user):
    form= ATOCForm(request.POST)
    if form.is_valid():
            form2=form.save(commit=False)
            form2.name = get_object_or_404(profileDetails,id=user.id)
            return form2
    else:
        return form
def pass_details(request,user):
    form= PassportDetailsForm(request.POST)


    if form.is_valid():
            form2=form.save(commit=False)
            form2.name = get_object_or_404(profileDetails,id=user.id)
            return form2
    else:
        return form

def cdcsb(request,user):
    form= CDCSBForm(request.POST)
    if form.is_valid():
            form2=form.save(commit=False)
            form2.name = get_object_or_404(profileDetails,id=user.id)
            return form2
    else:
        return form

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def academicdetails(request,user):
    form= AcademicDetailsForm(request.POST)

    if form.is_valid():
            form2=form.save(commit=False)
            form2.name = get_object_or_404(profileDetails,id=user.id)
            return form2
    else:
        return form

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def lcoc(request,user):
    form= LCOCForm(request.POST)
    if form.is_valid():
            form2=form.save(commit=False)
            form2.name = get_object_or_404(profileDetails,id=user.id)
            return form2
    else:
        return form
def stcw(request,user):
    form= STCWCertificatesForm(request.POST)
    if form.is_valid():
            form2=form.save(commit=False)
            form2.name = get_object_or_404(profileDetails,id=user.id)
            return form2
    else:
        return form
def stcw(request,user):
    form= STCWCertificatesForm(request.POST)
    if form.is_valid():
            form2=form.save(commit=False)
            form2.name = get_object_or_404(profileDetails,id=user.id)
            return form2
    else:
        return form


def ref(request,user):
    name1=request.POST.getlist(f'name_ref')
    company=request.POST.getlist(f'company0')
    contact=request.POST.getlist(f'phone0')
    print(name1,company,contact)
    for i,j,q in zip(name1,company,contact):
            if i !='':
                Reference(name=user,name1=i,company=j,contact=q).save()

def aboutus(request,user):
    form= AboutUSForm(request.POST)
    if form.is_valid():
            form2=form.save(commit=False)
            form2.name = get_object_or_404(profileDetails,id=user.id)
            return form2
    else:
        return form

def personaldetails(request,user):
    form= PersonalDetailsForm(request.POST)
    if form.is_valid():
            form2=form.save(commit=False)
            form2.name = get_object_or_404(profileDetails,id=user.id)
            return form2
    else:
        return form

def ldw(request,user):
    form= LDWForm(request.POST)
    if form.is_valid():
            form2=form.save(commit=False)
            form2.name = get_object_or_404(profileDetails,id=user.id)
            return form2
    else:
        return form

def addition_details(request,user):
    form= Additional_infoForm(request.POST)
    if form.is_valid():
            form2=form.save(commit=False)
            form2.name = get_object_or_404(profileDetails,id=user.id)
            return form2
    else:
        return form

def reson_for_app(request,user):
    form= Reason_for_appForm(request.POST)
    if form.is_valid():
            form2=form.save(commit=False)
            form2.name = get_object_or_404(profileDetails,id=user.id)
            return form2
    else:
        return form



def sea_exp(request,user):
    employer=request.POST.getlist('empl')
    rpsl=request.POST.getlist('rspl0')
    vessel_name=request.POST.getlist('vessel0')
    steam_motor=request.POST.getlist('stream_motor0')
    dwt_grt=request.POST.getlist('dwt0')
    rank=request.POST.getlist('rank0')
    engine=request.POST.getlist('engine0')

    bhp=request.POST.getlist('bhp0')
    engin_room=request.POST.getlist('engine_room')
    date_from=request.POST.getlist('fromdt0')
    date_to=request.POST.getlist('todt0')
    total=request.POST.getlist('total0')





    for i,j,q,k,x,y,z,a,b,c,d,e in zip(employer,rpsl,vessel_name,steam_motor,dwt_grt,rank,engine,bhp,engin_room,date_from,date_to,total):
             if i !='':
                SEA_Exp(name=user,employer=i,rpsl=j,vessel_name=q,steam_motor=k,dwt_grt=x,rank=y,engine=z,bhp=a,engin_room=b,date_from=c,date_to=d,total=e).save()

def oss(request,user):
    employer=request.POST.getlist('empl0')
    title=request.POST.getlist('title0')
    workshop=request.POST.getlist('works0')
    major_machine=request.POST.getlist('machine0')
    supervised=request.POST.getlist('pers0')
    size=request.POST.getlist('size0')
    period_frm=request.POST.getlist('from0')
    period_to=request.POST.getlist('to0')
    other_info=request.POST.getlist('any0')


    for i,j,q,k,x,y,z,a,b in zip(employer,title,workshop,major_machine,supervised,size,period_frm,period_to,other_info):
            print(i,j,q,k,x,y,z,a,b)
            if i !='':
                OSS(name=user,employer=i,title=j,workshop=q,major_machine=k,supervised=x,size=y,period_frm=z,period_to=a,other_info=b).save()

def declar(request,user):
    form= DeclarationForm(request.POST, request.FILES)
    if form.is_valid():
            form2=form.save(commit=False)
            form2.name = get_object_or_404(profileDetails,id=user.id)
            return form2
    else:
        return form

def form_submit(request):
    if request.method =='POST':
        form =profileDetailsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                user = profileDetails.objects.latest('created')
                atocF=atoc(request,user)
                nkd_des = nkd_de(request,user)
                pass_detail =pass_details(request,user)
                cdcsbform =cdcsb(request,user)
                academicdetailsform=academicdetails(request,user)
                lcocform=lcoc(request,user)
                stcwform=stcw(request,user)
                aboutusform=aboutus(request,user)
                personaldetailsform=personaldetails(request,user)
                ldwform=ldw(request,user)
                addition_detailsform=addition_details(request,user)

                reson_for_appform=reson_for_app(request,user)

                declarform=declar(request,user)


                # saving forms
                nkd_des.save()
                atocF.save()
                pass_detail.save()

                cdcsbform.save()

                academicdetailsform.save()

                lcocform.save()

                stcwform.save()

                aboutusform.save()

                personaldetailsform.save()

                ldwform.save()

                addition_detailsform.save()
                reson_for_appform.save()

                declarform.save()

                save_nkd(request,user)


                ref(request,user)

                sea_exp(request,user)

                oss(request,user)


                messages.success(request,"Form Submitted Successfully")


            except Exception as e:
                 messages.error(request,e)
        else:
            messages.error(request,form.errors)


    return redirect('home')




def pdf1_view(request,pk):
    profileDetail=profileDetails.objects.get(id=pk)
    nkd_list = NKD.objects.filter(name=profileDetail.id)
    passportDetails = PassportDetails.objects.get(name=profileDetail.id)
    
    name= profileDetail.fname
    surname=profileDetail.lname
    father = profileDetail.mname
    context={
            'atoc':ATOC.objects.get(name=profileDetail.id),
'name':name ,
          'father':father,
          'surname':surname,
          'profileDetails':profileDetail,
          'nkd_list':nkd_list,
          'nkd_de':NKD_de.objects.get(name=profileDetail.id),
          'passportDetails':passportDetails,
          'CDCSB':CDCSB.objects.get(name=profileDetail.id),
         'AcademicDetails':AcademicDetails.objects.get(name=profileDetail.id),
         'LCOC':LCOC.objects.get(name=profileDetail.id),
        'STCWCertificates': STCWCertificates.objects.get(name=profileDetail.id),
         'reference':Reference.objects.filter(name=profileDetail.id),
            'LDW':LDW.objects.get(name=profileDetail.id),
         'AboutUS':AboutUS.objects.get(name=profileDetail.id),
        'LDW':LDW.objects.get(name=profileDetail.id),
         'PersonalDetails':PersonalDetails.objects.get(name=profileDetail.id),
         'Additional_info':Additional_info.objects.get(name=profileDetail.id),
            'Reason_for_app':Reason_for_app.objects.get(name=profileDetail.id),
         'SEA_Exp':SEA_Exp.objects.filter(name=profileDetail.id),
         'OSS':OSS.objects.filter(name=profileDetail.id),
         'Declaration':Declaration.objects.get(name=profileDetail.id)



    }
    return render(request,'amptc.html',context)


def pdf1_apmtc2_view(request,pk):
    profileDetail=profileDetails.objects.get(id=pk)
    print(profileDetail)
    #nkd_de = NKD_de.objects.get(name=profileDetail.id)
    nkd_list = NKD.objects.filter(name=profileDetail.id)
    passportDetails = PassportDetails.objects.get(name=profileDetail.id)

    name= profileDetail.fname
    surname=profileDetail.lname
    father = profileDetail.mname
    context={
            'atoc':ATOC.objects.get(name=profileDetail.id),
'name':name ,
          'father':father,
          'surname':surname,
          'profileDetails':profileDetail,
          'nkd_list':nkd_list,
          'nkd_de':NKD_de.objects.get(name=profileDetail.id),
          'passportDetails':passportDetails,
          'CDCSB':CDCSB.objects.get(name=profileDetail.id),
         'AcademicDetails':AcademicDetails.objects.get(name=profileDetail.id),
         'LCOC':LCOC.objects.get(name=profileDetail.id),
        'STCWCertificates': STCWCertificates.objects.get(name=profileDetail.id),
         'reference':Reference.objects.filter(name=profileDetail.id),
            'LDW':LDW.objects.get(name=profileDetail.id),
         'AboutUS':AboutUS.objects.get(name=profileDetail.id),
        'LDW':LDW.objects.get(name=profileDetail.id),
         'PersonalDetails':PersonalDetails.objects.get(name=profileDetail.id),
         'Additional_info':Additional_info.objects.get(name=profileDetail.id),
            'Reason_for_app':Reason_for_app.objects.get(name=profileDetail.id),
         'SEA_Exp':SEA_Exp.objects.filter(name=profileDetail.id),
         'OSS':OSS.objects.filter(name=profileDetail.id),
         'Declaration':Declaration.objects.get(name=profileDetail.id)



    }
    return render(request,'amptc2.html',context)



def pdf2_view(request,pk):
    profileDetail=profileDetails.objects.get(id=pk)
    #nkd_de = NKD_de.objects.get(name=profileDetail.id)
    nkd_list = NKD.objects.filter(name=profileDetail.id)
    passportDetails = PassportDetails.objects.get(name=profileDetail.id)
 
    name= profileDetail.fname
    surname=profileDetail.lname
    father = profileDetail.mname
    nkd =NKD_de.objects.get(name=profileDetail.id)
    print(nkd.name_rela)
    context={
            'atoc':ATOC.objects.get(name=profileDetail.id),
'name':name ,
          'father':father,
          'surname':surname,
          'profileDetails':profileDetail,
          'nkd_list':nkd_list,
          'nkd_de':NKD_de.objects.get(name=profileDetail.id),
          'passportDetails':passportDetails,
          'CDCSB':CDCSB.objects.get(name=profileDetail.id),
         'AcademicDetails':AcademicDetails.objects.get(name=profileDetail.id),
         'LCOC':LCOC.objects.get(name=profileDetail.id),
        'STCWCertificates': STCWCertificates.objects.get(name=profileDetail.id),
         'reference':Reference.objects.filter(name=profileDetail.id),
            'LDW':LDW.objects.get(name=profileDetail.id),
         'AboutUS':AboutUS.objects.get(name=profileDetail.id),
        'LDW':LDW.objects.get(name=profileDetail.id),
         'PersonalDetails':PersonalDetails.objects.get(name=profileDetail.id),
         'Additional_info':Additional_info.objects.get(name=profileDetail.id),
            'Reason_for_app':Reason_for_app.objects.get(name=profileDetail.id),
         'SEA_Exp':SEA_Exp.objects.filter(name=profileDetail.id),
         'OSS':OSS.objects.filter(name=profileDetail.id),
         'Declaration':Declaration.objects.get(name=profileDetail.id)



    }
    return render(request,'kotc_new.html',context)
def pdf3_view(request,pk):
    profileDetail=profileDetails.objects.get(id=pk)

    name= profileDetail.fname
    surname=profileDetail.lname
    father = profileDetail.mname
    nkd_list = NKD.objects.filter(name=profileDetail.id)
    passportDetails = PassportDetails.objects.get(name=profileDetail.id)
    context={
                'atoc':ATOC.objects.get(name=profileDetail.id),
    'nkd_de' :NKD_de.objects.get(name=profileDetail.id),

          'profileDetails':profileDetail,
          'name':name ,
          'father':father,
          'surname':surname,
          'nkd_list':nkd_list,
          'passportDetailsForm':passportDetails,
          'CDCSB':CDCSB.objects.get(name=profileDetail.id),
         'AcademicDetails':AcademicDetails.objects.get(name=profileDetail.id),
         'LCOC':LCOC.objects.get(name=profileDetail.id),
        'STCWCertificates': STCWCertificates.objects.get(name=profileDetail.id),
         'reference':Reference.objects.filter(name=profileDetail.id),
            'LDW':LDW.objects.get(name=profileDetail.id),
         'AboutUS':AboutUS.objects.get(name=profileDetail.id),
        'LDW':LDW.objects.get(name=profileDetail.id),
         'PersonalDetails':PersonalDetails.objects.get(name=profileDetail.id),
         'Additional_info':Additional_info.objects.get(name=profileDetail.id),
            'Reason_for_app':Reason_for_app.objects.get(name=profileDetail.id),
         'SEA_Exp':SEA_Exp.objects.filter(name=profileDetail.id),
         'OSS':OSS.objects.filter(name=profileDetail.id),
         'Declaration':Declaration.objects.get(name=profileDetail.id)



    }
    return render(request,'warmseas.html',context)

def pdf4_view(request,pk):
    profileDetail=profileDetails.objects.get(id=pk)
    name= profileDetail.fname
    surname=profileDetail.mname
    father = profileDetail.lname
    nkd_list = NKD.objects.filter(name=profileDetail.id)
    passportDetails = PassportDetails.objects.get(name=profileDetail.id)
    context={
                'atoc':ATOC.objects.get(name=profileDetail.id),
    'nkd_de' :NKD_de.objects.get(name=profileDetail.id),

          'profileDetails':profileDetail,
          'name':name ,
          'father':father,
          'surname':surname,
          'nkd_list':nkd_list,
          'passportDetailsForm':passportDetails,
          'CDCSB':CDCSB.objects.get(name=profileDetail.id),
         'AcademicDetails':AcademicDetails.objects.get(name=profileDetail.id),
         'LCOC':LCOC.objects.get(name=profileDetail.id),
        'STCWCertificates': STCWCertificates.objects.get(name=profileDetail.id),
         'reference':Reference.objects.filter(name=profileDetail.id),
            'LDW':LDW.objects.get(name=profileDetail.id),
         'AboutUS':AboutUS.objects.get(name=profileDetail.id),
        'LDW':LDW.objects.get(name=profileDetail.id),
         'PersonalDetails':PersonalDetails.objects.get(name=profileDetail.id),
         'Additional_info':Additional_info.objects.get(name=profileDetail.id),
            'Reason_for_app':Reason_for_app.objects.get(name=profileDetail.id),
         'SEA_Exp':SEA_Exp.objects.filter(name=profileDetail.id),
         'OSS':OSS.objects.filter(name=profileDetail.id),
         'Declaration':Declaration.objects.get(name=profileDetail.id)



    }
    return render(request,'new.html',context)


class updateDetails(View):
    template_name = 'edit.html'

    def get_object(self):
        try:
            obj = profileDetails.objects.get(pk=self.kwargs['pk'])
        except profileDetails.DoesNotExist:
            raise Http404('Question not found!')
        return obj

    def get_context_data(self, **kwargs):
        kwargs['question'] = self.get_object()
        if 'profileDetailsForm' not in kwargs:
            kwargs['profileDetailsForm'] = profileDetailsForm()
        if 'ATOCForm' not in kwargs:
            kwargs['ATOCForm'] = ATOCForm()

        return kwargs

    def get(self, request, *args, **kwargs):
            return render(request, self.template_name, self.get_context_data())



def  adminView(request):
    infos = profileDetails.objects.all()

    return render(request,'admin.html',{'infos':infos})



def deleteDetails(request,pk):
    detail = profileDetails.objects.filter(id =pk)
    detail.delete()
    return HttpResponseRedirect(reverse("admin_form"))
    
   