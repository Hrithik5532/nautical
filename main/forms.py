
from sys import argv
from django import forms
from pkg_resources import require
from .models import *
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django.conf import settings
import datetime

# 1
class profileDetailsForm(forms.ModelForm):
    ms={
        ('----','----')
,    ('Married','Married'),
    ('UnMarried ', 'UnMarried'),
    ('Separated','Separated'),('Divorced','Divorced'),('Widow(er)','Widow(er)')

    }

    smoker={
                ('----','----'),

    ('Smoker','Smoker'),
    ('Non-Smoker', 'Non-Smoker')
    }
    dob= forms.DateField(widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control','placeHolder':"Enter Email"}))
    email2 = forms.EmailField(required=False,widget=forms.TextInput(attrs={'class': 'form-control','placeHolder':"Enter Email"}))
    nationality=CountryField().formfield(widget=CountrySelectWidget(attrs={"class": "form-control"}))
    marritial_status =forms.ChoiceField(  initial='----',choices=ms ,widget=forms.Select(attrs={'class': 'form-control'}))
    smoker =forms.ChoiceField( required=False, initial='----',choices=smoker ,widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = profileDetails
        fields= '__all__'
        widgets={
                'fname':forms.TextInput(attrs={'class':'form-control','placeHolder':"First Name"}),
                'mname':forms.TextInput(attrs={'class':'form-control','placeHolder':"Middle Name"}),
                'lname':forms.TextInput(attrs={'class':'form-control','placeHolder':"Last Name"}),

                'pob':forms.TextInput(attrs={'class':'form-control','placeHolder':"Enter Place Of Birth"}),
                'add1':forms.TextInput(attrs={'class':'form-control','placeHolder':"Enter Address"}),
                'city':forms.TextInput(attrs={'class':'form-control','placeHolder':"Enter City "}),
                'pno':forms.TextInput(attrs={'class':'form-control','placeHolder':"Enter Number"}),
                'airport':forms.TextInput(attrs={'class':'form-control','placeHolder':"Enter Nearest Airport"}),
                'add2' : forms.TextInput(attrs={'class':'form-control','placeHolder':"Enter Address"}),
                'city2': forms.TextInput(attrs={'class':'form-control','placeHolder':"Enter City"}),
                'pno2' : forms.TextInput(attrs={'class':'form-control','placeHolder':"Enter Number"}),

                'insta': forms.TextInput(attrs={'class':'form-control','placeHolder':"Instagram Id/Username/Link"}),
                'facebook' : forms.TextInput(attrs={'class':'form-control','placeHolder':"FaceBook Id/Username/Link"}),
                'twitter': forms.TextInput(attrs={'class':'form-control','placeHolder':"Twitter Id/Username/Link"}),
                'linkedin' : forms.TextInput(attrs={'class':'form-control','placeHolder':"LinkedIn Id/Username/Link"}),

                'airport2': forms.TextInput(attrs={'class':'form-control','placeHolder':"Enter Internation Airport"}),
                'zip':forms.TextInput(attrs={'class':'form-control','placeHolder':"Enter Pin Code"}),
                'zip2':forms.TextInput(attrs={'class':'form-control','placeHolder':"Enter Pin Code"}),

        }
#2
class Nkd_deForm(forms.ModelForm):
    class Meta:
        model =NKD_de
        exclude=['name']
        widgets={
            'name_rela':forms.TextInput(attrs={'class':'form-control','placeHolder':"Enter Name "}),
            'relation':forms.TextInput(attrs={'class':'form-control','placeHolder':"Relation"}),
            'add_nkd':forms.TextInput(attrs={'class':'form-control','placeHolder':"Enter Name"}),
        }
class ATOCForm(forms.ModelForm):
    doa = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    doa2 = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))

    class Meta:
        model =ATOC
        exclude=['name']
        widgets={
            'rank':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'ms_rank':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
        }

