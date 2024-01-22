from django.db import models
class circus(models.Model):
    ID = models.BigAutoField(primary_key=True,verbose_name="id")
    FullName = models.CharField(max_length=100 ,verbose_name="name")
    IsAlive = models.BooleanField(default=False,verbose_name="is alive")
    HowManyDalghakIsTrained = models.IntegerField(verbose_name = "HowManyDalghakIsTrained")
    class Meta:
        verbose_name_plural = "dalghak haha"
    def __str__(self) :
        return f"{self.ID} , {self.FullName}"
class Genres(models.Model):
    ID = models.BigAutoField(primary_key=True,verbose_name="id")
    GenName = models.CharField(max_length=100,verbose_name="gener")

class dalghak(models.Model):
    IsAlive = models.ForeignKey(circus,on_delete =models.CASCADE)
    ID = models.BigAutoField(primary_key=True,verbose_name="id")
    Name = models.CharField(max_length=100,verbose_name="name")
    DalghakSalary = models.SmallIntegerField(verbose_name = "Dalghak salary")
    WhenBecomeDalghak = models.DateField(max_length=100,verbose_name="id")
