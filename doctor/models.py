from django.db import models

import uuid

# import django user model
from hospital.models import Hospital_Information, User, Patient
from hospital_admin.models import hospital_department, specialization, service

# # Create your models here.

"""
null=True --> don't require a value when inserting into the database
blank=True --> allow blank value when submitting a form
auto_now_add --> automatically set the value to the current date and time
unique=True --> prevent duplicate values
primary_key=True --> set this field as the primary key
editable=False --> prevent the user from editing this field

django field types --> google it  # every field types has field options
Django automatically creates id field for each model class which will be a PK # primary_key=True --> if u want to set manual
"""
# Create your models here.


class Doctor_Information(models.Model):
    DOCTOR_TYPE = (
        ('Cardiologists', 'Cardiologists'),
        ('Neurologists', 'Neurologists'),
        ('Pediatricians', 'Pediatricians'),
        ('Physiatrists', 'Physiatrists'),
        ('Dermatologists', 'Dermatologists'),
    )
    
    doctor_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='profile')
    name = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    department = models.CharField(max_length=200, choices=DOCTOR_TYPE, null=True, blank=True)
    department_name = models.ForeignKey(hospital_department, on_delete=models.CASCADE, null=True, blank=True)
    specialization = models.ForeignKey(specialization, on_delete=models.CASCADE, null=True, blank=True)
    # service = models.ForeignKey(service, on_delete=models.CASCADE, null=True, blank=True)

    featured_image = models.ImageField(upload_to='doctors/', default='doctors/user-default.png', null=True, blank=True)
    certificate_image = models.ImageField(upload_to='doctors_certificate/', default='doctors_certificate/default.png', null=True, blank=True)

    email = models.EmailField(max_length=200, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    visiting_hour = models.CharField(max_length=200, null=True, blank=True)
    consultation_fee = models.IntegerField(null=True, blank=True)
    report_fee = models.IntegerField(null=True, blank=True)
    #doctor_password = models.CharField(max_length=200, null=True, blank=True)
    dob = models.CharField(max_length=200, null=True, blank=True)
    
    # Education
    institute = models.CharField(max_length=200, null=True, blank=True)
    degree = models.CharField(max_length=200, null=True, blank=True)
    completion_year = models.CharField(max_length=200, null=True, blank=True)
    
    # work experience
    work_place = models.CharField(max_length=200, null=True, blank=True)
    designation = models.CharField(max_length=200, null=True, blank=True)
    start_year = models.CharField(max_length=200, null=True, blank=True)
    end_year = models.CharField(max_length=200, null=True, blank=True)
    
    # register_status = models.BooleanField(default=False) default='pending'
    register_status =  models.CharField(max_length=200, null=True, blank=True)
    
    # ForeignKey --> one to one relationship with Hospital_Information model.
    hospital_name = models.ForeignKey(Hospital_Information, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.user.username)



class Appointment(models.Model):
    # ('database value', 'display_name')
    APPOINTMENT_TYPE = (
        ('report', 'report'),
        ('checkup', 'checkup'),
    )
    APPOINTMENT_STATUS = (
        ('pending', 'pending'),
        ('confirmed', 'confirmed'),
        ('cancelled', 'cancelled'),
    )

    id = models.AutoField(primary_key=True)
    date = models.DateField(null=True, blank=True)
    time = models.CharField(max_length=200, null=True, blank=True)
    # time = models.DateField(auto_now_add=True)
    # date = models.TimeField(auto_now_add=True)
    doctor = models.ForeignKey(Doctor_Information, on_delete=models.CASCADE, null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    appointment_type = models.CharField(max_length=200, choices=APPOINTMENT_TYPE)
    appointment_status = models.CharField(max_length=200, choices=APPOINTMENT_STATUS)
    serial_number = models.CharField(max_length=200, null=True, blank=True)
    payment_status = models.CharField(max_length=200, null=True, blank=True, default='pending')
    transaction_id = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.patient.username)

class Education(models.Model):
    education_id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey(Doctor_Information, on_delete=models.CASCADE, null=True, blank=True)
    degree = models.CharField(max_length=200, null=True, blank=True)
    institute = models.CharField(max_length=200, null=True, blank=True)
    year_of_completion = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return str(self.doctor.name)
    
class Experience(models.Model):
    experience_id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey(Doctor_Information, on_delete=models.CASCADE, null=True, blank=True)
    work_place_name = models.CharField(max_length=200, null=True, blank=True)
    from_year = models.CharField(max_length=200, null=True, blank=True)
    to_year = models.CharField(max_length=200, null=True, blank=True)
    designation = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return str(self.doctor.name)


class Report(models.Model):

    report_id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey(Doctor_Information, on_delete=models.CASCADE, null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    specimen_id = models.CharField(max_length=200, null=True, blank=True)
    specimen_type = models.CharField(max_length=200, null=True, blank=True)
    collection_date = models.CharField(max_length=200, null=True, blank=True)
    receiving_date = models.CharField(max_length=200, null=True, blank=True)
    test_name = models.CharField(max_length=200, null=True, blank=True)
    result = models.CharField(max_length=200, null=True, blank=True)
    unit = models.CharField(max_length=200, null=True, blank=True)
    referred_value = models.CharField(max_length=200, null=True, blank=True)
    delivery_date = models.CharField(max_length=200, null=True, blank=True)
    other_information = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.patient.username)

class Specimen(models.Model):

    report = models.ForeignKey(Report, on_delete=models.CASCADE, null=True, blank=True)
    specimen_id = models.AutoField(primary_key=True)
    specimen_type = models.CharField(max_length=200, null=True, blank=True)
    collection_date = models.CharField(max_length=200, null=True, blank=True)
    receiving_date = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return str(self.report.report_id)

class Test(models.Model):

    report = models.ForeignKey(Report, on_delete=models.CASCADE, null=True, blank=True)
    test_id = models.AutoField(primary_key=True)
    test_name = models.CharField(max_length=200, null=True, blank=True)
    result = models.CharField(max_length=200, null=True, blank=True)
    unit = models.CharField(max_length=200, null=True, blank=True)
    referred_value = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return str(self.report.report_id)

        
class Prescription(models.Model):

    # medicine name, quantity, days, time, description, test, test_descrip
    prescription_id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey(Doctor_Information, on_delete=models.CASCADE, null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    
    medicine_name = models.CharField(max_length=200, null=True, blank=True)
    quantity = models.CharField(max_length=200, null=True, blank=True)
    days = models.CharField(max_length=200, null=True, blank=True)
    time = models.CharField(max_length=200, null=True, blank=True)
    medicine_description = models.TextField(null=True, blank=True)

    test_name = models.CharField(max_length=200, null=True, blank=True)
    test_description = models.TextField(null=True, blank=True)
    extra_information = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.doctor.username)
