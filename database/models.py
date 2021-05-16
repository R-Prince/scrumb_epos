from django.db import models
from django.db.models import Sum


# Total SKU units sold
class Sku(models.Model):
    sku = models.CharField(max_length=50, null=False, blank=False)
    sku_description = models.CharField(max_length=300, null=False, blank=False)
    total_units = models.IntegerField(null=False, blank=False)

    def update_units(self):
        """
        Update total units
        """
        self.total_units = self.units.aggregate(
            Sum('units_sold'))['units_sold__sum'] or 0
        self.save()

    def __str__(self):
        return self.sku


# Invoice Line items
class SkuData(models.Model):
    sku = models.ForeignKey(
        Sku, null=False, blank=False,
        on_delete=models.CASCADE,
        related_name='units')
    retailer = models.CharField(max_length=500, null=False, blank=False)
    size = models.CharField(max_length=500, null=False, blank=False)
    category = models.CharField(max_length=500, null=False, blank=False)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False)
    units_sold = models.IntegerField(null=False, blank=False)
    sales_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False,
        editable=False)
    date = models.DateField(null=False, blank=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the sales_total
        """
        self.sales_total = self.units_sold + self.price
        super().save(*args, **kwargs)

    def __str__(self):
        return self.retailer
