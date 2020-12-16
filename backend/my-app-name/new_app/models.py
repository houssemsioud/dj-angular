from django.db import models
from django.urls import reverse  # To generate URLS by reversing URL patterns
import uuid  # Required for unique book instances
from django import forms
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext as _
from django.contrib.auth.models import User  # Required to assign User as a borrower


PROTOCOLES = [
    ('fabrication', 'Fabrication'),
    ('compression', 'Compression'),
    ('mise en gélules', 'Mise en gélules'),
    ('pelliculage ', 'Pelliculage'),
    ('conditionnement primaire ', 'Conditionnement primaire'),
    ('conditionnement secondaire', 'Conditionnement secondaire'),
    ('rendement de la fabrication', 'Rendement de la fabrication'),
]
RENDEMENTS = [
    ('rendement de la fabrication', 'Rendement de la fabrication'),
    ('rendement de la compression', 'Rendement de la compression'),
    ('rendement de mise en gélules', 'Rendement de mise en gélules'),
    ('rendement de pelliculage ', 'Rendement de pelliculage'),
    ('rendement de conditionnement primaire ', 'Rendement de conditionnement primaire'),
    ('rendement de conditionnement secondaire', 'Rendement de conditionnement secondaire'),
]

# Create your models here.
class ExampleModel(models.Model):
	firstname    = models.CharField(max_length=200)
	lastname     = models.CharField(max_length=200)

class Forme_produit(models.Model):
    """Model representing a book genre (e.g. Science Fiction, Non Fiction)."""
    name = models.CharField(
        max_length=200,
        help_text="Entrer une forme de produit (exemple: Liquide ...)"
        )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name

class Presentation(models.Model):
    """Model representing a book genre (e.g. Science Fiction, Non Fiction)."""
    name = models.CharField(
        max_length=200,
        help_text="Entrer la présentation de produit (exemple: Bte de 12 ...)"
        )
    n_amm = models.CharField(max_length=100)

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name

class Type_composant(models.Model):  
    """Model representing an author."""
    name = models.CharField(max_length=100, help_text= "Matière première, Article de conditionnement primaire...")

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Composant(models.Model):  
    """Model representing an author."""
    code_composant = models.CharField(max_length=100)
    designation_composant = models.CharField(max_length=100)
    principe_actif= models.BooleanField(default=False)
    dosage_maximum = models.DecimalField(max_digits=19, decimal_places=10)
    dosage_minimum = models.DecimalField(max_digits=19, decimal_places=10)
    type_composant = models.ForeignKey('Type_composant', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        """String for representing the Model object."""
        return self.code_composant
class Type_parametre(models.Model):  
    """Model representing an author."""
    name = models.CharField(max_length=100, help_text="Production - Mélange, Production - Compression...")

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Unite(models.Model):  
    """Model representing an author."""
    name = models.CharField(max_length=100)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Parametre(models.Model):  
    """Model representing an author."""
    designation_parametre = models.CharField(max_length=100)
    type_parametre = models.ForeignKey('Type_parametre', on_delete=models.SET_NULL, null=True)
    unite = models.ForeignKey('Unite', on_delete=models.SET_NULL, null=True)
    valeur_maximum = models.DecimalField(max_digits=19, decimal_places=10)
    valeaur_minimum = models.DecimalField(max_digits=19, decimal_places=10)

    def __str__(self):
        """String for representing the Model object."""
        return self.designation_parametre

class Equipement(models.Model):  
    """Model representing an author."""
    designation_equipement = models.CharField(max_length=100)
    reference = models.CharField(max_length=100)
    reference_rapport_qi = models.CharField(max_length=100)
    reference_rapport_qo = models.CharField(max_length=100)
    reference_rapport_qp = models.CharField(max_length=100)
    date_qi = models.DateField(null=True, blank=True)
    date_qo = models.DateField(null=True, blank=True)
    date_qp = models.DateField(null=True, blank=True)
    date_prochaine_qp = models.DateField(null=True, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.designation_equipement

class Produit_fini(models.Model):  
    """Model representing an author."""
    code_produit = models.CharField(max_length=100)
    designation_produit = models.CharField(max_length=100)
    forme_produit = models.ForeignKey(Forme_produit, on_delete=models.SET_NULL, null=True, blank=True)
    dosage = models.PositiveIntegerField()
    presentation = models.ForeignKey(Presentation, on_delete=models.SET_NULL, null=True, blank=True)
    composant = models.ManyToManyField(Composant)
    parametre = models.ManyToManyField(Parametre)
    equipement = models.ManyToManyField(Equipement)
    rendement_global_minimal_acceptable = models.PositiveIntegerField()
    protocoles = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=PROTOCOLES,
    )
    valeur_max_rdt_fab_acc = models.DecimalField(max_digits=19, decimal_places=10)
    valeur_min_rdt_fab_acc = models.DecimalField(max_digits=19, decimal_places=10)
    valeur_max_rdt_comp_acc = models.DecimalField(max_digits=19, decimal_places=10)
    valeur_min_rdt_comp_acc = models.DecimalField(max_digits=19, decimal_places=10)
    valeur_max_rdt_meg_acc = models.DecimalField(max_digits=19, decimal_places=10)
    valeur_min_rdt_meg_acc = models.DecimalField(max_digits=19, decimal_places=10)
    valeur_max_rdt_pel_acc = models.DecimalField(max_digits=19, decimal_places=10)
    valeur_min_rdt_pel_acc = models.DecimalField(max_digits=19, decimal_places=10)
    valeur_max_rdt_cond1_acc = models.DecimalField(max_digits=19, decimal_places=10)
    valeur_min_rdt_cond1_acc = models.DecimalField(max_digits=19, decimal_places=10)
    valeur_max_rdt_cond2_acc = models.DecimalField(max_digits=19, decimal_places=10)
    valeur_min_rdt_cond2_acc = models.DecimalField(max_digits=19, decimal_places=10)

    def __str__(self):
        """String for representing the Model object."""
        return self.designation_produit

    
def current_year():
    return date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)    

