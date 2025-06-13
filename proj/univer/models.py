from django.db import models

class students(models.Model):
    st_name = models.CharField(max_length = 255, null=False)
    st_surname = models.CharField(max_length = 255, null=False)
    st_group = models.CharField(max_length=255, null=True)
    st_course = models.IntegerField()   
    teacher = models.ForeignKey('Teacher', on_delete=models.PROTECT)



    def __str__(self):
        return self.st_name + " " + self.st_surname + "("+ self.st_group + ")" + " " + str(self.st_course) + " курс"

class Teacher(models.Model):
    t_name = models.CharField(max_length=255)

    def __str__(self):
        return self.t_name
    
class subject(models.Model):
    subject_name = models.CharField(max_length=255, null=False)
    st_grade = models.ForeignKey('grades', on_delete=models.PROTECT)

    def __str__(self):
        return self.subject_name
    
class grades(models.Model):
    grade = models.CharField(max_length = 255, null= False)

    def __str__(self):
        return self.grade