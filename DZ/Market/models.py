from django.db import models
from django.urls import reverse


class Store(models.Model):
    # store_id
    name = models.CharField(max_length=30, db_index=True)
    address = models.TextField()
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        db_table = 'Market"."Stores'
        ordering = ('name',)
        verbose_name = 'Store'
        verbose_name_plural = 'Store'

    def __str__(self):
        return f'{self.name}, {self.address}'

    def get_absolute_url(self):
        return reverse('product_list_by_store',
                       args=[self.slug])


class Product(models.Model):
    # product_id
    name = models.CharField(max_length=50, db_index=True)
    description = models.TextField()
    price = models.FloatField()
    store = models.ManyToManyField(Store, related_name='store')
    slug = models.SlugField(max_length=200, db_index=True)

    class Meta:
        db_table = 'Market"."Products'
        ordering = ('price',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return f'{self.name}, {self.description}, {self.price}'

    def get_absolute_url(self):
        return reverse('product_detail',
                       args=[self.id, self.slug])


class Order(models.Model):
    # order_id
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    created_at = models.DateTimeField()

    def __str__(self):
        return f'{self.created_at}'

    class Meta:
        db_table = 'Market"."Orders'


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return f'{self.amount}'

    class Meta:
        db_table = 'Market"."OrderDetails'
