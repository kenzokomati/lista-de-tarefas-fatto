from django import forms
from .models import Task

# Create Add Record Form
class AddTaskForm(forms.ModelForm):  
  task_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Nome da tarefa", "class":"form-control"}), label="Tarefa")
  task_due_date = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={"type":"date", "class":"form-control"}), label="Data Limite")
  task_cost = forms.DecimalField(max_digits=10, decimal_places=2, required=True, widget=forms.widgets.NumberInput(attrs={"placeholder":"100,00", "step":"0.01", "class":"form-control"}), label="Custo (R$)")
  
  class Meta:
    model = Task
    fields = ("task_name", "task_cost", "task_due_date")
  
  def clean_task_name(self):
    task_name = self.cleaned_data.get('task_name')

    duplicates = Task.objects.filter(task_name__iexact=task_name)

    if self.instance.pk:
      duplicates = duplicates.exclude(pk=self.instance.pk)

    if duplicates.exists():
      raise forms.ValidationError(
        "Já existe uma tarefa com esse nome. Por favor, escolha outro nome."
      )
    
    return task_name