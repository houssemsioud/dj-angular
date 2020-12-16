from django.contrib import admin
from .models import ExampleModel
from .models import Forme_produit
from .models import Presentation
from .models import Type_composant
from .models import Composant
from .models import Type_parametre
from .models import Unite
from .models import Parametre
from .models import Equipement
from .models import Produit_fini
from .models import Exercice
from .models import Type_anomalie
from .models import Capa
from .models import Lot


# Register your models here.
admin.site.register(ExampleModel)
admin.site.register(Forme_produit)
admin.site.register(Presentation)
admin.site.register(Type_composant)
admin.site.register(Composant)
admin.site.register(Type_parametre)
admin.site.register(Unite)
admin.site.register(Parametre)
admin.site.register(Equipement)
admin.site.register(Produit_fini)
admin.site.register(Exercice)
admin.site.register(Type_anomalie)
admin.site.register(Capa)
admin.site.register(Lot)