class PassportDetailsForm(forms.ModelForm):
    pass_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    pass_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    visa_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    visa_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    yellow_fever_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    yellow_fever_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))

    class Meta:
        model = PassportDetails
        exclude = ['name']
        widgets = {
                    'pass_no': forms.TextInput(attrs={'class':'form-control','placeHolder':"Passport no."}),
                    'pass_poi': forms.TextInput(attrs={'class':'form-control','placeHolder':"place of issue"}),

                    'visa_no' : forms.TextInput(attrs={'class':'form-control','placeHolder':"VISA no."}),
                    'visa_poi' : forms.TextInput(attrs={'class':'form-control','placeHolder':"place of issue"}),

                    'yellow_fever_no': forms.TextInput(attrs={'class':'form-control','placeHolder':"yellow fever no."}),
                    'yellow_fever_poi': forms.TextInput(attrs={'class':'form-control','placeHolder':"place of issue"}),

        }


#4
class CDCSBForm(forms.ModelForm):
    ind_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    ind_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    panama_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    panama_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    others_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    others_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))

    class Meta:
        model = CDCSB
        exclude = ['name']
        widgets = {
                    'ind_no':forms.TextInput(attrs={'class':'form-control','placeHolder':"Certificate no."}),
                    'ind_poi':forms.TextInput(attrs={'class':'form-control','placeHolder':"place of issue"}),
                    'panama_no':forms.TextInput(attrs={'class':'form-control','placeHolder':"Certificate no."}),
                    'panama_poi':forms.TextInput(attrs={'class':'form-control','placeHolder':"place of issue"}),
                    'others_no': forms.TextInput(attrs={'class':'form-control','placeHolder':"Certificate no."}),
                    'others_poi': forms.TextInput(attrs={'class':'form-control','placeHolder':"place of issue"}),


        }


YEAR_CHOICES = [('----','----')]
for r in range((datetime.datetime.now().year-50), (datetime.datetime.now().year+50)):
    YEAR_CHOICES.append((f'{r}',r))
#5
class AcademicDetailsForm(forms.ModelForm):
    elem_from_yr = forms.ChoiceField(  initial='----',choices=YEAR_CHOICES ,widget=forms.Select(attrs={'class': 'form-control'}))
    elem_to_yr = forms.ChoiceField(  initial='----',choices=YEAR_CHOICES ,widget=forms.Select(attrs={'class': 'form-control'}))

    secd_from_yr = forms.ChoiceField(  initial='----',choices=YEAR_CHOICES ,widget=forms.Select(attrs={'class': 'form-control'}))
    secd_to_yr = forms.ChoiceField(  initial='----',choices=YEAR_CHOICES ,widget=forms.Select(attrs={'class': 'form-control'}))

    univ_from_yr = forms.ChoiceField(  initial='----',choices=YEAR_CHOICES ,widget=forms.Select(attrs={'class': 'form-control'}))
    univ_to_yr = forms.ChoiceField(  initial='----',choices=YEAR_CHOICES ,widget=forms.Select(attrs={'class': 'form-control'}))

    profe_from_yr = forms.ChoiceField(  initial='----',choices=YEAR_CHOICES ,widget=forms.Select(attrs={'class': 'form-control'}))
    profe_to_yr = forms.ChoiceField(  initial='----',choices=YEAR_CHOICES ,widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = AcademicDetails
        exclude = ['name']
        widgets = {
                    'elem_noi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
                    'elem_grade':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
                    'secd_noi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
                    'secd_grade':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
                    'univ_noi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
                    'univ_grade':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
                    'profe_noi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
                    'profe_grade':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
                    'addition_skills':forms.TextInput(attrs={'class':'form-control','placeHolder':""})
        }


#6
class LCOCForm(forms.ModelForm):

    ind_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    ind_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    ind_dr = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))

    uk_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    uk_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    uk_dr = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))

    singa_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    singa_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    singa_dr = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))

    aus_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    aus_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    aus_dr = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))

    panama_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    panama_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    panama_dr = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))

    other_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    other_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    other_dr = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    class Meta:
        model=LCOC
        exclude = ['name']
        widgets={
                'ind_grade':forms.TextInput(attrs={'class':'form-control'}),
                'ind_no':forms.TextInput(attrs={'class':'form-control'}),
                'ind_stcw':forms.TextInput(attrs={'class':'form-control','placeholder':'Yes or No'}),

                'uk_grade':forms.TextInput(attrs={'class':'form-control'}),
                'uk_no':forms.TextInput(attrs={'class':'form-control'}),
                'uk_stcw':forms.TextInput(attrs={'class':'form-control','placeholder':'Yes or No'}),

                'aus_grade':forms.TextInput(attrs={'class':'form-control'}),
                'aus_no':forms.TextInput(attrs={'class':'form-control'}),
                'aus_stcw':forms.TextInput(attrs={'class':'form-control','placeholder':'Yes or No'}),

                'singa_grade':forms.TextInput(attrs={'class':'form-control'}),
                'singa_no':forms.TextInput(attrs={'class':'form-control'}),
                'singa_stcw':forms.TextInput(attrs={'class':'form-control','placeholder':'Yes or No'}),

                'panama_grade':forms.TextInput(attrs={'class':'form-control'}),
                'panama_no':forms.TextInput(attrs={'class':'form-control'}),
                'panama_stcw':forms.TextInput(attrs={'class':'form-control','placeholder':'Yes or No'}),

                'other_grade':forms.TextInput(attrs={'class':'form-control'}),
                'other_no':forms.TextInput(attrs={'class':'form-control'}),
                'other_stcw':forms.TextInput(attrs={'class':'form-control','placeholder':'Yes or No'}),

        }



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#7
# class STCWCertificatesForm(forms.ModelForm):
#     class Meta:
#         model = STCWCertificates
#         exclude = ['name']
#         widgets={

