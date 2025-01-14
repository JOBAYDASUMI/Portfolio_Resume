from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    
    USER=[
        ('admin','Admin'),
        ('viewer','Viewer'),
    ]
    usertype=models.CharField(max_length=100,null=True,choices=USER)
    
    def __str__(self):
        return f"{self.username}-{self.first_name}-{self.last_name}" 
    
class ResumeModel(models.Model):
    
    user=models.OneToOneField(CustomUser,null=True,on_delete=models.CASCADE)
    contact_No=models.CharField(max_length=100,null=True)
    Designation=models.CharField(max_length=100,null=True)
    Profile_Pic=models.ImageField(upload_to="Media/Profile_Pic",null=True)
    Carrer_Summary=models.CharField(max_length=100,null=True)
    Age=models.PositiveIntegerField(null=True)
    Gender=models.CharField(max_length=100,null=True)
    
    def __str__(self) -> str:
        return self.user.username+ " "+ self.Designation
   
class LanguageModel(models.Model):
    
    Proficiency_Level_Choices=[
        ('beginner','Beginner'),
        ('intermediate','Intermediate'),
        ('expert','Expert'),
    ]

    user=models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE)
    Language_Name=models.CharField(max_length=100,null=True)
    Proficiency_Level=models.CharField(choices=Proficiency_Level_Choices,max_length=100,null=True)
    
    
    class Meta:
        unique_together=['user','Language_Name']
    
    def __str__(self) -> str:
        return self.user.username+ " "+ self.Language_Name
    
class IntermediateLanguageModel(models.Model):
    
    Language_Name=models.CharField(max_length=100,null=True)
    
    def __str__(self) -> str:
        return self.Language_Name
    

class SkillModel(models.Model):
    
    
    Skill_Level_Choices=[
        ('beginner','Beginner'),
        ('intermediate','Intermediate'),
        ('expert','Expert'),
    ]
    user=models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE)
    Skill_Name=models.CharField(max_length=100,null=True)
    Skill_Level=models.CharField(choices=Skill_Level_Choices,max_length=100,null=True)
    
    class Meta:
        unique_together=['user','Skill_Name']
    
    def __str__(self) -> str:
        return self.user.username+ " "+ self.Skill_Name
    
class IntermediateSkillModel(models.Model):
    
    My_Skill_Name=models.CharField(max_length=100,null=True)
    
    def __str__(self) -> str:
        return self.My_Skill_Name
    
    
class EducationModel(models.Model):
    
    
    Education_Choices=[
        ('ssc','SSC'),
        ('hsc','HSC'),
        ('honurs','Honurs'),
    ]
    user=models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE)
    Education_Name=models.CharField(max_length=100,null=True)
    Education_Choices=models.CharField(choices=Education_Choices,max_length=100,null=True)
    
    class Meta:
        unique_together=['user','Education_Name']
    
    def __str__(self) -> str:
        return self.user.username+ " "+ self.Education_Name
    
class IntermediateEducationModel(models.Model):
    
    Education_Name=models.CharField(max_length=100,null=True)
    
    def __str__(self) -> str:
        return self.Education_Name
    
    
class InterestModel(models.Model):
    
    
    Interest_Choices=[
        ('sports','Sports'),
        ('music','Music'),
        ('reading','Reading'),
    ]
    user=models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE)
    Interest_Name=models.CharField(max_length=100,null=True)
    Interest_Choices=models.CharField(choices=Interest_Choices,max_length=100,null=True)
    
    class Meta:
        unique_together=['user','Interest_Name']
    
    def __str__(self) -> str:
        return self.user.username+ " "+ self.Interest_Name
    
class IntermediateInterestModel(models.Model):
    
    Interest_Name=models.CharField(max_length=100,null=True)
    
    def __str__(self) -> str:
        return self.Interest_Name
    
    
class ExperienceModel(models.Model):
    
    
    Experience_level_Choices = [
        ('beginner','Beginner'),
        ('intermediate','Intermediate'),
        ('advanced','Advanced'),
        ('expert','Expert'),
    ]
    user=models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE)
    Experience_Name=models.CharField(max_length=100,null=True)
    Experience_Choices=models.CharField(choices=Experience_level_Choices,max_length=100,null=True)
    
    class Meta:
        unique_together=['user','Experience_Name']
    
    def __str__(self) -> str:
        return self.user.username+ " "+ self.Experience_Name
    
class IntermediateExperienceModel(models.Model):
    
    Experience_Name=models.CharField(max_length=100,null=True)
    
    def __str__(self) -> str:
        return self.Experience_Name
    
