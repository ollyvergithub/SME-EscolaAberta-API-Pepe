from django.db import models


class Turmas(models.Model):
    dre = models.TextField(blank=True, null=True)
    codesc = models.CharField(max_length=6, blank=True, null=True)
    codinep = models.IntegerField(blank=True, null=True)
    tipoesc = models.CharField(max_length=12, blank=True, null=True)
    nomesc = models.CharField(max_length=60, blank=True, null=True)
    subpref = models.CharField(max_length=35, blank=True, null=True)
    distrito = models.TextField(blank=True, null=True)
    setor = models.SmallIntegerField(blank=True, null=True)
    dturnos = models.TextField(blank=True, null=True)
    t2d3d = models.TextField(blank=True, null=True)
    numsala = models.CharField(max_length=6, blank=True, null=True)
    codamb = models.IntegerField(blank=True, null=True)
    descamb = models.CharField(max_length=70, blank=True, null=True)
    capreal = models.IntegerField(blank=True, null=True)
    metragem = models.IntegerField(blank=True, null=True)
    codturm = models.IntegerField(primary_key=True)
    ano = models.IntegerField(blank=True, null=True)
    modal = models.CharField(max_length=60, blank=True, null=True)
    semestre = models.IntegerField(blank=True, null=True)
    rede = models.TextField(blank=True, null=True)
    cdserie = models.IntegerField(blank=True, null=True)
    descserie = models.CharField(max_length=40, blank=True, null=True)
    turno = models.IntegerField(blank=True, null=True)
    turma = models.CharField(max_length=15, blank=True, null=True)
    vagofer = models.IntegerField(blank=True, null=True)
    matric = models.BigIntegerField(blank=True, null=True)
    alu_teg = models.BigIntegerField(blank=True, null=True)
    alu_teg_def = models.BigIntegerField(blank=True, null=True)
    hora_inicio = models.CharField(max_length=4, blank=True, null=True)
    hora_final = models.CharField(max_length=4, blank=True, null=True)
    dt_inclusao = models.DateTimeField(blank=True, null=True)
    localizacao = models.CharField(max_length=6, blank=True, null=True)
    classes = models.IntegerField(blank=True, null=True)
    x_semana = models.BigIntegerField(blank=True, null=True)
    durac_dia = models.IntegerField(blank=True, null=True)
    durac_semana = models.FloatField(blank=True, null=True)
    escolarizacao = models.TextField(blank=True, null=True)
    dias = models.TextField(blank=True, null=True)
    al_reprov = models.FloatField(blank=True, null=True)
    al_evad = models.FloatField(blank=True, null=True)
    al_aprov = models.FloatField(blank=True, null=True)
    al_fale = models.FloatField(blank=True, null=True)
    al_excl = models.FloatField(blank=True, null=True)
    al_ncom = models.FloatField(blank=True, null=True)
    al_nrem = models.FloatField(blank=True, null=True)
    pnee_ah = models.BigIntegerField(blank=True, null=True)
    pnee_da = models.BigIntegerField(blank=True, null=True)
    pnee_df = models.BigIntegerField(blank=True, null=True)
    pnee_dv = models.BigIntegerField(blank=True, null=True)
    pnee_di = models.BigIntegerField(blank=True, null=True)
    pnee_tgd = models.BigIntegerField(blank=True, null=True)
    pnee_bv = models.BigIntegerField(blank=True, null=True)
    pnee_ba = models.BigIntegerField(blank=True, null=True)
    pnee_tdi = models.BigIntegerField(blank=True, null=True)
    pnee_mul = models.BigIntegerField(blank=True, null=True)
    pnee_suce = models.BigIntegerField(blank=True, null=True)
    cadeir = models.BigIntegerField(blank=True, null=True)
    pnee_tot = models.BigIntegerField(blank=True, null=True)
    database = models.DateField(blank=True, null=True)