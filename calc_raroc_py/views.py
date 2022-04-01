from django.shortcuts import render
from .models import calculaRaroc
import pandas as pd


def index(request):
    calcraroc_df = pd.DataFrame(calculaRaroc.objects.all().values())
    context = {
        'calcraroc': calcraroc_df.to_html,
    }
    return render(request, 'index.html', context)