#         }



#     aff_certificate_no = forms.CharField(max_length=25)
#     aff_doi = forms.DateField()
#     aff_doe = forms.DateField()
#     aff_poi = forms.CharField(max_length=25)
#     aff_authority = forms.CharField(max_length=50)

#     fp_ff_certificate_no = forms.CharField(max_length=25)
#     fp_ff_doi = forms.DateField()
#     fp_ff_doe = forms.DateField()
#     fp_ff_poi = forms.CharField(max_length=25)
#     fp_ff_authority = forms.CharField(max_length=50)

#     efa_certificate_no = forms.CharField(max_length=25)
#     efa_doi = forms.DateField()
#     efa_doe = forms.DateField()
#     efa_poi = forms.CharField(max_length=25)
#     efa_authority = forms.CharField(max_length=50)

#     mfa_certificate_no = forms.CharField(max_length=25)
#     mfa_doi = forms.DateField()
#     mfa_doe = forms.DateField()
#     mfa_poi = forms.CharField(max_length=25)
#     mfa_authority = forms.CharField(max_length=50)

#     pst_certificate_no = forms.CharField(max_length=25)
#     pst_doi = forms.DateField()
#     pst_doe = forms.DateField()
#     pst_poi = forms.CharField(max_length=25)
#     pst_authority = forms.CharField(max_length=50)

#     pscrb_certificate_no = forms.CharField(max_length=25)
#     pscrb_doi = forms.DateField()
#     pscrb_doe = forms.DateField()
#     pscrb_poi = forms.CharField(max_length=25)
#     pscrb_authority = forms.CharField(max_length=50)

#     pssr_certificate_no = forms.CharField(max_length=25)
#     pssr_doi = forms.DateField()
#     pssr_doe = forms.DateField()
#     pssr_poi = forms.CharField(max_length=25)
#     pssr_authority = forms.CharField(max_length=50)

#     sso_certificate_no = forms.CharField(max_length=25)
#     sso_doi = forms.DateField()
#     sso_doe = forms.DateField()
#     sso_poi = forms.CharField(max_length=25)
#     sso_authority = forms.CharField(max_length=50)

#     stsdsd_certificate_no = forms.CharField(max_length=25)
#     stsdsd_doi = forms.DateField()
#     stsdsd_doe = forms.DateField()
#     stsdsd_poi = forms.CharField(max_length=25)
#     stsdsd_authority = forms.CharField(max_length=50)

#     roc_certificate_no = forms.CharField(max_length=25)
#     roc_doi = forms.DateField()
#     roc_doe = forms.DateField()
#     roc_poi = forms.CharField(max_length=25)
#     roc_authority = forms.CharField(max_length=50)

