from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


# manager for our custom model
class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError(_('The given email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self._create_user(email, password, **extra_fields)


class ContactType(models.Model):
    id = models.AutoField(db_column='icType', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='cDescription', max_length=50,
                                    db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                                    null=True)  # Field name made lowercase.
    description_an = models.CharField(db_column='cDescriptionAn', max_length=50,
                                      db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                                      null=True)  # Field name made lowercase.
    system = models.BooleanField(db_column='lSysteme', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblTypeContact'


class ContactSousType(models.Model):
    id = models.AutoField(db_column='icType', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='cDescription', max_length=50,
                                    db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                                    null=True)  # Field name made lowercase.
    description_an = models.CharField(db_column='cDescriptionAn', max_length=50,
                                      db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                                      null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='nType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblTypeContactSous'


class Language(models.Model):
    id = models.AutoField(db_column='icLangue', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='cDescription', max_length=50,
                                    db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                                    null=True)  # Field name made lowercase.
    description_an = models.CharField(db_column='cDescriptionAn', max_length=50,
                                      db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                                      null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLangue'


class Representant(models.Model):
    id = models.AutoField(db_column='icRepresentant', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='cNom', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                            null=True)  # Field name made lowercase.
    admin = models.BooleanField(db_column='lAdmin', blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='cMotPasse', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                 blank=True, null=True)  # Field name made lowercase.
    option = models.BooleanField(db_column='lOption', blank=True, null=True)  # Field name made lowercase.
    signature = models.TextField(db_column='mSignature', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                                  null=True)  # Field name made lowercase.
    security_group = models.IntegerField(db_column='fkSecuriteGroupe')  # Field name made lowercase.
    golibro = models.BooleanField(db_column='lGOLIBRO', blank=True, null=True)  # Field name made lowercase.
    acc_comptable = models.BooleanField(db_column='lAccComptable', blank=True, null=True)  # Field name made lowercase.
    client_account = models.BooleanField(db_column='bCompteClient')  # Field name made lowercase.
    email = models.EmailField(db_column='cEmail', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS',
                              blank=True, null=True)  # Field name made lowercase.
    dist_complete = models.BooleanField(db_column='bDistComplete', blank=True, null=True)  # Field name made lowercase.
    hourly_access = models.BooleanField(db_column='bAccesHoraire')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblRepresentant'


class Frequence(models.Model):
    id = models.AutoField(db_column='icFrequence', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='cDescription', max_length=50,
                                    db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                                    null=True)  # Field name made lowercase.
    description_an = models.CharField(db_column='cDescriptionAn', max_length=50,
                                      db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                                      null=True)  # Field name made lowercase.
    month = models.IntegerField(db_column='nMois', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblFrequence'


class Contact(models.Model):
    id = models.AutoField(db_column='icContact', primary_key=True)  # Field name made lowercase.
    type = models.ForeignKey('ContactType', models.DO_NOTHING, db_column='nType')  # Field name made lowercase.
    sous_contact_type = models.ForeignKey('ContactSousType', models.DO_NOTHING, db_column='nTypeSous', blank=True,
                                  null=True)  # Field name made lowercase.
    company = models.CharField(db_column='cEntreprise', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                   blank=True, null=True)  # Field name made lowercase.
    greeting = models.CharField(db_column='cSalutation', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                   blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='cNom', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                            null=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='cPrenom', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS',
                               blank=True, null=True)  # Field name made lowercase.
    address_1 = models.CharField(db_column='cAdresse1', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                 blank=True, null=True)  # Field name made lowercase.
    address_2 = models.CharField(db_column='cAdresse2', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                 blank=True, null=True)  # Field name made lowercase.
    town = models.CharField(db_column='cVille', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS',
                              blank=True, null=True)  # Field name made lowercase.
    province = models.CharField(db_column='cProvince', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                 blank=True, null=True)  # Field name made lowercase.
    postal_code = models.CharField(db_column='cCodePostal', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                   blank=True, null=True)  # Field name made lowercase.
    phone_1 = models.CharField(db_column='cTelephone1', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                   blank=True, null=True)  # Field name made lowercase.
    poste_1 = models.CharField(db_column='cPoste1', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS',
                               blank=True, null=True)  # Field name made lowercase.
    phone_2 = models.CharField(db_column='cTelephone2', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                   blank=True, null=True)  # Field name made lowercase.
    poste_2 = models.CharField(db_column='cPoste2', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS',
                               blank=True, null=True)  # Field name made lowercase.
    pagette = models.CharField(db_column='cPagette', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                blank=True, null=True)  # Field name made lowercase.
    cellphone = models.CharField(db_column='cCellulaire', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                   blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='cTelecopieur', max_length=10,
                                    db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                                    null=True)  # Field name made lowercase.
    email = models.EmailField(db_column='cEmail', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS',
                              blank=True, null=True)  # Field name made lowercase.
    website = models.CharField(db_column='cSiteWeb', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                blank=True, null=True)  # Field name made lowercase.
    language = models.ForeignKey('Language', models.DO_NOTHING, db_column='nLangue', blank=True,
                                null=True)  # Field name made lowercase.
    representative = models.ForeignKey('Representant', models.DO_NOTHING, db_column='nRepresentant', blank=True,
                                      null=True)  # Field name made lowercase.
    note = models.TextField(db_column='mNote', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                             null=True)  # Field name made lowercase.
    windows_directory = models.CharField(db_column='cRepertoireWindows', max_length=250,
                                          db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                                          null=True)  # Field name made lowercase.
    open_datetime = models.DateTimeField(db_column='dOuverture', blank=True, null=True)  # Field name made lowercase.
    updated_datetime = models.DateTimeField(db_column='dModification', blank=True, null=True)  # Field name made lowercase.
    reminder_datetime = models.DateTimeField(db_column='dRappel', blank=True, null=True)  # Field name made lowercase.
    frequency = models.ForeignKey('Frequence', models.DO_NOTHING, db_column='nFrequence', blank=True,
                                   null=True)  # Field name made lowercase.
    birth_date = models.DateTimeField(db_column='dNaissance', blank=True, null=True)  # Field name made lowercase.
    birth_date_2 = models.DateTimeField(db_column='dNaissance2', blank=True, null=True)  # Field name made lowercase.
    cellphone_3 = models.CharField(db_column='cTelephone3', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                   blank=True, null=True)  # Field name made lowercase.
    poste_3 = models.CharField(db_column='cPoste3', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS',
                               blank=True, null=True)  # Field name made lowercase.
    cell_owner = models.CharField(db_column='cProprietaireCellulaire', max_length=50,
                                               db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                                               null=True)  # Field name made lowercase.
    number = models.CharField(db_column='cNumero', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS',
                               blank=True, null=True)  # Field name made lowercase.
    occupation = models.CharField(db_column='cOccupation', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                   blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='cPays', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                             null=True)  # Field name made lowercase.
    num = models.IntegerField(db_column='nNum', blank=True, null=True)  # Field name made lowercase.
    cost = models.FloatField(db_column='nCout', blank=True, null=True)  # Field name made lowercase.
    copy_add = models.FloatField(db_column='nCopieAdd', blank=True, null=True)  # Field name made lowercase.
    tps = models.BooleanField(db_column='blnTPS')  # Field name made lowercase.
    tvq = models.BooleanField(db_column='blnTVQ')  # Field name made lowercase.
    terme_id = models.IntegerField(db_column='intTermeID', blank=True, null=True)  # Field name made lowercase.
    type_taxe_id = models.IntegerField(db_column='intTypeTaxeID', blank=True, null=True)  # Field name made lowercase.
    distributer = models.BooleanField(db_column='bDistributeur')  # Field name made lowercase.
    distrib_price_lbs = models.FloatField(db_column='nDistribPrixLbs', blank=True,
                                        null=True)  # Field name made lowercase.
    profit_margin = models.FloatField(db_column='nMargeBenefice', blank=True, null=True)  # Field name made lowercase.
    trans_profit_margin = models.FloatField(db_column='nMargeBeneficeTrans', blank=True,
                                            null=True)  # Field name made lowercase.
    distrib_admin_fees = models.FloatField(db_column='nFraisAdminDistrib', blank=True,
                                           null=True)  # Field name made lowercase.
    admin_other_fees_add = models.FloatField(db_column='nFraisAdminAutreAdd', blank=True,
                                            null=True)  # Field name made lowercase.
    folder_fees = models.FloatField(db_column='nFraisDossier', blank=True, null=True)  # Field name made lowercase.
    plus_base_profit_margin = models.FloatField(db_column='nMargeBeneficeBasePlus', blank=True,
                                               null=True)  # Field name made lowercase.
    plus_margin_profit = models.FloatField(db_column='nMargeBeneficePlus', blank=True,
                                           null=True)  # Field name made lowercase.
    volume_profit_margin = models.FloatField(db_column='nMargeBeneficeVolume', blank=True,
                                             null=True)  # Field name made lowercase.
    edit_cvr_fees = models.FloatField(db_column='nFraisModifCVR', blank=True, null=True)  # Field name made lowercase.
    edit_txt_fees = models.FloatField(db_column='nFraisModifTXT', blank=True, null=True)  # Field name made lowercase.
    add_copy_fees = models.FloatField(db_column='nFraisCopieAdd', blank=True, null=True)  # Field name made lowercase.
    limit_credit = models.FloatField(db_column='nLimiteCredit', blank=True, null=True)  # Field name made lowercase.
    actual_sold = models.FloatField(db_column='nSoldeActuel', blank=True, null=True)  # Field name made lowercase.
    insured_amount = models.FloatField(db_column='nMntAssure', blank=True, null=True)  # Field name made lowercase.
    export_amount = models.FloatField(db_column='nMntExporte', blank=True, null=True)  # Field name made lowercase.
    marginpostcanada = models.FloatField(db_column='nMargePosteCanada', blank=True,
                                          null=True)  # Field name made lowercase.
    marginflatratepod = models.FloatField(db_column='nMargeFlatRatePOD', blank=True,
                                          null=True)  # Field name made lowercase.
    bookmark = models.BooleanField(db_column='bSignet', blank=True, null=True)  # Field name made lowercase.
    base_bookmark = models.FloatField(db_column='nSignetBase', blank=True, null=True)  # Field name made lowercase.
    bookmark_the_100 = models.FloatField(db_column='nSignetLe100', blank=True, null=True)  # Field name made lowercase.
    bcvraplat = models.BooleanField(db_column='bCVRAPlat', blank=True, null=True)  # Field name made lowercase.
    ncvraplatle10 = models.FloatField(db_column='nCVRAPlatLe10', blank=True, null=True)  # Field name made lowercase.
    dinactif = models.DateTimeField(db_column='dInactif', blank=True, null=True)  # Field name made lowercase.
    golibro_booking_access = models.BooleanField(db_column='bAccesReservationGolibro')  # Field name made lowercase.
    api_billing_frequency = models.IntegerField(db_column='nFrequenceFacturationAPI', blank=True,
                                                   null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblContact'


class User(AbstractUser):
    """
      Custom user class inheriting AbstractBaseUser class
    """
    date_joined = None
    last_login = None
    id = models.AutoField(db_column='icLigne', primary_key=True)  # Field name made lowercase.
    contact = models.ForeignKey(Contact, models.DO_NOTHING, db_column='nContact')  # Field name made lowercase.
    greeting = models.CharField(db_column='cSalutation', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                   blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='cNom', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                            null=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='cPrenom', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS',
                               blank=True, null=True)  # Field name made lowercase.
    phone_1 = models.CharField(db_column='cTelephone1', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                   blank=True, null=True)  # Field name made lowercase.
    poste_1 = models.CharField(db_column='cPoste1', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS',
                               blank=True, null=True)  # Field name made lowercase.
    phone_2 = models.CharField(db_column='cTelephone2', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                   blank=True, null=True)  # Field name made lowercase.
    poste_2 = models.CharField(db_column='cPoste2', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS',
                               blank=True, null=True)  # Field name made lowercase.
    email = models.EmailField(db_column='cEmail', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS',
                              blank=True, null=True, unique=True)  # Field name made lowercase.
    occupation = models.CharField(db_column='cOccupation', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                   blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='mCommentaire', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                                    null=True)  # Field name made lowercase.
    birth_date = models.DateTimeField(db_column='dNaissance', blank=True, null=True)  # Field name made lowercase.
    birth_date_2 = models.DateTimeField(db_column='dNaissance2', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='strUsername', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                   blank=True, null=True)  # Field name made lowercase.
    strpassword = models.CharField(db_column='strPassword', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                   blank=True, null=True)  # Field name made lowercase.
    send_message = models.BooleanField(db_column='blnEnvoiMSG')  # Field name made lowercase.
    ftp_access = models.BooleanField(db_column='blnAccesFTP')  # Field name made lowercase.
    extranet_access = models.BooleanField(db_column='blnAccesExtranet')  # Field name made lowercase.
    is_staff = models.BooleanField(db_column='blnAccesAdmin')  # Field name made lowercase.
    msrepl_tran_version = models.CharField(max_length=36)
    billing_access = models.BooleanField(db_column='blnAccesFacturation')  # Field name made lowercase.
    examination_access = models.BooleanField(db_column='blnAccessEpreuve')  # Field name made lowercase.
    update_main_server = models.BooleanField(db_column='blnUpdateMainServer')  # Field name made lowercase.
    bv_access = models.BooleanField(db_column='blnAccessBv')  # Field name made lowercase.
    bv_admin_access = models.BooleanField(db_column='blnAccessBvAdmin')  # Field name made lowercase.
    bv_acheteur_access = models.BooleanField(db_column='blnAccessBvAcheteur')  # Field name made lowercase.
    bv_user_access = models.BooleanField(db_column='blnAccessBvUtilisateur')  # Field name made lowercase.
    accept_contract = models.BooleanField(db_column='blnAcceptContract')  # Field name made lowercase.
    dtm_accept_contact = models.DateField(db_column='dtmAcceptContact', blank=True,
                                        null=True)  # Field name made lowercase.
    str_password_encrypt = models.CharField(db_column='strPasswordEncrypt', max_length=100,
                                          db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                                          null=True)  # Field name made lowercase.
    api_access = models.BooleanField(db_column='blnAccessApi', blank=True, null=True)  # Field name made lowercase.
    str_api_password= models.CharField(db_column='strPasswordAPI', max_length=64,
                                      db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                                      null=True)  # Field name made lowercase.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        managed = True
        db_table = 'tblContactSecondaire'
