from django import forms
from coordinaAsignaturas.models import Asignatura
 
class FormularioAsignatura(forms.ModelForm):
    lun = forms.BooleanField()
    lun_inicio = forms.ChoiceField(choices=[(n, n) for n in range(1, 11)])
    lun_fin = forms.ChoiceField(choices=[(n, n) for n in range(1, 11)])
    mar = forms.BooleanField()
    mar_inicio = forms.ChoiceField(choices=[(n, n) for n in range(1, 11)])
    mar_fin = forms.ChoiceField(choices=[(n, n) for n in range(1, 11)])
    mie = forms.BooleanField()
    mie_inicio = forms.ChoiceField(choices=[(n, n) for n in range(1, 11)])
    mie_fin = forms.ChoiceField(choices=[(n, n) for n in range(1, 11)])
    jue = forms.BooleanField()
    jue_inicio = forms.ChoiceField(choices=[(n, n) for n in range(1, 11)])
    jue_fin = forms.ChoiceField(choices=[(n, n) for n in range(1, 11)])
    vie = forms.BooleanField()
    vie_inicio = forms.ChoiceField(choices=[(n, n) for n in range(1, 11)])
    vie_fin = forms.ChoiceField(choices=[(n, n) for n in range(1, 11)])
    
    class Meta:
        model = Asignatura
        exclude = ['cod_Dpto','dia','horas']
        labels = {'codAsig' : 'Codigo de asignatura',
                  'creditos' : 'Numero de creditos',
                  'nomAsig' : 'Nombre',
                  'progAsig' : 'Programa',
                  'prof' : 'Profesor'}
   
    # Haciendole override al metodo is_valid
    def is_valid(self):
        # Se llama primero al metodo de la superclase
        valid = super(FormularioAsignatura,self).is_valid()
       
        # Si el metodo de la super clase retorna False, se retorna False
        if not(valid) :
            return valid
       
        # Comprobando que no haya una asignatura con igual codigo
        try:
            Asignatura.objects.get(codAsig=self.cleaned_data['codAsig'])
            return False
        except Asignatura.DoesNotExist :
            pass
       
        # Comprobando que no haya una asignatura con igual nombre
        try:
            Asignatura.objects.get(nomAsig=self.cleaned_data['nomAsig'])
            return False
        except Asignatura.DoesNotExist :
            pass
       
        return True