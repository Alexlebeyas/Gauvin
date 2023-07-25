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
        user = User.objects.first()
        user.pk = None
        user.email = email
        user.is_staff = True
        user.is_superuser = True
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
    id = models.AutoField(db_column='icType', primary_key=True)
    description = models.CharField(db_column='cDescription', max_length=50,
                                   db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                                   null=True)
    description_en = models.CharField(db_column='cDescriptionAn', max_length=50,
                                      db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                                      null=True)
    is_system = models.BooleanField(db_column='lSysteme', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblTypeContact'


class ContactSubType(models.Model):
    id = models.AutoField(db_column='icType', primary_key=True)
    description = models.CharField(db_column='cDescription', max_length=50,
                                   db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                                   null=True)
    description_en = models.CharField(db_column='cDescriptionAn', max_length=50,
                                      db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                                      null=True)
    contact_type_id = models.IntegerField(db_column='nType', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblTypeContactSous'


class Language(models.Model):
    id = models.AutoField(db_column='icLangue', primary_key=True)
    description = models.CharField(db_column='cDescription', max_length=50,
                                   db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                                   null=True)
    description_en = models.CharField(db_column='cDescriptionAn', max_length=50,
                                      db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                                      null=True)

    class Meta:
        managed = False
        db_table = 'tblLangue'


class Representative(models.Model):
    id = models.AutoField(db_column='icRepresentant', primary_key=True)
    name = models.CharField(db_column='cNom', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                            null=True)
    is_admin = models.BooleanField(db_column='lAdmin', blank=True, null=True)
    password = models.CharField(db_column='cMotPasse', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                blank=True, null=True)
    option = models.BooleanField(db_column='lOption', blank=True, null=True)
    signature = models.TextField(db_column='mSignature', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                                 null=True)
    security_group = models.IntegerField(db_column='fkSecuriteGroupe')
    is_golibro = models.BooleanField(db_column='lGOLIBRO', blank=True, null=True)
    is_acc_comptable = models.BooleanField(db_column='lAccComptable', blank=True, null=True)
    is_client_account = models.BooleanField(db_column='bCompteClient')
    email = models.EmailField(db_column='cEmail', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS',
                              blank=True, null=True)
    is_dist_complete = models.BooleanField(db_column='bDistComplete', blank=True, null=True)
    has_hourly_access = models.BooleanField(db_column='bAccesHoraire')

    class Meta:
        managed = False
        db_table = 'tblRepresentant'


class Frequency(models.Model):
    id = models.AutoField(db_column='icFrequence', primary_key=True)
    description = models.CharField(db_column='cDescription', max_length=50,
                                   db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                                   null=True)
    description_en = models.CharField(db_column='cDescriptionAn', max_length=50,
                                      db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                                      null=True)
    month = models.IntegerField(db_column='nMois', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblFrequence'


class Contact(models.Model):
    id = models.AutoField(db_column='icContact', primary_key=True)
    contact_type_id = models.ForeignKey('ContactType', models.DO_NOTHING, db_column='nType')
    contact_sub_type_id = models.ForeignKey('ContactSubType', models.DO_NOTHING, db_column='nTypeSous', blank=True,
                                          null=True)
    company = models.CharField(db_column='cEntreprise', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS',
                               blank=True, null=True)
    greeting = models.CharField(db_column='cSalutation', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                blank=True, null=True)
    last_name = models.CharField(db_column='cNom', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                 blank=True,
                                 null=True)
    first_name = models.CharField(db_column='cPrenom', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                  blank=True, null=True)
    address_1 = models.CharField(db_column='cAdresse1', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                 blank=True, null=True)
    address_2 = models.CharField(db_column='cAdresse2', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                 blank=True, null=True)
    city = models.CharField(db_column='cVille', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS',
                            blank=True, null=True)
    province = models.CharField(db_column='cProvince', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                blank=True, null=True)
    postal_code = models.CharField(db_column='cCodePostal', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                   blank=True, null=True)
    phone_1 = models.CharField(db_column='cTelephone1', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS',
                               blank=True, null=True)
    ext_1 = models.CharField(db_column='cPoste1', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS',
                             blank=True, null=True)
    phone_2 = models.CharField(db_column='cTelephone2', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS',
                               blank=True, null=True)
    ext_2 = models.CharField(db_column='cPoste2', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS',
                             blank=True, null=True)
    pager = models.CharField(db_column='cPagette', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS',
                               blank=True, null=True)
    cellphone = models.CharField(db_column='cCellulaire', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                 blank=True, null=True)
    fax = models.CharField(db_column='cTelecopieur', max_length=10,
                           db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                           null=True)
    email = models.EmailField(db_column='cEmail', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS',
                              blank=True, null=True)
    website = models.CharField(db_column='cSiteWeb', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS',
                               blank=True, null=True)
    language_id = models.ForeignKey('Language', models.DO_NOTHING, db_column='nLangue', blank=True,
                                 null=True)
    representative_id = models.ForeignKey('Representative', models.DO_NOTHING, db_column='nRepresentant', blank=True,
                                       null=True)
    note = models.TextField(db_column='mNote', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                            null=True)
    windows_directory = models.CharField(db_column='cRepertoireWindows', max_length=250,
                                         db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                                         null=True)
    open_datetime = models.DateTimeField(db_column='dOuverture', blank=True, null=True)
    updated_at = models.DateTimeField(db_column='dModification', blank=True,
                                            null=True)
    reminder_datetime = models.DateTimeField(db_column='dRappel', blank=True, null=True)
    frequency_id = models.ForeignKey('Frequency', models.DO_NOTHING, db_column='nFrequence', blank=True,
                                  null=True)
    birth_date = models.DateField(db_column='dNaissance', blank=True, null=True)
    birth_date_2 = models.DateField(db_column='dNaissance2', blank=True, null=True)
    cellphone_3 = models.CharField(db_column='cTelephone3', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                   blank=True, null=True)
    ext_3 = models.CharField(db_column='cPoste3', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS',
                             blank=True, null=True)
    cell_owner = models.CharField(db_column='cProprietaireCellulaire', max_length=50,
                                  db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                                  null=True)
    number = models.CharField(db_column='cNumero', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS',
                              blank=True, null=True)
    occupation = models.CharField(db_column='cOccupation', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                  blank=True, null=True)
    country = models.CharField(db_column='cPays', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS',
                               blank=True,
                               null=True)
    num = models.IntegerField(db_column='nNum', blank=True, null=True)
    cost = models.FloatField(db_column='nCout', blank=True, null=True)
    copy_add = models.FloatField(db_column='nCopieAdd', blank=True, null=True)
    has_gst = models.BooleanField(db_column='blnTPS')
    has_qst = models.BooleanField(db_column='blnTVQ')
    term_id = models.IntegerField(db_column='intTermeID', blank=True, null=True)
    type_taxe_id = models.IntegerField(db_column='intTypeTaxeID', blank=True, null=True)
    is_distributer = models.BooleanField(db_column='bDistributeur')
    distrib_price_lbs = models.FloatField(db_column='nDistribPrixLbs', blank=True,
                                          null=True)
    profit_margin = models.FloatField(db_column='nMargeBenefice', blank=True, null=True)
    trans_profit_margin = models.FloatField(db_column='nMargeBeneficeTrans', blank=True,
                                            null=True)
    distrib_admin_fees = models.FloatField(db_column='nFraisAdminDistrib', blank=True,
                                           null=True)
    admin_other_fees_add = models.FloatField(db_column='nFraisAdminAutreAdd', blank=True,
                                             null=True)
    folder_fees = models.FloatField(db_column='nFraisDossier', blank=True, null=True)
    plus_base_profit_margin = models.FloatField(db_column='nMargeBeneficeBasePlus', blank=True,
                                                null=True)
    plus_margin_profit = models.FloatField(db_column='nMargeBeneficePlus', blank=True,
                                           null=True)
    volume_profit_margin = models.FloatField(db_column='nMargeBeneficeVolume', blank=True,
                                             null=True)
    edit_cvr_fees = models.FloatField(db_column='nFraisModifCVR', blank=True, null=True)
    edit_txt_fees = models.FloatField(db_column='nFraisModifTXT', blank=True, null=True)
    add_copy_fees = models.FloatField(db_column='nFraisCopieAdd', blank=True, null=True)
    credit_limit = models.FloatField(db_column='nLimiteCredit', blank=True, null=True)
    current_sold = models.FloatField(db_column='nSoldeActuel', blank=True, null=True)
    insured_amount = models.FloatField(db_column='nMntAssure', blank=True, null=True)
    exported_amount = models.FloatField(db_column='nMntExporte', blank=True, null=True)
    margin_post_canada = models.FloatField(db_column='nMargePosteCanada', blank=True,
                                         null=True)
    margin_flat_rate_pod = models.FloatField(db_column='nMargeFlatRatePOD', blank=True,
                                          null=True)
    is_bookmark = models.BooleanField(db_column='bSignet', blank=True, null=True)
    base_bookmark = models.FloatField(db_column='nSignetBase', blank=True, null=True)
    bookmark_the_100 = models.FloatField(db_column='nSignetLe100', blank=True, null=True)
    is_bcvraplat = models.BooleanField(db_column='bCVRAPlat', blank=True, null=True)
    ncvraplatle10 = models.FloatField(db_column='nCVRAPlatLe10', blank=True, null=True)
    dinactif = models.DateTimeField(db_column='dInactif', blank=True, null=True)
    has_golibro_booking_access = models.BooleanField(db_column='bAccesReservationGolibro')
    api_billing_frequency = models.IntegerField(db_column='nFrequenceFacturationAPI', blank=True,
                                                null=True)

    class Meta:
        managed = False
        db_table = 'tblContact'


class User(AbstractUser):
    """
      Custom user class inheriting AbstractBaseUser class
    """
    date_joined = None
    last_login = None
    id = models.AutoField(db_column='icLigne', primary_key=True)
    contact_id = models.ForeignKey(Contact, models.DO_NOTHING, db_column='nContact')
    greeting = models.CharField(db_column='cSalutation', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                blank=True, null=True)
    last_name = models.CharField(db_column='cNom', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                 blank=True,
                                 null=True)
    first_name = models.CharField(db_column='cPrenom', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                  blank=True, null=True)
    phone_1 = models.CharField(db_column='cTelephone1', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS',
                               blank=True, null=True)
    ext_1 = models.CharField(db_column='cPoste1', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS',
                             blank=True, null=True)
    phone_2 = models.CharField(db_column='cTelephone2', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS',
                               blank=True, null=True)
    ext_2 = models.CharField(db_column='cPoste2', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS',
                             blank=True, null=True)
    email = models.EmailField(db_column='cEmail', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS',
                              blank=True, null=True, unique=True)
    occupation = models.CharField(db_column='cOccupation', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                  blank=True, null=True)
    comment = models.TextField(db_column='mCommentaire', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                               null=True)
    birth_date = models.DateField(db_column='dNaissance', blank=True, null=True)
    birth_date_2 = models.DateField(db_column='dNaissance2', blank=True, null=True)
    username = models.CharField(db_column='strUsername', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                blank=True, null=True)
    strpassword = models.CharField(db_column='strPassword', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                   blank=True, null=True)
    can_send_message = models.BooleanField(db_column='blnEnvoiMSG')
    has_ftp_access = models.BooleanField(db_column='blnAccesFTP')
    has_extranet_access = models.BooleanField(db_column='blnAccesExtranet')
    is_staff = models.BooleanField(db_column='blnAccesAdmin')
    msrepl_tran_version = models.CharField(max_length=36)
    has_billing_access = models.BooleanField(db_column='blnAccesFacturation')
    has_examination_access = models.BooleanField(db_column='blnAccessEpreuve')
    has_update_main_server = models.BooleanField(db_column='blnUpdateMainServer')
    has_bv_access = models.BooleanField(db_column='blnAccessBv')
    has_bv_admin_access = models.BooleanField(db_column='blnAccessBvAdmin')
    has_bv_acheteur_access = models.BooleanField(db_column='blnAccessBvAcheteur')
    has_bv_user_access = models.BooleanField(db_column='blnAccessBvUtilisateur')
    can_accept_contract = models.BooleanField(db_column='blnAcceptContract')
    dtm_accept_contact = models.DateField(db_column='dtmAcceptContact', blank=True,
                                          null=True)
    str_password_encrypt = models.CharField(db_column='strPasswordEncrypt', max_length=100,
                                            db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                                            null=True)
    has_api_access = models.BooleanField(db_column='blnAccessApi', blank=True, null=True)
    str_api_password = models.CharField(db_column='strPasswordAPI', max_length=64,
                                        db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True,
                                        null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __int__(self):
        return self.pk

    class Meta:
        managed = True
        db_table = 'tblContactSecondaire'
