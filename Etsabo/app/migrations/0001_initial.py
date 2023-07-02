# Generated by Django 4.1.7 on 2023-07-02 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'admin',
            },
        ),
        migrations.CreateModel(
            name='ConseilsSanitaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=90)),
                ('description', models.TextField(max_length=255)),
                ('img', models.CharField(max_length=90)),
            ],
            options={
                'db_table': 'conseils_sanitaire',
            },
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_consultation', models.DateField()),
                ('symptomes', models.CharField(max_length=500)),
                ('diagnostic', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'consultation',
            },
        ),
        migrations.CreateModel(
            name='Famille',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_famille', models.CharField(max_length=60)),
                ('adresse', models.CharField(max_length=80)),
                ('email', models.CharField(max_length=70)),
                ('password', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'famille',
            },
        ),
        migrations.CreateModel(
            name='Livraison',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_livraison', models.DateTimeField()),
                ('adresse', models.CharField(max_length=90)),
                ('description', models.TextField()),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('etat', models.IntegerField()),
            ],
            options={
                'db_table': 'livraison',
            },
        ),
        migrations.CreateModel(
            name='Medecin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('prenoms', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'medecin',
            },
        ),
        migrations.CreateModel(
            name='Medicament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'medicament',
            },
        ),
        migrations.CreateModel(
            name='Objet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_objet', models.CharField(max_length=70)),
                ('prix', models.FloatField()),
            ],
            options={
                'db_table': 'objet',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('prenoms', models.CharField(max_length=30)),
                ('adresse', models.CharField(max_length=30)),
                ('telephone', models.CharField(max_length=15)),
                ('sexe', models.IntegerField()),
                ('date_de_naissance', models.DateTimeField(blank=True, null=True)),
                ('email', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=40)),
                ('is_actif', models.IntegerField()),
                ('famille', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.famille')),
            ],
            options={
                'db_table': 'patient',
            },
        ),
        migrations.CreateModel(
            name='Pharmacie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_pharmacie', models.CharField(max_length=80)),
                ('long', models.FloatField()),
                ('lat', models.FloatField()),
            ],
            options={
                'db_table': 'pharmacie',
            },
        ),
        migrations.CreateModel(
            name='Publicite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('photo', models.CharField(max_length=30)),
                ('date_debut', models.DateTimeField(null=True)),
                ('date_fin', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'publicite',
            },
        ),
        migrations.CreateModel(
            name='Specialite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'specialite',
            },
        ),
        migrations.CreateModel(
            name='TypeAbonnement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_abonnement', models.CharField(max_length=70)),
                ('prix', models.FloatField()),
            ],
            options={
                'db_table': 'type_abonnement',
            },
        ),
        migrations.CreateModel(
            name='Rdv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_rdv', models.DateField()),
                ('heure_rdv', models.DateTimeField()),
                ('status', models.IntegerField()),
                ('medecin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.medecin')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.patient')),
            ],
            options={
                'db_table': 'rdv',
            },
        ),
        migrations.CreateModel(
            name='PhotoPatient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.CharField(max_length=70)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.patient')),
            ],
            options={
                'db_table': 'photo_patient',
            },
        ),
        migrations.CreateModel(
            name='PhotoObjet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.CharField(max_length=70)),
                ('objet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.objet')),
            ],
            options={
                'db_table': 'photo_objet',
            },
        ),
        migrations.CreateModel(
            name='PhotoMedecin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.CharField(max_length=70)),
                ('medecin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.medecin')),
            ],
            options={
                'db_table': 'photo_medecin',
            },
        ),
        migrations.CreateModel(
            name='Ordonnance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medocs', models.CharField(max_length=200)),
                ('prise', models.CharField(max_length=20)),
                ('remarque', models.CharField(max_length=200)),
                ('consultation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.consultation')),
            ],
            options={
                'db_table': 'ordonnance',
            },
        ),
        migrations.CreateModel(
            name='ObjetALivrer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.IntegerField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('livraison', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.livraison')),
                ('objet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.objet')),
            ],
            options={
                'db_table': 'objet_a_livrer',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField()),
                ('contenus', models.CharField(max_length=500)),
                ('date_envoie', models.DateField()),
                ('medecin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.medecin')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.patient')),
            ],
            options={
                'db_table': 'message',
            },
        ),
        migrations.AddField(
            model_name='medecin',
            name='specialite',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.specialite'),
        ),
        migrations.AddField(
            model_name='livraison',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.patient'),
        ),
        migrations.CreateModel(
            name='EtudeDocteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fianarana', models.CharField(max_length=90)),
                ('annee_debut', models.IntegerField()),
                ('annee_fin', models.IntegerField()),
                ('docteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.medecin')),
            ],
            options={
                'db_table': 'etude_docteur',
            },
        ),
        migrations.AddField(
            model_name='consultation',
            name='medecin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.medecin'),
        ),
        migrations.AddField(
            model_name='consultation',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.patient'),
        ),
        migrations.CreateModel(
            name='Abonnement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_fin', models.DateTimeField(blank=True, null=True)),
                ('reference', models.CharField(max_length=15)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.patient')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.typeabonnement')),
            ],
            options={
                'db_table': 'abonnement',
            },
        ),
    ]
