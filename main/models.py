
from email.policy import default
from pickle import TRUE
from django.db import models
from django.forms import Textarea
from django_countries.fields import CountryField

# Create your models here.


# 1
class profileDetails(models.Model):


    id = models.AutoField(primary_key=True)
    fname=models.CharField(max_length=50,default="")
    mname=models.CharField(max_length=50,default="")
    lname=models.CharField(max_length=50,default="")
    dob=models.DateField(default="")
    pob=models.CharField(max_length=50,default="")

    nationality = CountryField()
    marritial_status=models.CharField(max_length=20)
    smoker=models.CharField(max_length=10)


    add1 = models.TextField(default="")
    city= models.CharField(max_length=50,default="")
    zip= models.IntegerField(default="")
    pno = models.CharField(max_length=12,default="")
    airport= models.CharField(max_length=100,default="")
    email=models.EmailField(max_length=50,default="")
    insta= models.CharField(max_length=500,null=True, blank=True)
    facebook= models.CharField(max_length=500,null=True, blank=True)
    linkedin= models.CharField(max_length=500,null=True, blank=True)
    twitter= models.CharField(max_length=500,null=True, blank=True)

    add2 = models.TextField(null=True, blank=True)
    city2= models.CharField(max_length=50,null=True, blank=True)
    zip2= models.IntegerField(null=True, blank=True)
    pno2 = models.CharField(max_length=12,null=True, blank=True)
    airport2= models.CharField(max_length=100,default="")
    email2=models.EmailField(max_length=50,null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)

class ATOC(models.Model):
    name= models.ForeignKey(profileDetails, on_delete=models.CASCADE)
    agency=models.CharField(max_length=50,null=True,blank=True)
    rank=models.CharField(max_length=50,null=True, blank=True)
    ms_rank=models.CharField(max_length=50,null=True, blank=True)
    doa=models.DateField(null=True, default='',blank=True)

    doa2=models.DateField(null=True, default='',blank=True)

#2
class NKD_de(models.Model):
    name = models.OneToOneField(profileDetails,on_delete=models.CASCADE)
    name_rela = models.CharField(max_length=500,null=True, blank=True)
    relation = models.CharField(max_length=50,null=True,blank=True)
    add_nkd = models.TextField(null=True, blank=True)
class NKD(models.Model):
    name = models.ForeignKey(profileDetails,on_delete=models.CASCADE)

    nkd_name_no = models.CharField(max_length=500,default='NA', blank=True,null=True)
    nkd_rela_no= models.CharField(max_length=500,default='NA', blank=True,null=True)
    nkd_dob_no = models.DateField(blank=True,null=True,default='')
    nkd_ppno_no= models.CharField(max_length=500,default='NA', blank=True,null=True,)

#3
class PassportDetails(models.Model):
    name = models.OneToOneField(profileDetails,on_delete=models.CASCADE)
    pass_no = models.CharField(max_length=50,null=True, blank=True)
    pass_poi = models.CharField(max_length=200,null=True, blank=True)
    pass_doi=models.DateField(null=True, blank=True,default='')
    pass_doe = models.DateField(null=True, blank=True,default='')

    visa_no = models.CharField(max_length=50,null=True, blank=True)
    visa_poi = models.CharField(max_length=200,null=True, blank=True)
    visa_doi=models.DateField(null=True, blank=True,default='')
    visa_doe = models.DateField(null=True, blank=True,default='')

    yellow_fever_no = models.CharField(max_length=50,null=True, blank=True)
    yellow_fever_poi = models.CharField(max_length=200,null=True, blank=True)
    yellow_fever_doi=models.DateField(null=True, blank=True,default='')
    yellow_fever_doe = models.DateField(null=True, blank=True,default='')