#     arpa_certificate_no = forms.CharField(max_length=25)
#     arpa_doi = forms.DateField()
#     arpa_doe = forms.DateField()
#     arpa_poi = forms.CharField(max_length=25)
#     arpa_authority = forms.CharField(max_length=50)

#     gmdss_goc_certificate_no = forms.CharField(max_length=25)
#     gmdss_goc_doi = forms.DateField()
#     gmdss_goc_doe = forms.DateField()
#     gmdss_goc_poi = forms.CharField(max_length=25)
#     gmdss_goc_authority = forms.CharField(max_length=50)

#     gmdss_endor_certificate_no = forms.CharField(max_length=25)
#     gmdss_endor_doi = forms.DateField()
#     gmdss_endor_doe = forms.DateField()
#     gmdss_endor_poi = forms.CharField(max_length=25)
#     gmdss_endor_authority = forms.CharField(max_length=50)

#     rau_certificate_no = forms.CharField(max_length=25)
#     rau_doi = forms.DateField()
#     rau_doe = forms.DateField()
#     rau_poi = forms.CharField(max_length=25)
#     rau_authority = forms.CharField(max_length=50)

#     ransco_certificate_no = forms.CharField(max_length=25)
#     ransco_doi = forms.DateField()
#     ransco_doe = forms.DateField()
#     ransco_poi = forms.CharField(max_length=25)
#     ransco_authority = forms.CharField(max_length=50)

#     sms_certificate_no = forms.CharField(max_length=25)
#     sms_doi = forms.DateField()
#     sms_doe = forms.DateField()
#     sms_poi = forms.CharField(max_length=25)
#     sms_authority = forms.CharField(max_length=50)

#     indos_certificate_no = forms.CharField(max_length=25)
#     indos_doi = forms.DateField()
#     indos_doe = forms.DateField()
#     indos_poi = forms.CharField(max_length=25)
#     indos_authority = forms.CharField(max_length=50)

#     simulator_certificate_no = forms.CharField(max_length=25)
#     simulator_doi = forms.DateField()
#     simulator_doe = forms.DateField()
#     simulator_poi = forms.CharField(max_length=25)
#     simulator_authority = forms.CharField(max_length=50)

#     btm_certificate_no = forms.CharField(max_length=25)
#     btm_doi = forms.DateField()
#     btm_doe = forms.DateField()
#     btm_poi = forms.CharField(max_length=25)
#     btm_authority = forms.CharField(max_length=50)

#     marpol_certificate_no = forms.CharField(max_length=25)
#     marpol_doi = forms.DateField()
#     marpol_doe = forms.DateField()
#     marpol_poi = forms.CharField(max_length=25)
#     marpol_authority = forms.CharField(max_length=50)

#     ecdis_ger_certificate_no = forms.CharField(max_length=25)
#     ecdis_ger_doi = forms.DateField()
#     ecdis_ger_doe = forms.DateField()
#     ecdis_ger_poi = forms.CharField(max_length=25)
#     ecdis_ger_authority = forms.CharField(max_length=50)


#     ecdis_specific_certificate_no = forms.CharField(max_length=25)
#     ecdis_specific_doi = forms.DateField()
#     ecdis_specific_doe = forms.DateField()
#     ecdis_specific_poi = forms.CharField(max_length=25)
#     ecdis_specific_authority = forms.CharField(max_length=50)

#     raai_certificate_no = forms.CharField(max_length=25)
#     raai_doi = forms.DateField()
#     raai_doe = forms.DateField()
#     raai_poi = forms.CharField(max_length=25)
#     raai_authority = forms.CharField(max_length=50)

#     brm_certificate_no = forms.CharField(max_length=25)
#     brm_doi = forms.DateField()
#     brm_doe = forms.DateField()
#     brm_poi = forms.CharField(max_length=25)
#     brm_authority = forms.CharField(max_length=50)

#     bwm_certificate_no = forms.CharField(max_length=25)
#     bwm_doi = forms.DateField()
#     bwm_doe = forms.DateField()
#     bwm_poi = forms.CharField(max_length=25)
#     bwm_authority = forms.CharField(max_length=50)

