from django.db import models
from django.core.validators import RegexValidator
class people(models.Model):
    type_choices=((0,'جندي'),(1,'صف ضابط'))
    attend=((1,'متواجد'),(2,'اجازة'),(3,'راحة'),(4,'مأمورية'),(5,'مستشفي'),(6,'غياب'))
    sectors=((1,'تخطيط'),(2,'ادارة عسكرية'),(3,'شئون قانونية'),(4,'نمظيم و تسليح'),(5,'افراد'),(6,'ادارة محلية'),(7,'سجلات'),(8,'تعبئة'))
    type=models.IntegerField(choices=type_choices,default=4)
    name=models.CharField(max_length=50)
    attendance=models.IntegerField(choices=attend,default=1)
    sector=models.IntegerField(choices=sectors,default =0)
    mil_numb=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    phone_number=models.CharField(max_length=11)
    def __str__(self):
     return self.name
