from django.db import models
from django.utils import timezone


class Ambient(models.Model):
    name = models.CharField(max_length=128, unique=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Table(models.Model):
    ambient = models.ForeignKey('Ambient', on_delete=models.CASCADE, related_name='tables')
    label = models.CharField(max_length=32)
    active = models.BooleanField(default=True)
    menus = models.ManyToManyField('Menu', through='Order', related_name='tables')

    class Meta:
        unique_together = ['ambient', 'label']

    def __str__(self):
        return '{} [{}]'.format(self.ambient.name, self.label)


class Menu(models.Model):
    name = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    REQUESTED = 1
    PREPARING = 2
    DISPATCHED = 3

    STATE_CHOICES = (
        (REQUESTED, 'Solicitado'),
        (PREPARING, 'Preparando'),
        (DISPATCHED, 'Despachado'),
    )

    menu = models.ForeignKey('Menu', on_delete=models.CASCADE, related_name='orders')
    table = models.ForeignKey('Table', on_delete=models.CASCADE, related_name='orders')
    state = models.IntegerField(choices=STATE_CHOICES, default=REQUESTED)
    detail = models.CharField(max_length=256, blank=True, null=True)
    requested_at = models.DateTimeField(auto_now_add=True)
    dispatched_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '{} [Mesa {}]'.format(self.menu, self.table)

    def save(self, *args, **kwargs):
        if self.state == self.DISPATCHED:
            if self.dispatched_at is None:
                self.dispatched_at = timezone.now()
        else:
            self.dispatched_at = None
        super().save(*args, **kwargs)
