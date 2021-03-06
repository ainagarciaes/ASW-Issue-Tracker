# Generated by Django 2.2.7 on 2019-11-05 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titol', models.CharField(max_length=200)),
                ('descripcio', models.TextField()),
                ('data_creacio', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.BooleanField()),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aswissues.Issue')),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aswissues.User')),
            ],
        ),
        migrations.AddField(
            model_name='issue',
            name='assignee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Assignee', to='aswissues.User'),
        ),
        migrations.AddField(
            model_name='issue',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Creator', to='aswissues.User'),
        ),
        migrations.AddField(
            model_name='issue',
            name='watchers',
            field=models.ManyToManyField(to='aswissues.User'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('data_creacio', models.DateField()),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aswissues.Issue')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aswissues.User')),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.FileField(upload_to='')),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aswissues.Issue')),
            ],
        ),
    ]