#4
class CDCSB(models.Model):
    name = models.OneToOneField(profileDetails,on_delete=models.CASCADE)
    ind_no=models.CharField(max_length=20,blank=True,null=True,default='')
    ind_poi = models.CharField(max_length=50,blank=True,null=True,default='')
    ind_doi = models.DateField(null=True, blank=True,default='')
    ind_doe = models.DateField(null=True, blank=True,default='')

    panama_no=models.CharField(max_length=20,blank=True,null=True,default='')
    panama_poi = models.CharField(max_length=50,blank=True,null=True,default='')
    panama_doi = models.DateField(null=True, blank=True,default='')
    panama_doe = models.DateField(null=True, blank=True,default='')

    others_no=models.CharField(max_length=20,blank=True,null=True,default='')
    others_poi = models.CharField(max_length=50,blank=True,null=True,default='')
    others_doi = models.DateField(null=True, blank=True,default='')
    others_doe = models.DateField(null=True, blank=True,default='')

#5
class AcademicDetails(models.Model):
    name = models.OneToOneField(profileDetails,on_delete=models.CASCADE)

    elem_noi=models.CharField(max_length=1000,blank=True,null=True,default='')
    elem_grade = models.CharField(max_length=50,blank=True,null=True,default='')
    elem_from_yr = models.CharField(max_length=4,blank=True,null=True,default='')
    elem_to_yr =models.CharField(max_length=4,blank=True,null=True,default='')

    secd_noi=models.CharField(max_length=1000,blank=True,null=True,default='')
    secd_grade = models.CharField(max_length=50,blank=True,null=True,default='')
    secd_from_yr =models.CharField(max_length=4,blank=True,null=True,default='')
    secd_to_yr =models.CharField(max_length=4,blank=True,null=True,default='')

    univ_noi=models.CharField(max_length=1000,blank=True,null=True,default='')
    univ_grade = models.CharField(max_length=50,blank=True,null=True,default='')
    univ_from_yr =models.CharField(max_length=4,blank=True,null=True,default='')
    univ_to_yr =models.CharField(max_length=4,blank=True,null=True,default='')

    profe_noi=models.CharField(max_length=1000,blank=True,null=True,default='')
    profe_grade = models.CharField(max_length=50,blank=True,null=True,default='')
    profe_from_yr =models.CharField(max_length=4,blank=True,null=True,default='')
    profe_to_yr =models.CharField(max_length=4,blank=True,null=True,default='')

    addition_skills = models.CharField(max_length=1000,blank=True,null=True)

