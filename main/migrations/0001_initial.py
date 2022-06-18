# Generated by Django 3.2.6 on 2022-06-16 11:32

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profileDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('dob', models.DateField(default='')),
                ('pob', models.CharField(default='', max_length=50)),
                ('nationality', django_countries.fields.CountryField(max_length=2)),
                ('marritial_status', models.CharField(max_length=20)),
                ('smoker', models.CharField(max_length=10)),
                ('add1', models.TextField(default='')),
                ('city', models.CharField(default='', max_length=50)),
                ('zip', models.IntegerField(default='')),
                ('pno', models.CharField(default='', max_length=12)),
                ('airport', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(default='', max_length=50)),
                ('insta', models.CharField(blank=True, max_length=500, null=True)),
                ('facebook', models.CharField(blank=True, max_length=500, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=500, null=True)),
                ('twitter', models.CharField(blank=True, max_length=500, null=True)),
                ('add2', models.TextField(blank=True, null=True)),
                ('city2', models.CharField(blank=True, max_length=50, null=True)),
                ('zip2', models.IntegerField(blank=True, null=True)),
                ('pno2', models.CharField(blank=True, max_length=12, null=True)),
                ('airport2', models.CharField(default='', max_length=100)),
                ('email2', models.EmailField(blank=True, max_length=50, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='STCWCertificates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aff_certificate_no', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('aff_doi', models.DateField(blank=True, default='', null=True)),
                ('aff_doe', models.DateField(blank=True, default='', null=True)),
                ('aff_poi', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('aff_authority', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('fp_ff_certificate_no', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('fp_ff_doi', models.DateField(blank=True, default='', null=True)),
                ('fp_ff_doe', models.DateField(blank=True, default='', null=True)),
                ('fp_ff_poi', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('fp_ff_authority', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('efa_certificate_no', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('efa_doi', models.DateField(blank=True, default='', null=True)),
                ('efa_doe', models.DateField(blank=True, default='', null=True)),
                ('efa_poi', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('efa_authority', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('mfa_certificate_no', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('mfa_doi', models.DateField(blank=True, default='', null=True)),
                ('mfa_doe', models.DateField(blank=True, default='', null=True)),
                ('mfa_poi', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('mfa_authority', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('pst_certificate_no', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('pst_doi', models.DateField(blank=True, default='', null=True)),
                ('pst_doe', models.DateField(blank=True, default='', null=True)),
                ('pst_poi', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('pst_authority', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('pscrb_certificate_no', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('pscrb_doi', models.DateField(blank=True, default='', null=True)),
                ('pscrb_doe', models.DateField(blank=True, default='', null=True)),
                ('pscrb_poi', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('pscrb_authority', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('pssr_certificate_no', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('pssr_doi', models.DateField(blank=True, default='', null=True)),
                ('pssr_doe', models.DateField(blank=True, default='', null=True)),
                ('pssr_poi', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('pssr_authority', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('sso_certificate_no', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('sso_doi', models.DateField(blank=True, default='', null=True)),
                ('sso_doe', models.DateField(blank=True, default='', null=True)),
                ('sso_poi', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('sso_authority', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('stsdsd_certificate_no', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('stsdsd_doi', models.DateField(blank=True, default='', null=True)),
                ('stsdsd_doe', models.DateField(blank=True, default='', null=True)),
                ('stsdsd_poi', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('stsdsd_authority', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('roc_certificate_no', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('roc_doi', models.DateField(blank=True, default='', null=True)),
                ('roc_doe', models.DateField(blank=True, default='', null=True)),
                ('roc_poi', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('roc_authority', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('arpa_certificate_no', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('arpa_doi', models.DateField(blank=True, default='', null=True)),
                ('arpa_doe', models.DateField(blank=True, default='', null=True)),
                ('arpa_poi', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('arpa_authority', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('gmdss_goc_certificate_no', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('gmdss_goc_doi', models.DateField(blank=True, default='', null=True)),
                ('gmdss_goc_doe', models.DateField(blank=True, default='', null=True)),
                ('gmdss_goc_poi', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('gmdss_goc_authority', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('gmdss_endor_certificate_no', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('gmdss_endor_doi', models.DateField(blank=True, default='', null=True)),
                ('gmdss_endor_doe', models.DateField(blank=True, default='', null=True)),
                ('gmdss_endor_poi', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('gmdss_endor_authority', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('rau_certificate_no', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('rau_doi', models.DateField(blank=True, default='', null=True)),
                ('rau_doe', models.DateField(blank=True, default='', null=True)),
                ('rau_poi', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('rau_authority', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('ransco_certificate_no', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('ransco_doi', models.DateField(blank=True, default='', null=True)),
                ('ransco_doe', models.DateField(blank=True, default='', null=True)),
                ('ransco_poi', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('ransco_authority', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('sms_certificate_no', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('sms_doi', models.DateField(blank=True, default='', null=True)),
                ('sms_doe', models.DateField(blank=True, default='', null=True)),
                ('sms_poi', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('sms_authority', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('indos_certificate_no', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('indos_doi', models.DateField(blank=True, default='', null=True)),
                ('indos_doe', models.DateField(blank=True, default='', null=True)),
                ('indos_poi', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('indos_authority', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('simulator_certificate_no', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('simulator_doi', models.DateField(blank=True, default='', null=True)),
                ('simulator_doe', models.DateField(blank=True, default='', null=True)),
                ('simulator_poi', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('simulator_authority', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('btm_certificate_no', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('btm_doi', models.DateField(blank=True, default='', null=True)),
                ('btm_doe', models.DateField(blank=True, default='', null=True)),
                ('btm_poi', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('btm_authority', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('marpol_certificate_no', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('marpol_doi', models.DateField(blank=True, default='', null=True)),
                ('marpol_doe', models.DateField(blank=True, default='', null=True)),
                ('marpol_poi', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('marpol_authority', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('ecdis_ger_certificate_no', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('ecdis_ger_doi', models.DateField(blank=True, default='', null=True)),
                ('ecdis_ger_doe', models.DateField(blank=True, default='', null=True)),
                ('ecdis_ger_poi', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('ecdis_ger_authority', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('ecdis_specific_certificate_no', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('ecdis_specific_doi', models.DateField(blank=True, default='', null=True)),
                ('ecdis_specific_doe', models.DateField(blank=True, default='', null=True)),
                ('ecdis_specific_poi', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('ecdis_specific_authority', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('raai_certificate_no', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('raai_doi', models.DateField(blank=True, default='', null=True)),
                ('raai_doe', models.DateField(blank=True, default='', null=True)),
                ('raai_poi', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('raai_authority', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('brm_certificate_no', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('brm_doi', models.DateField(blank=True, default='', null=True)),
                ('brm_doe', models.DateField(blank=True, default='', null=True)),
                ('brm_poi', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('brm_authority', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('bwm_certificate_no', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('bwm_doi', models.DateField(blank=True, default='', null=True)),
                ('bwm_doe', models.DateField(blank=True, default='', null=True)),
                ('bwm_poi', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('bwm_authority', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('lvhsc_certificate_no', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('lvhsc_doi', models.DateField(blank=True, default='', null=True)),
                ('lvhsc_doe', models.DateField(blank=True, default='', null=True)),
                ('lvhsc_poi', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('lvhsc_authority', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('tasco_certificate_no', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('tasco_doi', models.DateField(blank=True, default='', null=True)),
                ('tasco_doe', models.DateField(blank=True, default='', null=True)),
                ('tasco_poi', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('tasco_authority', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('chemco_certificate_no', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('chemco_doi', models.DateField(blank=True, default='', null=True)),
                ('chemco_doe', models.DateField(blank=True, default='', null=True)),
                ('chemco_poi', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('chemco_authority', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('gasco_certificate_no', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('gasco_doi', models.DateField(blank=True, default='', null=True)),
                ('gasco_doe', models.DateField(blank=True, default='', null=True)),
                ('gasco_poi', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('gasco_authority', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('dce_petro_certificate_no', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('dce_petro_doi', models.DateField(blank=True, default='', null=True)),
                ('dce_petro_doe', models.DateField(blank=True, default='', null=True)),
                ('dce_petro_poi', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('dce_petro_authority', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('dce_chem_certificate_no', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('dce_chem_doi', models.DateField(blank=True, default='', null=True)),
                ('dce_chem_doe', models.DateField(blank=True, default='', null=True)),
                ('dce_chem_poi', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('dce_chem_authority', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('dce_gas_certificate_no', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('dce_gas_doi', models.DateField(blank=True, default='', null=True)),
                ('dce_gas_doe', models.DateField(blank=True, default='', null=True)),
                ('dce_gas_poi', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('dce_gas_authority', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('lcab_certificate_no', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('lcab_doi', models.DateField(blank=True, default='', null=True)),
                ('lcab_doe', models.DateField(blank=True, default='', null=True)),
                ('lcab_poi', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('lcab_authority', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('me_certificate_no', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('me_doi', models.DateField(blank=True, default='', null=True)),
                ('me_doe', models.DateField(blank=True, default='', null=True)),
                ('me_poi', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('me_authority', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('sham_certificate_no', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('sham_doi', models.DateField(blank=True, default='', null=True)),
                ('sham_doe', models.DateField(blank=True, default='', null=True)),
                ('sham_poi', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('sham_authority', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.profiledetails')),
            ],
        ),
        migrations.CreateModel(
            name='SEA_Exp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employer', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('rpsl', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('vessel_name', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('steam_motor', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('dwt_grt', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('rank', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('engine', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('bhp', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('engin_room', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('date_from', models.DateField(blank=True, default='', null=True)),
                ('date_to', models.DateField(blank=True, default='', null=True)),
                ('total', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profiledetails')),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('company', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('contact', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profiledetails')),
            ],
        ),
        migrations.CreateModel(
            name='Reason_for_app',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('present_emp', models.TextField(blank=True, default='', null=True)),
                ('support_application', models.TextField(blank=True, default='', null=True)),
                ('reference', models.CharField(blank=True, default='', max_length=5, null=True)),
                ('contact_details', models.TextField(blank=True, default='', null=True)),
                ('attend_interview', models.TextField(blank=True, default='', null=True)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.profiledetails')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('weight', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('BMI', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('color_of_eye', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('color_of_hair', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('major_illness', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('major_illness_res', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('defect_in_hearing', models.CharField(blank=True, default='', max_length=5, null=True)),
                ('defect_in_vision', models.CharField(blank=True, default='', max_length=5, null=True)),
                ('defect_in_speech', models.CharField(blank=True, default='', max_length=5, null=True)),
                ('affected_climate', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('state', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.profiledetails')),
            ],
        ),
        migrations.CreateModel(
            name='PassportDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pass_no', models.CharField(blank=True, max_length=50, null=True)),
                ('pass_poi', models.CharField(blank=True, max_length=200, null=True)),
                ('pass_doi', models.DateField(blank=True, default='', null=True)),
                ('pass_doe', models.DateField(blank=True, default='', null=True)),
                ('visa_no', models.CharField(blank=True, max_length=50, null=True)),
                ('visa_poi', models.CharField(blank=True, max_length=200, null=True)),
                ('visa_doi', models.DateField(blank=True, default='', null=True)),
                ('visa_doe', models.DateField(blank=True, default='', null=True)),
                ('yellow_fever_no', models.CharField(blank=True, max_length=50, null=True)),
                ('yellow_fever_poi', models.CharField(blank=True, max_length=200, null=True)),
                ('yellow_fever_doi', models.DateField(blank=True, default='', null=True)),
                ('yellow_fever_doe', models.DateField(blank=True, default='', null=True)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.profiledetails')),
            ],
        ),
        migrations.CreateModel(
            name='OSS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employer', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('title', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('workshop', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('major_machine', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('supervised', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('size', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('period_frm', models.DateField(blank=True, default='', null=True)),
                ('period_to', models.DateField(blank=True, default='', null=True)),
                ('other_info', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profiledetails')),
            ],
        ),
        migrations.CreateModel(
            name='NKD_de',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_rela', models.CharField(blank=True, max_length=500, null=True)),
                ('relation', models.CharField(blank=True, max_length=50, null=True)),
                ('add_nkd', models.TextField(blank=True, null=True)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.profiledetails')),
            ],
        ),
        migrations.CreateModel(
            name='NKD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nkd_name_no', models.CharField(blank=True, default='NA', max_length=500, null=True)),
                ('nkd_rela_no', models.CharField(blank=True, default='NA', max_length=500, null=True)),
                ('nkd_dob_no', models.DateField(blank=True, default='', null=True)),
                ('nkd_ppno_no', models.CharField(blank=True, default='NA', max_length=500, null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profiledetails')),
            ],
        ),
        migrations.CreateModel(
            name='LDW',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ldw', models.CharField(blank=True, default='', max_length=5, null=True)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.profiledetails')),
            ],
        ),
        migrations.CreateModel(
            name='LCOC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ind_grade', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('ind_no', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('ind_doi', models.DateField(blank=True, default='', null=True)),
                ('ind_doe', models.DateField(blank=True, default='', null=True)),
                ('ind_dr', models.DateField(blank=True, default='', null=True)),
                ('ind_stcw', models.CharField(blank=True, default='', max_length=5, null=True)),
                ('uk_grade', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('uk_no', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('uk_doi', models.DateField(blank=True, default='', null=True)),
                ('uk_doe', models.DateField(blank=True, default='', null=True)),
                ('uk_dr', models.DateField(blank=True, default='', null=True)),
                ('uk_stcw', models.CharField(blank=True, default='', max_length=5, null=True)),
                ('aus_grade', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('aus_no', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('aus_doi', models.DateField(blank=True, default='', null=True)),
                ('aus_doe', models.DateField(blank=True, default='', null=True)),
                ('aus_dr', models.DateField(blank=True, default='', null=True)),
                ('aus_stcw', models.CharField(blank=True, default='', max_length=5, null=True)),
                ('singa_grade', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('singa_no', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('singa_doi', models.DateField(blank=True, default='', null=True)),
                ('singa_doe', models.DateField(blank=True, default='', null=True)),
                ('singa_dr', models.DateField(blank=True, default='', null=True)),
                ('singa_stcw', models.CharField(blank=True, default='', max_length=5, null=True)),
                ('panama_grade', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('panama_no', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('panama_doi', models.DateField(blank=True, default='', null=True)),
                ('panama_doe', models.DateField(blank=True, default='', null=True)),
                ('panama_dr', models.DateField(blank=True, default='', null=True)),
                ('panama_stcw', models.CharField(blank=True, default='', max_length=5, null=True)),
                ('other_grade', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('other_no', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('other_doi', models.DateField(blank=True, default='', null=True)),
                ('other_doe', models.DateField(blank=True, default='', null=True)),
                ('other_dr', models.DateField(blank=True, default='', null=True)),
                ('other_stcw', models.CharField(blank=True, default='', max_length=5, null=True)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.profiledetails')),
            ],
        ),
        migrations.CreateModel(
            name='Declaration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default='', null=True)),
                ('photo', models.ImageField(blank=True, default='', null=True, upload_to='photo/')),
                ('signature', models.ImageField(blank=True, default='', null=True, upload_to='signatures/')),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.profiledetails')),
            ],
        ),
        migrations.CreateModel(
            name='CDCSB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ind_no', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('ind_poi', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('ind_doi', models.DateField(blank=True, default='', null=True)),
                ('ind_doe', models.DateField(blank=True, default='', null=True)),
                ('panama_no', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('panama_poi', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('panama_doi', models.DateField(blank=True, default='', null=True)),
                ('panama_doe', models.DateField(blank=True, default='', null=True)),
                ('others_no', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('others_poi', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('others_doi', models.DateField(blank=True, default='', null=True)),
                ('others_doe', models.DateField(blank=True, default='', null=True)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.profiledetails')),
            ],
        ),
        migrations.CreateModel(
            name='ATOC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency', models.CharField(blank=True, max_length=50, null=True)),
                ('rank', models.CharField(blank=True, max_length=50, null=True)),
                ('ms_rank', models.CharField(blank=True, max_length=50, null=True)),
                ('doa', models.DateField(blank=True, default='', null=True)),
                ('doa2', models.DateField(blank=True, default='', null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profiledetails')),
            ],
        ),
        migrations.CreateModel(
            name='Additional_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applied', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('aicoba', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('criminal_offence', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('criminal_offence_details', models.TextField(blank=True, default='', null=True)),
                ('ship_incident', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('ship_incident_details', models.TextField(blank=True, default='', null=True)),
                ('suspended', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('suspended_from', models.DateField(blank=True, default='', null=True)),
                ('suspended_to', models.DateField(blank=True, default='', null=True)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.profiledetails')),
            ],
        ),
        migrations.CreateModel(
            name='AcademicDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elem_noi', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('elem_grade', models.CharField(blank=True, default='', max_length=5, null=True)),
                ('elem_from_yr', models.CharField(blank=True, default='', max_length=4, null=True)),
                ('elem_to_yr', models.CharField(blank=True, default='', max_length=4, null=True)),
                ('secd_noi', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('secd_grade', models.CharField(blank=True, default='', max_length=5, null=True)),
                ('secd_from_yr', models.CharField(blank=True, default='', max_length=4, null=True)),
                ('secd_to_yr', models.CharField(blank=True, default='', max_length=4, null=True)),
                ('univ_noi', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('univ_grade', models.CharField(blank=True, default='', max_length=5, null=True)),
                ('univ_from_yr', models.CharField(blank=True, default='', max_length=4, null=True)),
                ('univ_to_yr', models.CharField(blank=True, default='', max_length=4, null=True)),
                ('profe_noi', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('profe_grade', models.CharField(blank=True, default='', max_length=5, null=True)),
                ('profe_from_yr', models.CharField(blank=True, default='', max_length=4, null=True)),
                ('profe_to_yr', models.CharField(blank=True, default='', max_length=4, null=True)),
                ('addition_skills', models.CharField(blank=True, max_length=1000, null=True)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.profiledetails')),
            ],
        ),
        migrations.CreateModel(
            name='AboutUS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comapany', models.BooleanField(default=False)),
                ('marin_club', models.BooleanField(default=False)),
                ('marin_magzin', models.BooleanField(default=False)),
                ('newspaper', models.BooleanField(default=False)),
                ('friend', models.BooleanField(default=False)),
                ('mail', models.BooleanField(default=False)),
                ('other', models.BooleanField(default=False)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.profiledetails')),
            ],
        ),
    ]
