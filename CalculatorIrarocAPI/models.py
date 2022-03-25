from django.db import models


class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Bof(Base):
    segmento = models.CharField(max_length=255)
    produto = models.CharField(max_length=255)
    modalidade = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Bof'
        verbose_name_plural = 'Bofs'

    def __str__(self):
        return self.produto


class Calculo(Base):
    calculo = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'Calculo'
        verbose_name_plural = 'Calculos'

    def __str__(self):
        return f'{self.calculo}'


class Calculoscombinada(Base):
    ids_calc = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'Calculoscombinada'
        verbose_name_plural = 'Calculoscombinadas'

    def __str__(self):
        return f'{self.ids_calc}'


class Cboregracusteio(Base):
    produto = models.ForeignKey(Bof, related_name='produtos', on_delete=models.CASCADE)
    modalidade = models.ForeignKey(Bof, related_name='modalidades',on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cboregracusteio'
        verbose_name_plural = 'Cboregracusteios'

    def __str__(self):
        return self.modalidade


class Comboloan(Base):
    instrumento = models.CharField(max_length=255)
    contraparte = models.CharField(max_length=255)
    deriv = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Comboloan'
        verbose_name_plural = 'Comboloans'

    def __str__(self):
        return f'{self.instrumento} / {self.contraparte} / {self.deriv}'


class Dadoscalculadorapipeline(Base):
    id_calculadora = models.DecimalField(max_digits=2, decimal_places=1)
    produto = models.CharField(max_length=255, default='')

    class Meta:
        verbose_name = 'Dadoscalculadorapipeline'
        verbose_name_plural = 'Dadoscalculadorapipelines'

        def __str__(self):
            return self.id_calculadora


class Dgabaseoperacoes(Base):
    cliente = models.CharField(max_length=255, default='')

    class Meta:
        verbose_name = 'Dgabaseoperacoes'
        verbose_name_plural = 'Dgabaseoperacoess'

        def __str__(self):
            return self.cliente


class Dgaceadiario(Base):
    cliente = models.CharField(max_length=255, default='')

    class Meta:
        verbose_name = 'Dgaceadiario'
        verbose_name_plural = 'Dgaceadiarios'

        def __str__(self):
            return self.cliente


class Dgacurvasjuros(Base):
    moeda = models.DecimalField(max_digits=2, decimal_places=1)
    prazo = models.DecimalField(max_digits=2, decimal_places=1)
    index = models.CharField(max_length=255, default='')

    class Meta:
        verbose_name = 'Dgacurvasjuros'
        verbose_name_plural = 'Dgacurvasjuross'

    def __str__(self):
        return self.index


class Dgagrupos(Base):
    racf = models.CharField(max_length=255, default='')
    carteira = models.CharField(max_length=255, default='')

    class Meta:
        verbose_name = 'Dgagrupos'
        verbose_name_plural = 'Dgagruposs'

        def __str__(self):
            return self.racf


class Dgamatrizmigracao(Base):
    id_grupo = models.CharField(max_length=255, default='')
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    mes = models.CharField(max_length=255, default='')
    segmento = models.CharField(max_length=255, default='')

    class Meta:
        verbose_name = 'Dgamatrizmigracao'
        verbose_name_plural = 'Dgamatrizmigracoes'

        def __str__(self):
            return self.id_grupo


class Dgamontecarlo(Base):
    atv = models.CharField(max_length=50, default='')
    passivo = models.CharField(max_length=50, default='')

    class Meta:
        verbose_name = 'Dgamontecarlo'
        verbose_name_plural = 'Dgamontecarlos'

        def __str__(self):
            return self.atv


class Dgaparametrosestrategiaportfolio(Base):
    cliente = models.CharField(max_length=50, default='')

    class Meta:
        verbose_name = 'Dgaparametrosestrategiaportfolio'
        verbose_name_plural = 'Dgaparametrosestrategiaportfolios'

        def __str__(self):
            return self.cliente


class Dgapercentualfepf(Base):
    classe = models.CharField(max_length=50, default='')
    prazo = models.IntegerField(default='')

    class Meta:
        verbose_name = 'Dgapercentualfepf'
        verbose_name_plural = 'Dgapercentualfepfs'

        def __str__(self):
            return self.classe


class Dgarcpalfasbetas(Base):
    ativo = models.CharField(max_length=50, default='')
    passivo = models.CharField(max_length=50, default='')
    racf = models.CharField(max_length=50, default='')

    class Meta:
        verbose_name = 'dgarcpalfasbetas'
        verbose_name_plural = 'dgarcpalfasbetass'

        def __str__(self):
            return self.ativo


class Dgatargetpais(Base):
    pais = models.CharField(max_length=2, default='')

    class Meta:
        verbose_name = 'dgatargetpais'
        verbose_name_plural = 'dgatargetpaiss'

        def __str__(self):
            return self.pais


class Fprcnpj(Base):
    cnpj = models.CharField(max_length=14, default='')

    class Meta:
        verbose_name = 'fprcnpj'
        verbose_name_plural = 'fprcnpjs'

        def __str__(self):
            return self.cnpj


class Garantiabem(Base):
    instrumento = models.CharField(max_length=50, default='')

    class Meta:
        verbose_name = 'Garantiabem'
        verbose_name_plural = 'Garantiabens'

        def __str__(self):
            return self.instrumento


class Garantia(Base):
    instrumento = models.CharField(max_length=50, default='')
    bem = models.CharField(max_length=50, default='')
    natureza = models.CharField(max_length=50, default='')

    class Meta:
        verbose_name = 'Garantia'
        verbose_name_plural = 'Garantias'

        def __str__(self):
            return self.bem


