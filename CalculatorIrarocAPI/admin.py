from django.contrib import admin

from .models import Bof, Calculo, Calculoscombinada, Cboregracusteio, Comboloan, Dadoscalculadorapipeline, \
    Dgabaseoperacoes, Dgaceadiario, Dgacurvasjuros, Dgagrupos, Dgamatrizmigracao, Dgamontecarlo, \
    Dgaparametrosestrategiaportfolio, Dgapercentualfepf, Dgarcpalfasbetas, Dgatargetpais, Fprcnpj, Garantiabem, \
    Garantia



@admin.register(Bof)
class BofAdmin(admin.ModelAdmin):
    list_display = ('segmento', 'produto', 'modalidade', 'criacao', 'ativo')


@admin.register(Calculo)
class CalculoAdmin(admin.ModelAdmin):
    list_display = ('calculo', 'criacao')


@admin.register(Calculoscombinada)
class CalculoscombinadaAdmin(admin.ModelAdmin):
    list_display = ('ids_calc',)

@admin.register(Cboregracusteio)
class CboregracusteioAdmin(admin.ModelAdmin):
    list_display = ('produto', 'modalidade')


@admin.register(Comboloan)
class ComboloanAdmin(admin.ModelAdmin):
    list_display = ('instrumento', 'contraparte', 'ativo', 'deriv')


@admin.register(Dadoscalculadorapipeline)
class DadoscalculadorapipelineAdmin(admin.ModelAdmin):
    list_display = ('id_calculadora', 'produto')


@admin.register(Dgabaseoperacoes)
class DgabaseoperacoesAdmin(admin.ModelAdmin):
    list_display = ('cliente',)


@admin.register(Dgaceadiario)
class DgaceadiarioAdmin(admin.ModelAdmin):
    list_display = ('cliente',)


@admin.register(Dgacurvasjuros)
class DgacurvasjurosAdmin(admin.ModelAdmin):
    list_display = ('moeda', 'prazo', 'index')


@admin.register(Dgagrupos)
class DgagruposAdmin(admin.ModelAdmin):
    list_display = ('racf', 'carteira')


@admin.register(Dgamatrizmigracao)
class DgamatrizmigracaoAdmin(admin.ModelAdmin):
    list_dysplay = ('id_grupo', 'rating', 'mes', 'segmento')


@admin.register(Dgamontecarlo)
class DgamontecarloAdmin(admin.ModelAdmin):
    list_display = ('atv', 'passivo')


@admin.register(Dgaparametrosestrategiaportfolio)
class DgaparametrosestrategiaportfolioAdmin(admin.ModelAdmin):
    list_display = ( 'cliente', )


@admin.register(Dgapercentualfepf)
class DgapercentualfepfAdmin(admin.ModelAdmin):
    list_display = ('classe', 'prazo')


@admin.register(Dgarcpalfasbetas)
class DgarcpalfasbetasAdmin(admin.ModelAdmin):
    list_display = ('ativo', 'passivo', 'racf')


@admin.register(Dgatargetpais)
class DgatargetpaisAdmin(admin.ModelAdmin):
    list_display = ('pais', )


@admin.register(Fprcnpj)
class FprcnpjAdmin(admin.ModelAdmin):
    list_display = ('cnpj', )


@admin.register(Garantiabem)
class GarantiabemAdmin(admin.ModelAdmin):
    list_display = ('instrumento', )


@admin.register(Garantia)
class GarantiaAdmin(admin.ModelAdmin):
    list_display = ('instrumento', 'bem', 'natureza')

