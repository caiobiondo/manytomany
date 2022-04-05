from django.shortcuts import render
from .models import calculaRaroc, Fluxo
import pandas as pd
#import numpy as np


def index(request):
    calcraroc_df = pd.DataFrame(calculaRaroc.objects.all().values())
    fluxo_df = pd.DataFrame(Fluxo.objects.all().values())
    calcraroc_df['percent'] = (calcraroc_df['raroc_ref'].sum()) * 100
    context = {
        'calcraroc': calcraroc_df.to_html,
        'fluxo': fluxo_df.to_html,
    }
    return render(request, 'index.html', context)