#6
class LCOC(models.Model):
    name = models.OneToOneField(profileDetails,on_delete=models.CASCADE)

    ind_grade=models.CharField(max_length=50,blank=True,null=True,default='')
    ind_no = models.CharField(max_length=50,blank=True,null=True,default='')
    ind_doi = models.DateField(blank=True,null=True,default='')
    ind_doe = models.DateField(blank=True,null=True,default='')
    ind_dr = models.DateField(blank=True,null=True,default='')
    ind_stcw = models.CharField(max_length=5,blank=True,null=True,default='')
    
    uk_grade=models.CharField(max_length=50,blank=True,null=True,default='')
    uk_no = models.CharField(max_length=50,blank=True,null=True,default='')
    uk_doi = models.DateField(blank=True,null=True,default='')
    uk_doe = models.DateField(blank=True,null=True,default='')
    uk_dr = models.DateField(blank=True,null=True,default='')
    uk_stcw = models.CharField(max_length=5,blank=True,null=True,default='')
    
    aus_grade=models.CharField(max_length=50,blank=True,null=True,default='')
    aus_no = models.CharField(max_length=50,blank=True,null=True,default='')
    aus_doi = models.DateField(blank=True,null=True,default='')
    aus_doe = models.DateField(blank=True,null=True,default='')
    aus_dr = models.DateField(blank=True,null=True,default='')
    aus_stcw = models.CharField(max_length=5,blank=True,null=True,default='')

    singa_grade=models.CharField(max_length=50,blank=True,null=True,default='')
    singa_no = models.CharField(max_length=50,blank=True,null=True,default='')
    singa_doi = models.DateField(blank=True,null=True,default='')
    singa_doe = models.DateField(blank=True,null=True,default='')
    singa_dr = models.DateField(blank=True,null=True,default='')
    singa_stcw = models.CharField(max_length=5,blank=True,null=True,default='')


    panama_grade=models.CharField(max_length=50,blank=True,null=True,default='')
    panama_no = models.CharField(max_length=50,blank=True,null=True,default='')
    panama_doi = models.DateField(blank=True,null=True,default='')
    panama_doe = models.DateField(blank=True,null=True,default='')
    panama_dr = models.DateField(blank=True,null=True,default='')
    panama_stcw = models.CharField(max_length=5,blank=True,null=True,default='')

    other_grade=models.CharField(max_length=50,blank=True,null=True,default='')
    other_no = models.CharField(max_length=50,blank=True,null=True,default='')
    other_doi = models.DateField(blank=True,null=True,default='')
    other_doe = models.DateField(blank=True,null=True,default='')
    other_dr = models.DateField(blank=True,null=True,default='')
    other_stcw = models.CharField(max_length=5,blank=True,null=True,default='')


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#7
class STCWCertificates(models.Model):
    name = models.OneToOneField(profileDetails,on_delete=models.CASCADE)

    aff_certificate_no = models.CharField(max_length=25,blank=True,null=True,default='')
    aff_doi = models.DateField(blank=True,null=True,default='')
    aff_doe = models.DateField(blank=True,null=True,default='')
    aff_poi = models.CharField(max_length=25,blank=True,null=True,default='')
    aff_authority = models.CharField(max_length=50,blank=True,null=True,default='')

    fp_ff_certificate_no = models.CharField(max_length=25,blank=True,null=True,default='')
    fp_ff_doi = models.DateField(blank=True,null=True,default='')
    fp_ff_doe = models.DateField(blank=True,null=True,default='')
    fp_ff_poi = models.CharField(max_length=25,blank=True,null=True,default='')
    fp_ff_authority = models.CharField(max_length=50,blank=True,null=True,default='')

    efa_certificate_no = models.CharField(max_length=25,blank=True,null=True,default='')
    efa_doi = models.DateField(blank=True,null=True,default='')
    efa_doe = models.DateField(blank=True,null=True,default='')
    efa_poi = models.CharField(max_length=25,blank=True,null=True,default='')
    efa_authority = models.CharField(max_length=50,blank=True,null=True,default='')

    mfa_certificate_no = models.CharField(max_length=25,blank=True,null=True,default='')
    mfa_doi = models.DateField(blank=True,null=True,default='')
    mfa_doe = models.DateField(blank=True,null=True,default='')
    mfa_poi = models.CharField(max_length=25,blank=True,null=True,default='')
    mfa_authority = models.CharField(max_length=50,blank=True,null=True,default='')

    pst_certificate_no = models.CharField(max_length=25,blank=True,null=True,default='')
    pst_doi = models.DateField(blank=True,null=True,default='')
    pst_doe = models.DateField(blank=True,null=True,default='')
    pst_poi = models.CharField(max_length=25,blank=True,null=True,default='')
    pst_authority = models.CharField(max_length=50,blank=True,null=True,default='')

    pscrb_certificate_no = models.CharField(max_length=25,blank=True,null=True,default='')
    pscrb_doi = models.DateField(blank=True,null=True,default='')
    pscrb_doe = models.DateField(blank=True,null=True,default='')
    pscrb_poi = models.CharField(max_length=25,blank=True,null=True,default='')
    pscrb_authority = models.CharField(max_length=50,blank=True,null=True,default='')

    pssr_certificate_no = models.CharField(max_length=25,blank=True,null=True,default='')
    pssr_doi = models.DateField(blank=True,null=True,default='')
    pssr_doe = models.DateField(blank=True,null=True,default='')
    pssr_poi = models.CharField(max_length=25,blank=True,null=True,default='')
    pssr_authority = models.CharField(max_length=50,blank=True,null=True,default='')

    sso_certificate_no = models.CharField(max_length=25,blank=True,null=True,default='')
    sso_doi = models.DateField(blank=True,null=True,default='')
    sso_doe = models.DateField(blank=True,null=True,default='')
    sso_poi = models.CharField(max_length=25,blank=True,null=True,default='')
    sso_authority = models.CharField(max_length=50,blank=True,null=True,default='')

    stsdsd_certificate_no = models.CharField(max_length=25,blank=True,null=True,default='')
    stsdsd_doi = models.DateField(blank=True,null=True,default='')
    stsdsd_doe = models.DateField(blank=True,null=True,default='')
    stsdsd_poi = models.CharField(max_length=25,blank=True,null=True,default='')
    stsdsd_authority = models.CharField(max_length=50,blank=True,null=True,default='')

    roc_certificate_no = models.CharField(max_length=25,blank=True,null=True,default='')
    roc_doi = models.DateField(blank=True,null=True,default='')
    roc_doe = models.DateField(blank=True,null=True,default='')
    roc_poi = models.CharField(max_length=25,blank=True,null=True,default='')
    roc_authority = models.CharField(max_length=50,blank=True,null=True,default='')

    arpa_certificate_no = models.CharField(max_length=25,blank=True,null=True,default='')
    arpa_doi = models.DateField(blank=True,null=True,default='')
    arpa_doe = models.DateField(blank=True,null=True,default='')
    arpa_poi = models.CharField(max_length=25,blank=True,null=True,default='')
    arpa_authority = models.CharField(max_length=50,blank=True,null=True,default='')

    gmdss_goc_certificate_no = models.CharField(max_length=25,blank=True,null=True,default='')
    gmdss_goc_doi = models.DateField(blank=True,null=True,default='')
    gmdss_goc_doe = models.DateField(blank=True,null=True,default='')
    gmdss_goc_poi = models.CharField(max_length=25,blank=True,null=True,default='')
    gmdss_goc_authority = models.CharField(max_length=50,blank=True,null=True,default='')

    gmdss_endor_certificate_no = models.CharField(max_length=25,blank=True,null=True,default='')
    gmdss_endor_doi = models.DateField(blank=True,null=True,default='')
    gmdss_endor_doe = models.DateField(blank=True,null=True,default='')
    gmdss_endor_poi = models.CharField(max_length=25,blank=True,null=True,default='')
    gmdss_endor_authority = models.CharField(max_length=50,blank=True,null=True,default='')

    rau_certificate_no = models.CharField(max_length=25,blank=True,null=True,default='')
    rau_doi = models.DateField(blank=True,null=True,default='')
    rau_doe = models.DateField(blank=True,null=True,default='')
    rau_poi = models.CharField(max_length=25,blank=True,null=True,default='')
    rau_authority = models.CharField(max_length=50,blank=True,null=True,default='')

    ransco_certificate_no = models.CharField(max_length=25,blank=True,null=True,default='')
    ransco_doi = models.DateField(blank=True,null=True,default='')
    ransco_doe = models.DateField(blank=True,null=True,default='')
    ransco_poi = models.CharField(max_length=25,blank=True,null=True,default='')
    ransco_authority = models.CharField(max_length=50,blank=True,null=True,default='')

    sms_certificate_no = models.CharField(max_length=25,blank=True,null=True,default='')
    sms_doi = models.DateField(blank=True,null=True,default='')
    sms_doe = models.DateField(blank=True,null=True,default='')
    sms_poi = models.CharField(max_length=25,blank=True,null=True,default='')
    sms_authority = models.CharField(max_length=50,blank=True,null=True,default='')

    indos_certificate_no = models.CharField(max_length=25,blank=True,null=True,default='')
    indos_doi = models.DateField(blank=True,null=True,default='')
    indos_doe = models.DateField(blank=True,null=True,default='')
    indos_poi = models.CharField(max_length=25,blank=True,null=True,default='')
    indos_authority = models.CharField(max_length=50,blank=True,null=True,default='')

    simulator_certificate_no = models.CharField(max_length=25,blank=True,null=True,default='')
    simulator_doi = models.DateField(blank=True,null=True,default='')
    simulator_doe = models.DateField(blank=True,null=True,default='')
    simulator_poi = models.CharField(max_length=25,blank=True,null=True,default='')
    simulator_authority = models.CharField(max_length=50,blank=True,null=True,default='')

    btm_certificate_no = models.CharField(max_length=25,blank=True,null=True,default='')
    btm_doi = models.DateField(blank=True,null=True,default='')
    btm_doe = models.DateField(blank=True,null=True,default='')
    btm_poi = models.CharField(max_length=25,blank=True,null=True,default='')
    btm_authority = models.CharField(max_length=50,blank=True,null=True,default='')

    marpol_certificate_no = models.CharField(max_length=25,blank=True,null=True,default='')
    marpol_doi = models.DateField(blank=True,null=True,default='')
    marpol_doe = models.DateField(blank=True,null=True,default='')
    marpol_poi = models.CharField(max_length=25,blank=True,null=True,default='')
    marpol_authority = models.CharField(max_length=50,blank=True,null=True,default='')

    ecdis_ger_certificate_no = models.CharField(max_length=25,blank=True,null=True,default='')
    ecdis_ger_doi = models.DateField(blank=True,null=True,default='')
    ecdis_ger_doe = models.DateField(blank=True,null=True,default='')
    ecdis_ger_poi = models.CharField(max_length=25,blank=True,null=True,default='')
    ecdis_ger_authority = models.CharField(max_length=50,blank=True,null=True,default='')


    ecdis_specific_certificate_no = models.CharField(max_length=25,blank=True,null=True,default='')
    ecdis_specific_doi = models.DateField(blank=True,null=True,default='')
    ecdis_specific_doe = models.DateField(blank=True,null=True,default='')
    ecdis_specific_poi = models.CharField(max_length=25,blank=True,null=True,default='')
    ecdis_specific_authority = models.CharField(max_length=50,blank=True,null=True,default='')

    raai_certificate_no = models.CharField(max_length=25,blank=True,null=True,default='')
    raai_doi = models.DateField(blank=True,null=True,default='')
    raai_doe = models.DateField(blank=True,null=True,default='')
    raai_poi = models.CharField(max_length=25,blank=True,null=True,default='')
    raai_authority = models.CharField(max_length=50,blank=True,null=True,default='')

    brm_certificate_no = models.CharField(max_length=25,blank=True,null=True,default='')
    brm_doi = models.DateField(blank=True,null=True,default='')
    brm_doe = models.DateField(blank=True,null=True,default='')
    brm_poi = models.CharField(max_length=25,blank=True,null=True,default='')
    brm_authority = models.CharField(max_length=50,blank=True,null=True,default='')

    bwm_certificate_no = models.CharField(max_length=25,blank=True,null=True,default='')
    bwm_doi = models.DateField(blank=True,null=True,default='')
    bwm_doe = models.DateField(blank=True,null=True,default='')
    bwm_poi = models.CharField(max_length=25,blank=True,null=True,default='')
    bwm_authority = models.CharField(max_length=50,blank=True,null=True,default='')

    lvhsc_certificate_no = models.CharField(max_length=25,blank=True,null=True,default='')
    lvhsc_doi = models.DateField(blank=True,null=True,default='')
    lvhsc_doe = models.DateField(blank=True,null=True,default='')
    lvhsc_poi = models.CharField(max_length=25,blank=True,null=True,default='')
    lvhsc_authority = models.CharField(max_length=50,blank=True,null=True,default='')

    tasco_certificate_no = models.CharField(max_length=25,blank=True,null=True,default='')
    tasco_doi = models.DateField(blank=True,null=True,default='')
    tasco_doe = models.DateField(blank=True,null=True,default='')
    tasco_poi = models.CharField(max_length=25,blank=True,null=True,default='')
    tasco_authority = models.CharField(max_length=50,blank=True,null=True,default='')

    chemco_certificate_no = models.CharField(max_length=25,blank=True,null=True,default='')
    chemco_doi = models.DateField(blank=True,null=True,default='')
    chemco_doe = models.DateField(blank=True,null=True,default='')
    chemco_poi = models.CharField(max_length=25,blank=True,null=True,default='')
    chemco_authority = models.CharField(max_length=50,blank=True,null=True,default='')

    gasco_certificate_no = models.CharField(max_length=25,blank=True,null=True,default='')
    gasco_doi = models.DateField(blank=True,null=True,default='')
    gasco_doe = models.DateField(blank=True,null=True,default='')
    gasco_poi = models.CharField(max_length=25,blank=True,null=True,default='')
    gasco_authority = models.CharField(max_length=50,blank=True,null=True,default='')


    dce_petro_certificate_no = models.CharField(max_length=25,blank=True,null=True,default='')
    dce_petro_doi = models.DateField(blank=True,null=True,default='')
    dce_petro_doe = models.DateField(blank=True,null=True,default='')
    dce_petro_poi = models.CharField(max_length=25,blank=True,null=True,default='')
    dce_petro_authority = models.CharField(max_length=50,blank=True,null=True,default='')

    dce_chem_certificate_no = models.CharField(max_length=25,blank=True,null=True,default='')
    dce_chem_doi = models.DateField(blank=True,null=True,default='')
    dce_chem_doe = models.DateField(blank=True,null=True,default='')
    dce_chem_poi = models.CharField(max_length=25,blank=True,null=True,default='')
    dce_chem_authority = models.CharField(max_length=50,blank=True,null=True,default='')

    dce_gas_certificate_no = models.CharField(max_length=25,blank=True,null=True,default='')
    dce_gas_doi = models.DateField(blank=True,null=True,default='')
    dce_gas_doe = models.DateField(blank=True,null=True,default='')
    dce_gas_poi = models.CharField(max_length=25,blank=True,null=True,default='')
    dce_gas_authority = models.CharField(max_length=50,blank=True,null=True,default='')

    lcab_certificate_no = models.CharField(max_length=25,blank=True,null=True,default='')
    lcab_doi = models.DateField(blank=True,null=True,default='')
    lcab_doe = models.DateField(blank=True,null=True,default='')
    lcab_poi = models.CharField(max_length=25,blank=True,null=True,default='')
    lcab_authority = models.CharField(max_length=50,blank=True,null=True,default='')

    me_certificate_no = models.CharField(max_length=25,blank=True,null=True,default='')
    me_doi = models.DateField(blank=True,null=True,default='')
    me_doe = models.DateField(blank=True,null=True,default='')
    me_poi = models.CharField(max_length=25,blank=True,null=True,default='')
    me_authority = models.CharField(max_length=50,blank=True,null=True,default='')

    sham_certificate_no = models.CharField(max_length=25,blank=True,null=True,default='')
    sham_doi = models.DateField(blank=True,null=True,default='')
    sham_doe = models.DateField(blank=True,null=True,default='')
    sham_poi = models.CharField(max_length=25,blank=True,null=True,default='')
    sham_authority = models.CharField(max_length=50,blank=True,null=True,default='')


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#8
class Reference(models.Model):

    name = models.ForeignKey(profileDetails,on_delete=models.CASCADE)
    name1 = models.CharField(max_length=100,blank=True,null=True,default='')
    company= models.CharField(max_length=100,blank=True,null=True,default='')
    contact= models.CharField(max_length=20,blank=True,null=True,default='')


