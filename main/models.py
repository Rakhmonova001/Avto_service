import qrcode.constants
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from .validators import ImageFileValidator
import qrcode
from io import BytesIO
from django.core.files import File


class User(AbstractUser):
    full_name = models.CharField(max_length=112, db_index=True, verbose_name="Ism")
    phone_number = models.CharField(max_length=11, unique=True, verbose_name="Telefon raqam", validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='Invalid number',
        )
    ])
    address = models.CharField(max_length=255, verbose_name="Manzil")

    class Meta:
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Foydalanuvchilar'

    def __str__(self):
        return self.username

class Employee(models.Model):
    user = models.OneToOneField(to='User', on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    profession = models.CharField(max_length=255, verbose_name="Kasb")
    salary = models.PositiveIntegerField(verbose_name="Maosh")
    age = models.IntegerField(default=18, verbose_name="Yosh")
    address = models.CharField(max_length=255, verbose_name="Manzil")
    experience = models.CharField(max_length=255, verbose_name="Tajriba")
    work_time = models.CharField(max_length=255, null=True, blank=True, verbose_name="Ish vaqti")
    rating = models.CharField(max_length=255, verbose_name="Reyting")
    garage = models.OneToOneField(to='Garage', on_delete=models.CASCADE, verbose_name="Garaj")

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Ishchilar'

    def __str__(self):
        return self.user.username

class Cassa(models.Model):
    total_amount = models.PositiveIntegerField(default=0, verbose_name="Umumiy summa")

    class Meta:
        verbose_name = 'Cassa'
        verbose_name_plural = 'Kassallar'

class Order(models.Model):
    owner_name = models.CharField(max_length=255, verbose_name="")
    is_delivery = models.BooleanField(default=False, verbose_name="Yetkazib berish")
    address = models.CharField(max_length=255, verbose_name="Manzil")
    car_name = models.CharField(max_length=255, verbose_name="Moshina nomi")
    car_number = models.IntegerField(default=8, verbose_name="Moshina raqami")
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True, verbose_name="QR code")

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=5,
            border=3,
        )
        qr.add_date(f"Your data to encode in the QR code: {self.order_id.username}")
        qr.make(fit=True)
        img = qr._image(fill_color="black", black="white")

        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)

        self.qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)

        super().save(*args, **kwargs)
    owner_phone_number = models.CharField(max_length=11, unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='Invalid number',
        )
    ])
    is_active = models.IntegerField(default=1, choices=(
        (1, 'wait'),
        (2, 'see'),
        (3, 'saw'),
    ))
    master_employee = models.ForeignKey(to='Employee', on_delete=models.CASCADE)
    problem = models.CharField(max_length=255, verbose_name="Muammo")
    service_cost = models.IntegerField(verbose_name="Xizmat narxi")
    start_time = models.DateTimeField(verbose_name="Boshlangan vaqt")

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Zakazlar'

class Payment(models.Model):
    admin = models.ForeignKey(to='Employee', on_delete=models.CASCADE, verbose_name="Admin")
    order = models.ForeignKey(to='Order', on_delete=models.CASCADE, verbose_name="Buyurtma")
    code = models.IntegerField(verbose_name="Kod")
    date = models.DateField(auto_now=True, verbose_name="Kun")
    payment_type = models.IntegerField(default=3, choices=(
        (1, "cash"),
        (2, "by_card"),
        (3, "other"),
    ), verbose_name="To'lov turi")
    payment_status = models.IntegerField(default=3, choices=(
        (1, "full_paid"),
        (2, "part_paid"),
        (3, "unpaid"),
    ), verbose_name="To'lov  holati")
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True, verbose_name="QR code")

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=5,
            border=3,
        )
        qr.add_date(f"Your data to encode in the QR code: {self.order_id.username}")
        qr.make(fit=True)
        img = qr._image(fill_color="black", black="white")

        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)

        self.qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)

        super().save(*args, **kwargs)

        class Meta:
            verbose_name = 'Payment'
            verbose_name_plural = 'Tolovlar'


class Garage(models.Model):
    number = models.IntegerField(verbose_name="Raqam")

    class Meta:
        verbose_name = 'Garage'
        verbose_name_plural = 'Garajlar'

        def __str__(self):
            return self.number


class Comment(models.Model):
    order = models.ForeignKey(to='Order', on_delete=models.CASCADE, verbose_name="Buyurtma")
    text = models.CharField(max_length=200, verbose_name="Matn")
    status = models.IntegerField(default=1, choices=(
        (1, 'comment'),
        (2, 'complain'),
        (3, 'suggest'),
    ), verbose_name="Holat")
    created_at = models.DateTimeField(auto_now=True, verbose_name="Yaratilgan")

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Kommentariyalar'


class Attendance(models.Model):
    employee = models.ForeignKey(to='Employee', on_delete=models.CASCADE)
    date = models.DateField(verbose_name="Kun")
    check_in = models.TimeField(null=True, blank=True, verbose_name="Ro'yxatdan otish")
    check_out = models.TimeField(null=True, blank=True, verbose_name="Tekshirib ko'rmoq")

    class Meta:
        unique_together = ['employee', 'date']

def clean(self):
    if self.check_out and self.chrck_in < self.check_in:
        raise ValidationError("Check-out time must be after check-in time.")

    def __str__(self):
        return f"{self.employee.username} - {self.date}"
