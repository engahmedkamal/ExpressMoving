from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Client(models.Model):
    mobile_no = models.CharField(max_length=25)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(editable=False)
    updateAt = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.createdAt = timezone.now()
        self.updateAt = timezone.now()
        return super(Client, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Vehicle(models.Model):
    type = models.CharField(max_length=50)
    enabled = models.BooleanField(default=True)
    createdAt = models.DateTimeField(editable=False)
    updateAt = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.createdAt = timezone.now()
        self.updateAt = timezone.now()
        return super(Vehicle, self).save(*args, **kwargs)

    def __str__(self):
        return self.type


class VehicleType(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    size = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    enabled = models.BooleanField(default=True)
    vehicle_img=models.FileField(null=True)
    createdAt = models.DateTimeField(editable=False)
    updateAt = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.createdAt = timezone.now()
        self.updateAt = timezone.now()
        return super(VehicleType, self).save(*args, **kwargs)

    def __str__(self):
        return self.vehicle.type + " " + self.size


class Order(models.Model):
    order_type = (
        (0, 'Local'),
        (1, 'Long Distance'),
    )
    order_status = (
        (0, 'created'),
        (1, 'scheduled'),
        (2, 'delivered'),
        (3, 'canceled')
    )
    vehicle = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    trackingId = models.CharField(db_index=True, max_length=50)
    totalCost = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    depositValue = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    pickFrom = models.CharField(max_length=1000)
    destinationTo = models.CharField(max_length=1000)
    orderType = models.IntegerField(choices=order_type)
    orderStatus = models.IntegerField(choices=order_status, default=0)
    noOfWorkers = models.IntegerField()
    noOFHours = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    createdAt = models.DateTimeField(editable=False)
    updateAt = models.DateTimeField()
    orderDate = models.DateField(null=False)
    fromTime = models.TimeField(null=False)
    toTime = models.TimeField(null=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.createdAt = timezone.now()
        self.updateAt = timezone.now()
        return super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return self.trackingId
