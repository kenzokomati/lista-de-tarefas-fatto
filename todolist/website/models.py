from django.db import models

# Create your models here.
# Identificador da tarefa (chave primária)
# Nome da tarefa
# Custo (R$)
# Data limite
# Ordem de apresentação (campo numérico, não repetido, que servirá para ordenar os registros na tela)

class Task(models.Model):
  id = models.AutoField(primary_key=True)  
  task_name = models.CharField(max_length=100, unique=True)  
  task_cost = models.DecimalField(max_digits=10, decimal_places=2)  
  task_due_date = models.DateField()  
  view_order = models.PositiveIntegerField(db_index=True)
  
  class Meta:
    ordering = ["view_order"]

  def __str__(self):
    return (f"{self.view_order} {self.task_name}")