#9
class AboutUS(models.Model):
    name = models.OneToOneField(profileDetails,on_delete=models.CASCADE)

    comapany = models.BooleanField(default=False)
    marin_club = models.BooleanField(default=False)
    marin_magzin = models.BooleanField(default=False)
    newspaper = models.BooleanField(default=False)
    friend = models.BooleanField(default=False)
    mail = models.BooleanField(default=False)
    other = models.BooleanField(default=False)


#10
class LDW(models.Model):
    name = models.OneToOneField(profileDetails,on_delete=models.CASCADE)

    ldw = models.CharField(max_length=5,blank=True,null=True,default='')

#11
class PersonalDetails(models.Model):
    name = models.OneToOneField(profileDetails,on_delete=models.CASCADE)

    height = models.CharField(max_length=10,blank=True,null=True,default='')
    weight = models.CharField(max_length=10,blank=True,null=True,default='')
    BMI = models.CharField(max_length=10,blank=True,null=True,default='')
    color_of_eye = models.CharField(max_length=10,blank=True,null=True,default='')
    color_of_hair = models.CharField(max_length=10,blank=True,null=True,default='')
    major_illness = models.CharField(max_length=500,blank=True,null=True,default='')
    major_illness_res = models.CharField(max_length=1000,blank=True,null=True,default='')
    defect_in_hearing = models.CharField(max_length=5,blank=True,null=True,default='')
    defect_in_vision = models.CharField(max_length=5,blank=True,null=True,default='')
    defect_in_speech = models.CharField(max_length=5,blank=True,null=True,default='')
    affected_climate = models.CharField(max_length=100,blank=True,null=True,default='')
    state= models.CharField(max_length=100,blank=True,null=True,default='')

