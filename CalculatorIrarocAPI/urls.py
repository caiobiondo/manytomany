from django.urls import path

from .views import BofAPIView, CalculoAPIView, CalculoscombinadaAPIView, CboregracusteioAPIView, ComboloanAPIView, \
    DadoscalculadorapipelineAPIView, DgabaseoperacoesAPIView, DgaceadiarioAPIView, DgacurvasjurosAPIView, \
    DgagruposAPIView, DgamatrizmigracaoAPIView, DgamontecarloAPIView, DgaparametrosestrategiaportfolioAPIView, \
    DgapercentualfepfAPIView, DgarcpalfasbetasAPIView, DgatargetpaisAPIView, FprcnpjAPIView, GarantiabemAPIView, \
    GarantiaAPIView

urlpatterns = [
    path('bof/', BofAPIView.as_view(), name='bof'),
    path('calculo/', CalculoAPIView.as_view(), name='calculo'),
    path('calculoscombinada/', CalculoscombinadaAPIView.as_view(), name='calculoscombinada'),
    path('cboregracusteio/', CboregracusteioAPIView.as_view(), name='cboregracusteio'),
    path('comboloan/', ComboloanAPIView.as_view(), name='comboloan'),
    path('dadoscalculadorapipeline/', DadoscalculadorapipelineAPIView.as_view(), name='dadoscalculadorapipeline'),
    path('dgabaseoperacoes/', DgabaseoperacoesAPIView.as_view(), name='dgabaseoperacoes'),
    path('dgaceadiario/', DgaceadiarioAPIView.as_view(), name='dgaceadiario'),
    path('dgacurvasjuros/', DgacurvasjurosAPIView.as_view(), name='dgacurvasjuros'),
    path('dgagrupos/', DgagruposAPIView.as_view(), name='dgagrupos'),
    path('dgamatrizmigracao/', DgamatrizmigracaoAPIView.as_view(), name='dgamatrizmigracao'),
    path('dgamontecarlo/', DgamontecarloAPIView.as_view(), name='dgamontecarlo'),
    path('dgaparametrosestrategiaportfolio/', DgaparametrosestrategiaportfolioAPIView.as_view(),
         name='dgaparametrosestrategiaportfolio'),
    path('dgapercentualfepf/', DgapercentualfepfAPIView.as_view(), name='dgapercentualfepf'),
    path('dgarcpalfasbetas/', DgarcpalfasbetasAPIView.as_view(), name='dgarcpalfasbetas'),
    path('dgatargetpais/', DgatargetpaisAPIView.as_view(), name='dgatargetpais'),
    path('fprcnpj/', FprcnpjAPIView.as_view(), name='fprcnpj'),
    path('garantiabem/', GarantiabemAPIView.as_view(), name='garantiabem'),
    path('garantia/', GarantiaAPIView.as_view(), name='garantia'),
]