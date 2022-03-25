from django.db import models


class Fluxo(models.Model):
    data = models.DateField()
    desembolso = models.CharField(max_length=50)
    amortiza = models.CharField(max_length=2)
    juros = models.CharField(max_length=50)
    mitiga = models.CharField(max_length=2)
    dc = models.IntegerField()

    objects = models.Manager()

    def __str__(self):
        return self.desembolso


class calculaRaroc(models.Model):
    id_grupo = models.CharField(max_length=50)
    cnpj_cabeca = models.CharField(max_length=50)
    ratingOper = models.CharField(max_length=50)
    ratingGrupo = models.CharField(max_length=50)
    id_segmento_risco_cabeca = models.CharField(max_length=5)
    id_segmento_risco_grupo = models.CharField(max_length=5)
    notional= models.IntegerField()
    indexador = models.CharField(max_length=3)
    indexadorGarantia = models.CharField(max_length=3)
    prazo_total = models.CharField(max_length=3)
    qtd_parcela = models.CharField(max_length=2)
    dt_inicio = models.DateField()
    dt_final = models.DateField()
    produto = models.CharField(max_length=2)
    modalidade = models.CharField(max_length=50)
    classe_produto = models.CharField(max_length=3)
    classe_derivativo = models.CharField(max_length=3)
    index_ativo = models.CharField(max_length=3)
    index_passivo = models.CharField(max_length=3)
    perc_uti = models.CharField(max_length=3)
    fluxo = models.ManyToManyField(Fluxo)
    formato_taxa = models.CharField(max_length=50)
    spread = models.CharField(max_length=3)
    CommitmentSpread = models.CharField(max_length=3)
    ValorLimiteLinha = models.IntegerField()
    IE = models.CharField(max_length=50)
    prazovenda = models.CharField(max_length=3)
    TxCliente = models.CharField(max_length=3)
    taxafunding = models.CharField(max_length=3)
    taxashortfunding = models.CharField(max_length=3)
    openDivOTS = models.BooleanField(default=False)
    qtde_titulos = models.CharField(max_length=3)
    pb_adicional = models.CharField(max_length=3)
    iss = models.CharField(max_length=50)
    fpr = models.CharField(max_length=50)
    fpr_pre = models.CharField(max_length=50)
    fpr_pos = models.CharField(max_length=50)
    frp = models.CharField(max_length=3)
    mitigacaoCEA = models.CharField(max_length=3)
    mitigacaoCEA2 = models.CharField(max_length=3)
    MitigacaoKREG = models.CharField(max_length=3)
    FXSpot = models.CharField(max_length=3)
    pzoMedio = models.CharField(max_length=50)
    onShore = models.CharField(max_length=50)
    FEE = models.CharField(max_length=3)
    raroc_ref = models.IntegerField()
    prazo_indeterminado = models.CharField(max_length=50)
    lgd = models.CharField(max_length=50)
    veiculo_legal = models.CharField(max_length=50)
    epe_constante = models.BooleanField(default=True)
    epe_manual = models.CharField(max_length=3)
    custo_manual = models.IntegerField()
    id_volatilidade = models.CharField(max_length=3)
    prospectivo = models.BooleanField(default=False)
    perc_bof = models.CharField(max_length=3)

    objects = models.Manager()

    def __str__(self):
        return self.cnpj_cabeca
