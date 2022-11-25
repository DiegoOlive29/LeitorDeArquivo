from django.db import models

# Create your models here.
class TypeOps(models.TextChoices):
       DEBITO = 1
       BOLETO = 2
       FINACIAMENTO = 3
       CREDITO = 4
       RECEBIMENTO_EMPRESTIMO = 5
       VENDAS = 6
       RECEBIMENTO_TED = 7
       RECEBIMENTO_DOC = 8
       ALUGUEL = 9
        

class Dado(models.Model):
        typeOp = models.CharField(choices=TypeOps.choices, max_length=22)
        date = models.DateField(null=True)
        value = models.CharField(max_length=10)
        cpf = models.CharField(max_length=11)
        card = models.CharField(max_length=12)
        hour = models.CharField(max_length=6)
        store_owner = models.CharField(max_length=14)
        store_name = models.CharField(max_length=19)
