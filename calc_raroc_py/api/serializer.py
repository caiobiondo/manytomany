from rest_framework import serializers
from calc_raroc_py.models import Fluxo, calculaRaroc


class FluxoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fluxo
        fields = ['id', 'data', 'desembolso', 'amortiza', 'juros', 'mitiga', 'dc']


class calculaRarocSerializer(serializers.ModelSerializer):
    class Meta:
        model = calculaRaroc
        fields = ['id', 'id_grupo', 'cnpj_cabeca', 'ratingOper', 'ratingGrupo', 'id_segmento_risco_cabeca',
                  'id_segmento_risco_grupo', 'notional', 'indexador', 'indexadorGarantia', 'prazo_total',
                  'qtd_parcela', 'dt_inicio', 'dt_final', 'produto', 'modalidade', 'classe_produto',
                  'classe_derivativo', 'index_ativo', 'index_passivo', 'perc_uti', 'fluxo', 'fluxo',
                  'formato_taxa', 'spread', 'CommitmentSpread', 'ValorLimiteLinha', 'IE', 'prazovenda',
                  'TxCliente', 'taxafunding', 'taxashortfunding', 'openDivOTS',
                  'qtde_titulos', 'pb_adicional', 'iss', 'fpr', 'fpr_pre', 'fpr_pos', 'frp', 'mitigacaoCEA',
                  'mitigacaoCEA2', 'MitigacaoKREG', 'FXSpot', 'pzoMedio', 'onShore', 'FEE', 'raroc_ref',
                  'prazo_indeterminado', 'lgd', 'veiculo_legal', 'epe_constante', 'epe_manual', 'custo_manual',
                  'id_volatilidade', 'prospectivo', 'perc_bof']
        depth = 1
