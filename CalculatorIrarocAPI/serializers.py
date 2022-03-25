from rest_framework import serializers

from .models import Bof, Calculo, Calculoscombinada, Cboregracusteio, Comboloan, Dadoscalculadorapipeline, \
    Dgabaseoperacoes, Dgaceadiario, Dgacurvasjuros, Dgagrupos, Dgamatrizmigracao, Dgamontecarlo, \
    Dgaparametrosestrategiaportfolio, Dgapercentualfepf, Dgarcpalfasbetas, Dgatargetpais, Fprcnpj, Garantiabem, \
    Garantia


class BofSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bof
        fields = (
            'id',
            'segmento',
            'produto',
            'modalidade',
             'criacao',
            'ativo'
        )


class CalculoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Calculo
        fields = (
            'id',
            'calculo'
        )


class CalculoscombinadaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Calculoscombinada
        fields = (
            'id',
            'ids_calc'
        )


class CboregracusteioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cboregracusteio
        fields = (
            'produto',
            'modalidade'
        )


class ComboloanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comboloan
        fields = (
            'id',
            'instrumento',
            'contraparte',
            'ativo',
            'deriv'
        )


class DadoscalculadorapipelineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dadoscalculadorapipeline
        fields = (
            'id',
            'id_calculadora',
            'produto'
        )


class DgabaseoperacoesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dgabaseoperacoes
        fields = (
            'id',
            'cliente'
        )


class DgaceadiarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dgaceadiario
        fields = (
            'id',
            'cliente'
        )


class DgacurvasjurosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dgacurvasjuros
        fields = (
            'id',
            'moeda',
            'prazo',
            'index'
        )


class DgagruposSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dgagrupos
        fields = (
            'id',
            'racf',
            'carteira'
        )


class DgamatrizmigracaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dgamatrizmigracao
        fields = (
            'id',
            'id_grupo',
            'rating',
            'mes',
            'segmento'

        )


class DgamontecarloSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dgamontecarlo
        fields = (
            'id',
            'atv',
            'passivo'

        )


class DgaparametrosestrategiaportfolioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dgaparametrosestrategiaportfolio
        fields = (
            'id',
            'cliente'
        )


class DgapercentualfepfSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dgapercentualfepf
        fields = (
            'id',
            'classe',
            'prazo'
        )


class DgarcpalfasbetasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dgarcpalfasbetas
        fields = (
            'ativo',
            'passivo',
            'racf'
        )


class DgatargetpaisSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dgatargetpais
        fields = (
            'id',
            'pais'
        )


class FprcnpjSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fprcnpj
        fields = (
            'id',
            'cnpj'
        )


class GarantiabemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Garantiabem
        fields = (
            'id',
            'instrumento'
        )


class GarantiaSerializer(serializers.ModelSerializer):

    class Meta:
        Model = Garantia
        fields = (
            'id',
            'instrumento'
        )