#     lvhsc_certificate_no = forms.CharField(max_length=25)
#     lvhsc_doi = forms.DateField()
#     lvhsc_doe = forms.DateField()
#     lvhsc_poi = forms.CharField(max_length=25)
#     lvhsc_authority = forms.CharField(max_length=50)

#     tasco_certificate_no = forms.CharField(max_length=25)
#     tasco_doi = forms.DateField()
#     tasco_doe = forms.DateField()
#     tasco_poi = forms.CharField(max_length=25)
#     tasco_authority = forms.CharField(max_length=50)

#     chemco_certificate_no = forms.CharField(max_length=25)
#     chemco_doi = forms.DateField()
#     chemco_doe = forms.DateField()
#     chemco_poi = forms.CharField(max_length=25)
#     chemco_authority = forms.CharField(max_length=50)

#     gasco_certificate_no = forms.CharField(max_length=25)
#     gasco_doi = forms.DateField()
#     gasco_doe = forms.DateField()
#     gasco_poi = forms.CharField(max_length=25)
#     gasco_authority = forms.CharField(max_length=50)


#     dce_petro_certificate_no = forms.CharField(max_length=25)
#     dce_petro_doi = forms.DateField()
#     dce_petro_doe = forms.DateField()
#     dce_petro_poi = forms.CharField(max_length=25)
#     dce_petro_authority = forms.CharField(max_length=50)

#     dce_chem_certificate_no = forms.CharField(max_length=25)
#     dce_chem_doi = forms.DateField()
#     dce_chem_doe = forms.DateField()
#     dce_chem_poi = forms.CharField(max_length=25)
#     dce_chem_authority = forms.CharField(max_length=50)

#     dce_gas_certificate_no = forms.CharField(max_length=25)
#     dce_gas_doi = forms.DateField()
#     dce_gas_doe = forms.DateField()
#     dce_gas_poi = forms.CharField(max_length=25)
#     dce_gas_authority = forms.CharField(max_length=50)

#     lcab_certificate_no = forms.CharField(max_length=25)
#     lcab_doi = forms.DateField()
#     lcab_doe = forms.DateField()
#     lcab_poi = forms.CharField(max_length=25)
#     lcab_authority = forms.CharField(max_length=50)

#     me_certificate_no = forms.CharField(max_length=25)
#     me_doi = forms.DateField()
#     me_doe = forms.DateField()
#     me_poi = forms.CharField(max_length=25)
#     me_authority = forms.CharField(max_length=50)

