# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CityGuideArticle'
        db.create_table(u'prime_cityguidearticle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('neighborhood', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prime.Neighborhood'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('lead_photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('option', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('body', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'prime', ['CityGuideArticle'])

        # Adding model 'Neighborhood'
        db.create_table(u'prime_neighborhood', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lead_photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('intro_body', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=128)),
        ))
        db.send_create_signal(u'prime', ['Neighborhood'])

        # Adding model 'RecipeTag'
        db.create_table(u'prime_recipetag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal(u'prime', ['RecipeTag'])

        # Adding model 'DIYarticle'
        db.create_table(u'prime_diyarticle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=128)),
            ('issue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prime.Issue'], null=True, blank=True)),
            ('lead_photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('teaser', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('body', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('redirect', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('position', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal(u'prime', ['DIYarticle'])

        # Adding M2M table for field author on 'DIYarticle'
        m2m_table_name = db.shorten_name(u'prime_diyarticle_author')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('diyarticle', models.ForeignKey(orm[u'prime.diyarticle'], null=False)),
            ('author', models.ForeignKey(orm[u'main.author'], null=False))
        ))
        db.create_unique(m2m_table_name, ['diyarticle_id', 'author_id'])

        # Adding M2M table for field tag on 'DIYarticle'
        m2m_table_name = db.shorten_name(u'prime_diyarticle_tag')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('diyarticle', models.ForeignKey(orm[u'prime.diyarticle'], null=False)),
            ('diytag', models.ForeignKey(orm[u'prime.diytag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['diyarticle_id', 'diytag_id'])

        # Adding model 'DIYTag'
        db.create_table(u'prime_diytag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal(u'prime', ['DIYTag'])

        # Adding field 'Recipe.issue'
        db.add_column(u'prime_recipe', 'issue',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prime.Issue'], null=True, blank=True),
                      keep_default=False)

        # Adding M2M table for field tag on 'Recipe'
        m2m_table_name = db.shorten_name(u'prime_recipe_tag')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipe', models.ForeignKey(orm[u'prime.recipe'], null=False)),
            ('recipetag', models.ForeignKey(orm[u'prime.recipetag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['recipe_id', 'recipetag_id'])


        # Changing field 'Recipe.teaser'
        db.alter_column(u'prime_recipe', 'teaser', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):
        # Deleting model 'CityGuideArticle'
        db.delete_table(u'prime_cityguidearticle')

        # Deleting model 'Neighborhood'
        db.delete_table(u'prime_neighborhood')

        # Deleting model 'RecipeTag'
        db.delete_table(u'prime_recipetag')

        # Deleting model 'DIYarticle'
        db.delete_table(u'prime_diyarticle')

        # Removing M2M table for field author on 'DIYarticle'
        db.delete_table(db.shorten_name(u'prime_diyarticle_author'))

        # Removing M2M table for field tag on 'DIYarticle'
        db.delete_table(db.shorten_name(u'prime_diyarticle_tag'))

        # Deleting model 'DIYTag'
        db.delete_table(u'prime_diytag')

        # Deleting field 'Recipe.issue'
        db.delete_column(u'prime_recipe', 'issue_id')

        # Removing M2M table for field tag on 'Recipe'
        db.delete_table(db.shorten_name(u'prime_recipe_tag'))


        # Changing field 'Recipe.teaser'
        db.alter_column(u'prime_recipe', 'teaser', self.gf('django.db.models.fields.CharField')(max_length=200))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'main.author': {
            'Meta': {'object_name': 'Author'},
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'mug': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'organization': ('django.db.models.fields.CharField', [], {'default': "'Daily Bruin'", 'max_length': '32', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'prime.article': {
            'Meta': {'object_name': 'Article'},
            'author': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['main.Author']", 'symmetrical': 'False'}),
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['prime.Issue']", 'null': 'True', 'blank': 'True'}),
            'lead_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'position': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'redirect': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128'}),
            'teaser': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'prime.cityguidearticle': {
            'Meta': {'object_name': 'CityGuideArticle'},
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lead_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'neighborhood': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prime.Neighborhood']"}),
            'option': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'prime.diyarticle': {
            'Meta': {'object_name': 'DIYarticle'},
            'author': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['main.Author']", 'symmetrical': 'False'}),
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prime.Issue']", 'null': 'True', 'blank': 'True'}),
            'lead_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'position': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'redirect': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128'}),
            'tag': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['prime.DIYTag']", 'symmetrical': 'False'}),
            'teaser': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'prime.diytag': {
            'Meta': {'object_name': 'DIYTag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'prime.image': {
            'Meta': {'object_name': 'Image'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Author']", 'null': 'True', 'blank': 'True'}),
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['prime.Issue']", 'null': 'True', 'blank': 'True'})
        },
        u'prime.issue': {
            'Meta': {'ordering': "['release_date']", 'object_name': 'Issue'},
            'header_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'release_date': ('django.db.models.fields.DateField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '32'})
        },
        u'prime.neighborhood': {
            'Meta': {'object_name': 'Neighborhood'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intro_body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'lead_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'prime.pdf': {
            'Meta': {'object_name': 'PDF'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'issue': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['prime.Issue']", 'unique': 'True'}),
            'pdf': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        u'prime.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'author': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['main.Author']", 'symmetrical': 'False'}),
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prime.Issue']", 'null': 'True', 'blank': 'True'}),
            'lead_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'position': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'redirect': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128'}),
            'tag': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['prime.RecipeTag']", 'symmetrical': 'False'}),
            'teaser': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'prime.recipetag': {
            'Meta': {'object_name': 'RecipeTag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['prime']