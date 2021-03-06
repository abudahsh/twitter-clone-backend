# Generated by Django 2.1 on 2018-08-02 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=300)),
                ('media', models.ImageField(blank=True, null=True, upload_to='')),
                ('is_liked', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('tweet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tweets.Tweet')),
            ],
            bases=('tweets.tweet',),
        ),
        migrations.CreateModel(
            name='ReTweet',
            fields=[
                ('tweet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tweets.Tweet')),
            ],
            bases=('tweets.tweet',),
        ),
        migrations.AddField(
            model_name='tweet',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tweets', to='profiles.Profile'),
        ),
        migrations.AddField(
            model_name='retweet',
            name='origin_tweet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='retweets', to='tweets.Tweet'),
        ),
        migrations.AddField(
            model_name='reply',
            name='reply_on',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='tweets.Tweet', verbose_name='replies'),
        ),
    ]