#     sham_certificate_no = forms.CharField(max_length=25)
#     sham_doi = forms.DateField()
#     sham_doe = forms.DateField()
#     sham_poi = forms.CharField(max_length=25)
#     sham_authority = forms.CharField(max_length=50)
class STCWCertificatesForm(forms.ModelForm):
    aff_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    aff_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    fp_ff_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    fp_ff_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    efa_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    efa_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    mfa_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    mfa_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    pst_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    pst_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    pscrb_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    pscrb_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    pssr_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    pssr_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    sso_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    sso_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    stsdsd_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    stsdsd_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    roc_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    roc_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    arpa_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    arpa_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    gmdss_goc_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    gmdss_goc_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    gmdss_endor_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    gmdss_endor_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    rau_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    rau_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    ransco_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    ransco_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    sms_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    sms_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    indos_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    indos_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    simulator_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    simulator_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    btm_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    btm_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    marpol_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    marpol_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    ecdis_ger_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    ecdis_ger_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    ecdis_specific_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    ecdis_specific_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    raai_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    raai_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    brm_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    brm_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    bwm_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    bwm_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    lvhsc_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    lvhsc_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    tasco_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    tasco_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    chemco_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    chemco_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    gasco_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    gasco_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    dce_petro_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    dce_petro_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    dce_chem_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    dce_chem_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    dce_gas_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    dce_gas_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    lcab_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    lcab_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    me_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    me_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    sham_doi = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    sham_doe = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))

    class Meta:
        model= STCWCertificates
        exclude=['name']
        widgets={
            'aff_certificate_no':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'aff_poi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'aff_authority':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'fp_ff_certificate_no':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'fp_ff_poi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'fp_ff_authority':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'efa_certificate_no':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'efa_poi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'efa_authority':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'mfa_certificate_no':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'mfa_poi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'mfa_authority':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'pst_certificate_no':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'pst_poi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'pst_authority':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'pscrb_certificate_no':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'pscrb_poi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'pscrb_authority':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'pssr_certificate_no':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'pssr_poi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'pssr_authority':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'sso_certificate_no':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'sso_poi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'sso_authority':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'stsdsd_certificate_no':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'stsdsd_poi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'stsdsd_authority':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'roc_certificate_no':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'roc_poi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'roc_authority':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'arpa_certificate_no':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'arpa_poi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'arpa_authority':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'gmdss_goc_certificate_no':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'gmdss_goc_poi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'gmdss_goc_authority':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'gmdss_endor_certificate_no':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'gmdss_endor_poi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'gmdss_endor_authority':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'rau_certificate_no':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'rau_poi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'rau_authority':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'ransco_certificate_no':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'ransco_poi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'ransco_authority':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'sms_certificate_no':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'sms_poi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'sms_authority':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'indos_certificate_no':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'indos_poi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'indos_authority':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'simulator_certificate_no':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'simulator_poi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'simulator_authority':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'btm_certificate_no':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'btm_poi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'btm_authority':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'marpol_certificate_no':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'marpol_poi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'marpol_authority':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'ecdis_ger_certificate_no':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'ecdis_ger_poi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'ecdis_ger_authority':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'ecdis_specific_certificate_no':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'ecdis_specific_poi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'ecdis_specific_authority':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'raai_certificate_no':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'raai_poi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'raai_authority':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'brm_certificate_no':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'brm_poi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'brm_authority':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'bwm_certificate_no':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'bwm_poi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'bwm_authority':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'lvhsc_certificate_no':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'lvhsc_poi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'lvhsc_authority':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'tasco_certificate_no':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'tasco_poi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'tasco_authority':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'chemco_certificate_no':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'chemco_poi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'chemco_authority':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'gasco_certificate_no':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'gasco_poi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'gasco_authority':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'dce_petro_certificate_no':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'dce_petro_poi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'dce_petro_authority':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'dce_chem_certificate_no':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'dce_chem_poi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'dce_chem_authority':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'dce_gas_certificate_no':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'dce_gas_poi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'dce_gas_authority':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'lcab_certificate_no':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'lcab_poi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'lcab_authority':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'me_certificate_no':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'me_poi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'me_authority':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'sham_certificate_no':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'sham_poi':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),
            'sham_authority':forms.TextInput(attrs={'class':'form-control','placeHolder':""}),


        }

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#8
# class ReferenceForm(forms.ModelForm):
#     class Meta:
#         model = Reference
#         exclude=['name']
#     widgets={
#     'name1': forms.TextInput(attrs={'class':'form-control '}),
#     'company': forms.TextInput(attrs={'class':'form-control'}),
#     'contact': forms.TextInput(attrs={'class':'form-control'})
#     }

#9
class AboutUSForm(forms.ModelForm):

    comapany = forms.BooleanField(required=False,
                                      initial=False,
                                      label='Yes')
    marin_club = forms.BooleanField(required=False,
                                      initial=False,
                                      label='Extra cheeze')
    marin_magzin = forms.BooleanField(required=False,
                                      initial=False,
                                      label='Extra cheeze')
    newspaper = forms.BooleanField(required=False,
                                      initial=False,
                                      label='Extra cheeze')
    friend = forms.BooleanField(required=False,
                                      initial=False,
                                      label='Extra cheeze')
    mail = forms.BooleanField(required=False,
                                      initial=False,
                                      label='Extra cheeze')
    other = forms.BooleanField(required=False,
                                      initial=False,
                                      label='Extra cheeze')
    class Meta:
        model= AboutUS
        exclude=['name']


#10
class LDWForm(forms.ModelForm):
    class Meta:
        model=LDW
        exclude=['name']
        widgets={
            'ldw':forms.TextInput(attrs={'class':'form-control '}),
            }
