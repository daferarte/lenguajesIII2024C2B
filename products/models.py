from django.db import models

# Create your models here.
class ProductsCategory(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    description = models.TextField(verbose_name="Descripción", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")
    
    class Meta:
        verbose_name = 'Categoria de producto'
        verbose_name_plural = 'Categorias de productos'
        
    def __str__(self):
        return self.name
    
class Products(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    description = models.TextField(verbose_name="Descripción", blank=True, null=True)
    amount = models.CharField(max_length=150, verbose_name='Cantidad')
    cost = models.CharField(max_length=150, verbose_name='Costo')
    image = models.ImageField(default='null', verbose_name='Imagen', upload_to='products', blank=True, null=True)
    publisher = models.BooleanField(default=True, verbose_name='Publicado?')
    fLote = models.DateField(null=True, blank=True, verbose_name='Fecha de lote')
    category = models.ForeignKey(ProductsCategory, verbose_name='Categoria', blank=True, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")
 
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        
    def __str__(self):
        return self.name