#12
class Additional_info(models.Model):
    name = models.OneToOneField(profileDetails,on_delete=models.CASCADE)

    applied = models.CharField(max_length=10,blank=True,null=True,default='')
    aicoba = models.CharField(max_length=10,blank=True,null=True,default='')
    criminal_offence = models.CharField(max_length=10,blank=True,null=True,default='')
    criminal_offence_details = models.TextField(blank=True,null=True,default='')

    ship_incident = models.CharField(max_length=10,blank=True,null=True,default='')
    ship_incident_details= models.TextField(blank=True,null=True,default='')
    suspended = models.CharField(max_length=10,blank=True,null=True,default='')
    suspended_from = models.DateField(blank=True,null=True,default='')
    suspended_to= models.DateField(blank=True,null=True,default='')


#13
class Reason_for_app(models.Model):
    name = models.OneToOneField(profileDetails,on_delete=models.CASCADE)

    present_emp = models.TextField(blank=True,null=True,default='')
    support_application = models.TextField(blank=True,null=True,default='')
    reference = models.CharField(max_length=5,blank=True,null=True,default='')
    contact_details= models.TextField(blank=True,null=True,default='')
    attend_interview= models.TextField(blank=True,null=True,default='')

#14
class SEA_Exp(models.Model):
    name = models.ForeignKey(profileDetails,on_delete=models.CASCADE)

    employer = models.CharField(max_length=50,blank=True,null=True,default='')
    rpsl = models.CharField(max_length=25,blank=True,null=True,default='')
    vessel_name= models.CharField(max_length=25,blank=True,null=True,default='')
    steam_motor = models.CharField(max_length=25,blank=True,null=True,default='')
    dwt_grt = models.CharField(max_length=25,blank=True,null=True,default='')
    rank = models.CharField(max_length=25,blank=True,null=True,default='')
    engine = models.CharField(max_length=25,blank=True,null=True,default='')
    bhp = models.CharField(max_length=25,blank=True,null=True,default='')
    engin_room = models.CharField(max_length=10,blank=True,null=True,default='')
    date_from = models.DateField(blank=True,null=True,default='')
    date_to = models.DateField(blank=True,null=True,default='')
    total =models.CharField(max_length=10,blank=True,null=True,default='')


#15
class OSS(models.Model):
    name = models.ForeignKey(profileDetails,on_delete=models.CASCADE)

    employer= models.CharField(max_length=50,blank=True,null=True,default='')
    title= models.CharField(max_length=50,blank=True,null=True,default='')
    workshop= models.CharField(max_length=50,blank=True,null=True,default='')
    major_machine= models.CharField(max_length=50,blank=True,null=True,default='')
    supervised= models.CharField(max_length=50,blank=True,null=True,default='')
    size= models.CharField(max_length=50,blank=True,null=True,default='')
    period_frm = models.DateField(blank=True,null=True,default='')
    period_to = models.DateField(blank=True,null=True,default='')
    other_info = models.CharField(max_length=200,blank=True,null=True,default='')

#16
class Declaration(models.Model):
    name = models.OneToOneField(profileDetails,on_delete=models.CASCADE)

    date=models.DateField(blank=True,null=True,default='')
    photo = models.ImageField(default='',blank=True,null=True,upload_to='photo/')
    signature = models.ImageField(default='',blank=True,null=True,upload_to='signatures/')








