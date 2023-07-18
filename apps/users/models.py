from django.db import models
from django.contrib.auth.models import Group, AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


# manager for our custom model
class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""
    use_in_migrations = True

    def _create_user(self, cemail, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not cemail:
            raise ValueError(_('The given email must be set'))
        cemail = self.normalize_email(cemail)
        user = self.model(cemail=cemail, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, cemail, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self._create_user(cemail, password, **extra_fields)


class Tbltypecontact(models.Model):
    ictype = models.AutoField(db_column='icType', primary_key=True)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cdescriptionan = models.CharField(db_column='cDescriptionAn', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lsysteme = models.BooleanField(db_column='lSysteme', blank=True, null=True)  # Field name made lowercase.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = True
        db_table = 'tblTypeContact'


class Tbltypecontactsous(models.Model):
    ictype = models.AutoField(db_column='icType', primary_key=True)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cdescriptionan = models.CharField(db_column='cDescriptionAn', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ntype = models.IntegerField(db_column='nType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tblTypeContactSous'


class Tbllangue(models.Model):
    iclangue = models.AutoField(db_column='icLangue', primary_key=True)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cdescriptionan = models.CharField(db_column='cDescriptionAn', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tblLangue'


class Tblrepresentant(models.Model):
    icrepresentant = models.AutoField(db_column='icRepresentant', primary_key=True)  # Field name made lowercase.
    cnom = models.CharField(db_column='cNom', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ladmin = models.BooleanField(db_column='lAdmin', blank=True, null=True)  # Field name made lowercase.
    cmotpasse = models.CharField(db_column='cMotPasse', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    loption = models.BooleanField(db_column='lOption', blank=True, null=True)  # Field name made lowercase.
    msignature = models.TextField(db_column='mSignature', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')  # Field name made lowercase. This field type is a guess.
    fksecuritegroupe = models.IntegerField(db_column='fkSecuriteGroupe')  # Field name made lowercase.
    lgolibro = models.BooleanField(db_column='lGOLIBRO', blank=True, null=True)  # Field name made lowercase.
    lacccomptable = models.BooleanField(db_column='lAccComptable', blank=True, null=True)  # Field name made lowercase.
    bcompteclient = models.BooleanField(db_column='bCompteClient')  # Field name made lowercase.
    cemail = models.CharField(db_column='cEmail', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bdistcomplete = models.BooleanField(db_column='bDistComplete', blank=True, null=True)  # Field name made lowercase.
    bacceshoraire = models.BooleanField(db_column='bAccesHoraire')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tblRepresentant'


class Tblfrequence(models.Model):
    icfrequence = models.AutoField(db_column='icFrequence', primary_key=True)  # Field name made lowercase.
    cdescription = models.CharField(db_column='cDescription', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cdescriptionan = models.CharField(db_column='cDescriptionAn', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nmois = models.IntegerField(db_column='nMois', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tblFrequence'


class Tblcontact(models.Model):
    iccontact = models.AutoField(db_column='icContact', primary_key=True)  # Field name made lowercase.
    ntype = models.ForeignKey('Tbltypecontact', models.DO_NOTHING, db_column='nType')  # Field name made lowercase.
    ntypesous = models.ForeignKey('Tbltypecontactsous', models.DO_NOTHING, db_column='nTypeSous', blank=True, null=True)  # Field name made lowercase.
    centreprise = models.CharField(db_column='cEntreprise', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    csalutation = models.CharField(db_column='cSalutation', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cnom = models.CharField(db_column='cNom', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cprenom = models.CharField(db_column='cPrenom', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cadresse1 = models.CharField(db_column='cAdresse1', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cadresse2 = models.CharField(db_column='cAdresse2', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cville = models.CharField(db_column='cVille', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cprovince = models.CharField(db_column='cProvince', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccodepostal = models.CharField(db_column='cCodePostal', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ctelephone1 = models.CharField(db_column='cTelephone1', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cposte1 = models.CharField(db_column='cPoste1', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ctelephone2 = models.CharField(db_column='cTelephone2', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cposte2 = models.CharField(db_column='cPoste2', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cpagette = models.CharField(db_column='cPagette', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ccellulaire = models.CharField(db_column='cCellulaire', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ctelecopieur = models.CharField(db_column='cTelecopieur', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cemail = models.CharField(db_column='cEmail', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    csiteweb = models.CharField(db_column='cSiteWeb', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nlangue = models.ForeignKey('Tbllangue', models.DO_NOTHING, db_column='nLangue', blank=True, null=True)  # Field name made lowercase.
    nrepresentant = models.ForeignKey('Tblrepresentant', models.DO_NOTHING, db_column='nRepresentant', blank=True, null=True)  # Field name made lowercase.
    mnote = models.TextField(db_column='mNote', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    crepertoirewindows = models.CharField(db_column='cRepertoireWindows', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    douverture = models.DateTimeField(db_column='dOuverture', blank=True, null=True)  # Field name made lowercase.
    dmodification = models.DateTimeField(db_column='dModification', blank=True, null=True)  # Field name made lowercase.
    drappel = models.DateTimeField(db_column='dRappel', blank=True, null=True)  # Field name made lowercase.
    nfrequence = models.ForeignKey('Tblfrequence', models.DO_NOTHING, db_column='nFrequence', blank=True, null=True)  # Field name made lowercase.
    dnaissance = models.DateTimeField(db_column='dNaissance', blank=True, null=True)  # Field name made lowercase.
    dnaissance2 = models.DateTimeField(db_column='dNaissance2', blank=True, null=True)  # Field name made lowercase.
    ctelephone3 = models.CharField(db_column='cTelephone3', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cposte3 = models.CharField(db_column='cPoste3', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cproprietairecellulaire = models.CharField(db_column='cProprietaireCellulaire', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cnumero = models.CharField(db_column='cNumero', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coccupation = models.CharField(db_column='cOccupation', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cpays = models.CharField(db_column='cPays', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nnum = models.IntegerField(db_column='nNum', blank=True, null=True)  # Field name made lowercase.
    ncout = models.FloatField(db_column='nCout', blank=True, null=True)  # Field name made lowercase.
    ncopieadd = models.FloatField(db_column='nCopieAdd', blank=True, null=True)  # Field name made lowercase.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')  # Field name made lowercase. This field type is a guess.
    blntps = models.BooleanField(db_column='blnTPS')  # Field name made lowercase.
    blntvq = models.BooleanField(db_column='blnTVQ')  # Field name made lowercase.
    inttermeid = models.IntegerField(db_column='intTermeID', blank=True, null=True)  # Field name made lowercase.
    inttypetaxeid = models.IntegerField(db_column='intTypeTaxeID', blank=True, null=True)  # Field name made lowercase.
    bdistributeur = models.BooleanField(db_column='bDistributeur')  # Field name made lowercase.
    ndistribprixlbs = models.FloatField(db_column='nDistribPrixLbs', blank=True, null=True)  # Field name made lowercase.
    nmargebenefice = models.FloatField(db_column='nMargeBenefice', blank=True, null=True)  # Field name made lowercase.
    nmargebeneficetrans = models.FloatField(db_column='nMargeBeneficeTrans', blank=True, null=True)  # Field name made lowercase.
    nfraisadmindistrib = models.FloatField(db_column='nFraisAdminDistrib', blank=True, null=True)  # Field name made lowercase.
    nfraisadminautreadd = models.FloatField(db_column='nFraisAdminAutreAdd', blank=True, null=True)  # Field name made lowercase.
    nfraisdossier = models.FloatField(db_column='nFraisDossier', blank=True, null=True)  # Field name made lowercase.
    nmargebeneficebaseplus = models.FloatField(db_column='nMargeBeneficeBasePlus', blank=True, null=True)  # Field name made lowercase.
    nmargebeneficeplus = models.FloatField(db_column='nMargeBeneficePlus', blank=True, null=True)  # Field name made lowercase.
    nmargebeneficevolume = models.FloatField(db_column='nMargeBeneficeVolume', blank=True, null=True)  # Field name made lowercase.
    nfraismodifcvr = models.FloatField(db_column='nFraisModifCVR', blank=True, null=True)  # Field name made lowercase.
    nfraismodiftxt = models.FloatField(db_column='nFraisModifTXT', blank=True, null=True)  # Field name made lowercase.
    nfraiscopieadd = models.FloatField(db_column='nFraisCopieAdd', blank=True, null=True)  # Field name made lowercase.
    nlimitecredit = models.FloatField(db_column='nLimiteCredit', blank=True, null=True)  # Field name made lowercase.
    nsoldeactuel = models.FloatField(db_column='nSoldeActuel', blank=True, null=True)  # Field name made lowercase.
    nmntassure = models.FloatField(db_column='nMntAssure', blank=True, null=True)  # Field name made lowercase.
    nmntexporte = models.FloatField(db_column='nMntExporte', blank=True, null=True)  # Field name made lowercase.
    nmargepostecanada = models.FloatField(db_column='nMargePosteCanada', blank=True, null=True)  # Field name made lowercase.
    nmargeflatratepod = models.FloatField(db_column='nMargeFlatRatePOD', blank=True, null=True)  # Field name made lowercase.
    bsignet = models.BooleanField(db_column='bSignet', blank=True, null=True)  # Field name made lowercase.
    nsignetbase = models.FloatField(db_column='nSignetBase', blank=True, null=True)  # Field name made lowercase.
    nsignetle100 = models.FloatField(db_column='nSignetLe100', blank=True, null=True)  # Field name made lowercase.
    bcvraplat = models.BooleanField(db_column='bCVRAPlat', blank=True, null=True)  # Field name made lowercase.
    ncvraplatle10 = models.FloatField(db_column='nCVRAPlatLe10', blank=True, null=True)  # Field name made lowercase.
    dinactif = models.DateTimeField(db_column='dInactif', blank=True, null=True)  # Field name made lowercase.
    baccesreservationgolibro = models.BooleanField(db_column='bAccesReservationGolibro')  # Field name made lowercase.
    nfrequencefacturationapi = models.IntegerField(db_column='nFrequenceFacturationAPI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tblContact'


class Tblcontactsecondaire(AbstractUser):
    """
      Custom user class inheriting AbstractBaseUser class
    """
    username = None
    first_name = None
    last_name = None
    email = None
    icligne = models.AutoField(db_column='icLigne', primary_key=True)  # Field name made lowercase.
    ncontact = models.ForeignKey(Tblcontact, models.DO_NOTHING, db_column='nContact')  # Field name made lowercase.
    csalutation = models.CharField(db_column='cSalutation', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cnom = models.CharField(db_column='cNom', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cprenom = models.CharField(db_column='cPrenom', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ctelephone1 = models.CharField(db_column='cTelephone1', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cposte1 = models.CharField(db_column='cPoste1', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ctelephone2 = models.CharField(db_column='cTelephone2', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cposte2 = models.CharField(db_column='cPoste2', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cemail = models.CharField(db_column='cEmail', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True, unique=True)  # Field name made lowercase.
    coccupation = models.CharField(db_column='cOccupation', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    mcommentaire = models.TextField(db_column='mCommentaire', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dnaissance = models.DateTimeField(db_column='dNaissance', blank=True, null=True)  # Field name made lowercase.
    dnaissance2 = models.DateTimeField(db_column='dNaissance2', blank=True, null=True)  # Field name made lowercase.
    strusername = models.CharField(db_column='strUsername', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    strpassword = models.CharField(db_column='strPassword', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ssma_timestamp = models.TextField(db_column='SSMA_TimeStamp')  # Field name made lowercase. This field type is a guess.
    blnenvoimsg = models.BooleanField(db_column='blnEnvoiMSG')  # Field name made lowercase.
    blnaccesftp = models.BooleanField(db_column='blnAccesFTP')  # Field name made lowercase.
    blnaccesextranet = models.BooleanField(db_column='blnAccesExtranet')  # Field name made lowercase.
    blnaccesadmin = models.BooleanField(db_column='blnAccesAdmin')  # Field name made lowercase.
    msrepl_tran_version = models.CharField(max_length=36)
    blnaccesfacturation = models.BooleanField(db_column='blnAccesFacturation')  # Field name made lowercase.
    blnaccessepreuve = models.BooleanField(db_column='blnAccessEpreuve')  # Field name made lowercase.
    blnupdatemainserver = models.BooleanField(db_column='blnUpdateMainServer')  # Field name made lowercase.
    blnaccessbv = models.BooleanField(db_column='blnAccessBv')  # Field name made lowercase.
    blnaccessbvadmin = models.BooleanField(db_column='blnAccessBvAdmin')  # Field name made lowercase.
    blnaccessbvacheteur = models.BooleanField(db_column='blnAccessBvAcheteur')  # Field name made lowercase.
    blnaccessbvutilisateur = models.BooleanField(db_column='blnAccessBvUtilisateur')  # Field name made lowercase.
    blnacceptcontract = models.BooleanField(db_column='blnAcceptContract')  # Field name made lowercase.
    dtmacceptcontact = models.DateField(db_column='dtmAcceptContact', blank=True, null=True)  # Field name made lowercase.
    strpasswordencrypt = models.CharField(db_column='strPasswordEncrypt', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    blnaccessapi = models.BooleanField(db_column='blnAccessApi', blank=True, null=True)  # Field name made lowercase.
    strpasswordapi = models.CharField(db_column='strPasswordAPI', max_length=64, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    USERNAME_FIELD = 'cemail'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        managed = True
        db_table = 'tblContactSecondaire'