def year_choices():
    return [(r,r) for r in range(1984, date.today().year+1)]

class Exercice(models.Model):
    year = models.IntegerField(_('year'), default= 2020, validators=[MinValueValidator(1984), max_value_current_year])
    def __str__(self):
        """String for representing the Model object."""
        return str(self.year)

class Type_anomalie(models.Model):  
    """Model representing an author."""
    name = models.CharField(max_length=100)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Capa(models.Model):  
    """Model representing an author."""
    name = models.CharField(max_length=100)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Lot(models.Model):      
    """Model representing an author."""
    produit = models.ForeignKey('Produit_fini', on_delete=models.SET_NULL, null=True)
    exercice = models.ForeignKey('Exercice', on_delete=models.SET_NULL, null=True)
    numero_lot = models.CharField(max_length=100)
    date_fabrication = models.DateField(null=True, blank=True)
    date_peremption = models.DateField(null=True, blank=True)
    taille_reelle_lot = models.DecimalField(max_digits=8, decimal_places=0)
    protocole_validation_process = models.CharField(max_length=100)
    protocole_validation_analytique = models.CharField(max_length=100)
    reference_technique_controle = models.CharField(max_length=100)
    valeur_prod_melange = models.DecimalField(max_digits=19, decimal_places=10)
    valeur_prod_compression= models.DecimalField(max_digits=19, decimal_places=10)
    valeur_prod_pelliculage = models.DecimalField(max_digits=19, decimal_places=10)
    valeur_prod_cond1 = models.DecimalField(max_digits=19, decimal_places=10)
    valeur_prod_cond2 = models.DecimalField(max_digits=19, decimal_places=10)
    valeur_cq_ph = models.DecimalField(max_digits=19, decimal_places=10)
    valeur_cq_micro_bio = models.DecimalField(max_digits=19, decimal_places=10)
    valeur_stabilite_ph = models.DecimalField(max_digits=19, decimal_places=10)
    valeur_stabilite_micro_bio = models.DecimalField(max_digits=19, decimal_places=10)
    echeance_stabilite = models.DecimalField(max_digits=8, decimal_places=0)
    valeur_rdt_fab = models.DecimalField(max_digits=19, decimal_places=10)
    valeur_rdt_comp= models.DecimalField(max_digits=19, decimal_places=10)
    valeur_rdt_meg = models.DecimalField(max_digits=19, decimal_places=10)
    valeur_rdt_pel = models.DecimalField(max_digits=19, decimal_places=10)
    valeur_rdt_cond1 = models.DecimalField(max_digits=19, decimal_places=10)
    valeur_rdt_cond2 = models.DecimalField(max_digits=19, decimal_places=10)
    type_anomalie = models.ForeignKey('Type_anomalie', on_delete=models.SET_NULL, null=True)
    capa = models.ForeignKey('Capa', on_delete=models.SET_NULL, null=True)
    anomalie_cloturee= models.BooleanField(default=False)
    num_lot_composant = models.CharField(max_length=100)
    fabricant_composant = models.CharField(max_length=100)
    dosage_pa = models.DecimalField(max_digits=19, decimal_places=10)

    def __str__(self):
        """String for representing the Model object."""
        return self.year