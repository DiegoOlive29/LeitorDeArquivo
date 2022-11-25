# Generated by Django 4.1.3 on 2022-11-25 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Dado",
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
                (
                    "typeOp",
                    models.CharField(
                        choices=[
                            ("1", "Debito"),
                            ("2", "Boleto"),
                            ("3", "Finaciamento"),
                            ("4", "Credito"),
                            ("5", "Recebimento Emprestimo"),
                            ("6", "Vendas"),
                            ("7", "Recebimento Ted"),
                            ("8", "Recebimento Doc"),
                            ("9", "Aluguel"),
                        ],
                        max_length=22,
                    ),
                ),
                ("date", models.DateField(null=True)),
                ("value", models.CharField(max_length=10)),
                ("cpf", models.CharField(max_length=11)),
                ("card", models.CharField(max_length=12)),
                ("hour", models.CharField(max_length=6)),
                ("store_owner", models.CharField(max_length=14)),
                ("store_name", models.CharField(max_length=19)),
            ],
        ),
    ]