#11
class PersonalDetailsForm(forms.ModelForm):
    decision={
                ('----',"----"),
        ('No',"No"),
        ('Yes',"Yes")
    }
    major_illness=forms.ChoiceField(  required=False,initial='----',choices=decision ,widget=forms.Select(attrs={'class': 'form-control'}))
    defect_in_hearing=forms.ChoiceField(  required=False,initial='----',choices=decision ,widget=forms.Select(attrs={'class': 'form-control'}))
    defect_in_vision=forms.ChoiceField(  required=False,initial='----',choices=decision ,widget=forms.Select(attrs={'class': 'form-control'}))
    defect_in_speech=forms.ChoiceField(  required=False,initial='----',choices=decision ,widget=forms.Select(attrs={'class': 'form-control'}))
    affected_climate=forms.ChoiceField(  required=False,initial='----',choices=decision ,widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model=PersonalDetails
        exclude = ['name']
        widgets={

    'height' : forms.TextInput(attrs={'class':'form-control '}),
    'weight' :forms.TextInput(attrs={'class':'form-control '}),
    'BMI' :forms.TextInput(attrs={'class':'form-control '}),
    'color_of_eye' :forms.TextInput(attrs={'class':'form-control '}),
    'color_of_hair' :forms.TextInput(attrs={'class':'form-control '}),
        'major_illness_res' :forms.TextInput(attrs={'class':'form-control ','placeholder':'Details'}),

    'state':forms.TextInput(attrs={'class':'form-control '})
        }
#12
class Additional_infoForm(forms.ModelForm):
    decision={
                ('----',"----"),

        ('Yes',"Yes"),
        ('No',"No")
    }
    suspended_from=forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    suspended_to=forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    applied =forms.ChoiceField(  initial='----',choices=decision ,required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    criminal_offence =forms.ChoiceField(  initial='----',choices=decision ,required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    aicoba =forms.ChoiceField(  initial='----',choices=decision ,required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    applied =forms.ChoiceField(  initial='----',choices=decision ,required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    suspended =forms.ChoiceField(  initial='----',choices=decision ,required=False,widget=forms.Select(attrs={'class': 'form-control'}))
    ship_incident  =forms.ChoiceField(  initial='----',choices=decision ,required=False,widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Additional_info
        exclude=['name']
        widgets={
            'criminal_offence_details' :forms.TextInput(attrs={'class':'form-control ',}),

            'ship_incident_details' :forms.TextInput(attrs={'class':'form-control '}),
        }



#13
class Reason_for_appForm(forms.ModelForm):
    decision={
                ('----',"----"),
        ('Yes',"Yes"),
        ('No',"No")
    }
    reference  =forms.ChoiceField(  required=False,initial='----',choices=decision ,widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Reason_for_app
        exclude=['name']
        widgets={
    'present_emp' : forms.TextInput(attrs={'class':'form-control '}),
    'support_application' : forms.TextInput(attrs={'class':'form-control '}),
    'contact_details': forms.TextInput(attrs={'class':'form-control '}),
    'attend_interview': forms.TextInput(attrs={'class':'form-control '})
        }
#14
class SEA_ExpForm(forms.Form):

    employer = forms.CharField(required=False,max_length=50)
    rpsl = forms.CharField(required=False,max_length=25)
    vessel_name= forms.CharField(required=False,max_length=25)
    steam_motor = forms.CharField(required=False,max_length=25)
    dwt_grt = forms.CharField(required=False,max_length=25)
    rank = forms.CharField(required=False,max_length=25)
    engine = forms.CharField(required=False,max_length=25)
    bhp = forms.CharField(required=False,max_length=25)
    engin_room = forms.CharField(required=False,max_length=25)
    date_from = forms.DateField(required=False,)
    date_to = forms.DateField(required=False,)
    total =forms.CharField(required=False,max_length=10)


#15


#16
class DeclarationForm(forms.ModelForm):
    date = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date','class': 'form-control'}))
    class Meta:
        model=Declaration
        exclude=['name']

