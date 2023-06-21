from django.db.models import TextChoices

class GeneroChoi(TextChoices):
    MULHER_TRANS = 'mt', 'Mulher Trans'
    MULHER_CIS = 'mc', 'Mulher Cis'
    HOMEM_TRANS = 'ht', 'Homem Trans'
    HOMEM_CIS = 'hc', 'Homem Cis'
    TRAVESTI = 'tr' , 'Travesti'
    NAO_BINARIO = 'nb', 'Não Binário'
    OUTROS = 'ot', 'Outros'