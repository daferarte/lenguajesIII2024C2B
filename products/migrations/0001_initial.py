# Generated by Django 4.2.6 on 2024-09-28 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ProductsCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150, verbose_name="Nombre")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Descripción"),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Creado"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now=True, verbose_name="Actualizado"),
                ),
            ],
            options={
                "verbose_name": "Categoria de producto",
                "verbose_name_plural": "Categorias de productos",
            },
        ),
        migrations.CreateModel(
            name="Products",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150, verbose_name="Nombre")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Descripción"),
                ),
                ("amount", models.CharField(max_length=150, verbose_name="Cantidad")),
                ("cost", models.CharField(max_length=150, verbose_name="Costo")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        default="null",
                        null=True,
                        upload_to="products",
                        verbose_name="Imagen",
                    ),
                ),
                (
                    "publisher",
                    models.BooleanField(default=True, verbose_name="Publicado?"),
                ),
                (
                    "fLote",
                    models.DateField(
                        blank=True, null=True, verbose_name="Fecha de lote"
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Creado"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now=True, verbose_name="Actualizado"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.productscategory",
                        verbose_name="Categoria",
                    ),
                ),
            ],
            options={
                "verbose_name": "Producto",
                "verbose_name_plural": "Productos",
            },
        ),
    ]
