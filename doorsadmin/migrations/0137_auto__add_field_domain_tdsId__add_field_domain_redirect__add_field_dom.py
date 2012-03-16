# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Domain.tdsId'
        db.add_column('doorsadmin_domain', 'tdsId', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'Domain.redirect'
        db.add_column('doorsadmin_domain', 'redirect', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Domain.redirectType'
        db.add_column('doorsadmin_domain', 'redirectType', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['doorsadmin.RedirectType'], null=True, blank=True), keep_default=False)

        # Adding field 'Domain.redirectDelay'
        db.add_column('doorsadmin_domain', 'redirectDelay', self.gf('django.db.models.fields.IntegerField')(default=30, blank=True), keep_default=False)

        # Deleting field 'Doorway.redirect'
        db.delete_column('doorsadmin_doorway', 'redirect')

        # Deleting field 'Doorway.tdsId'
        db.delete_column('doorsadmin_doorway', 'tdsId')

        # Deleting field 'Doorway.redirectDelay'
        db.delete_column('doorsadmin_doorway', 'redirectDelay')

        # Deleting field 'Doorway.redirectType'
        db.delete_column('doorsadmin_doorway', 'redirectType_id')


    def backwards(self, orm):
        
        # Deleting field 'Domain.tdsId'
        db.delete_column('doorsadmin_domain', 'tdsId')

        # Deleting field 'Domain.redirect'
        db.delete_column('doorsadmin_domain', 'redirect')

        # Deleting field 'Domain.redirectType'
        db.delete_column('doorsadmin_domain', 'redirectType_id')

        # Deleting field 'Domain.redirectDelay'
        db.delete_column('doorsadmin_domain', 'redirectDelay')

        # Adding field 'Doorway.redirect'
        db.add_column('doorsadmin_doorway', 'redirect', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Doorway.tdsId'
        db.add_column('doorsadmin_doorway', 'tdsId', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'Doorway.redirectDelay'
        db.add_column('doorsadmin_doorway', 'redirectDelay', self.gf('django.db.models.fields.IntegerField')(default=30, blank=True), keep_default=False)

        # Adding field 'Doorway.redirectType'
        db.add_column('doorsadmin_doorway', 'redirectType', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['doorsadmin.RedirectType'], null=True, blank=True), keep_default=False)


    models = {
        'doorsadmin.agent': {
            'Meta': {'object_name': 'Agent'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'currentTask': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'dateAdded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'dateChanged': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'dateLastPing': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'host': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.Host']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interval': ('django.db.models.fields.IntegerField', [], {'default': '3', 'null': 'True'}),
            'lastError': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'params': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'remarks': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'stateSimple': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '50'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'doorsadmin.domain': {
            'Meta': {'object_name': 'Domain'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'autoSubdomains': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'backLinksCount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'backLinksCountDate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'bulkAddDomains': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'dateAdded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'dateChanged': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'dateExpires': ('django.db.models.fields.DateField', [], {'default': 'datetime.date(2013, 3, 16)', 'null': 'True', 'blank': 'True'}),
            'dateRegistered': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'group': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'host': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.Host']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexCount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'indexCountDate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'ipAddress': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.IPAddress']", 'null': 'True'}),
            'lastError': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'linkedDomains': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['doorsadmin.Domain']", 'null': 'True', 'blank': 'True'}),
            'makeSpam': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'nameServer1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'nameServer2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'net': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.Net']", 'null': 'True', 'blank': 'True'}),
            'niche': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.Niche']", 'null': 'True', 'blank': 'True'}),
            'redirect': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'redirectDelay': ('django.db.models.fields.IntegerField', [], {'default': '30', 'blank': 'True'}),
            'redirectType': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.RedirectType']", 'null': 'True', 'blank': 'True'}),
            'registrator': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'remarks': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'stateSimple': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '50'}),
            'tdsId': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trafficLastDay': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trafficLastMonth': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trafficLastYear': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'useOwnDNS': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'doorsadmin.doorlink': {
            'Meta': {'object_name': 'DoorLink'},
            'anchor': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000'}),
            'doorway': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.Doorway']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'makeSpam': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'spamTask': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.SpamTask']", 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000'})
        },
        'doorsadmin.doorway': {
            'Meta': {'object_name': 'Doorway'},
            'agent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.Agent']", 'null': 'True', 'blank': 'True'}),
            'dateAdded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'dateChanged': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.Domain']", 'null': 'True', 'blank': 'True'}),
            'domainFolder': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'domainSub': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'doorLinksCount': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywordsList': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'keywordsSet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.KeywordsSet']", 'null': 'True', 'blank': 'True'}),
            'lastError': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'makeSpam': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'netLinksList': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'niche': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.Niche']", 'null': 'True'}),
            'pagesCount': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'priority': ('django.db.models.fields.CharField', [], {'default': "'std'", 'max_length': '20'}),
            'remarks': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'runTime': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'spamLinksCount': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'stateManaged': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '50'}),
            'stateSimple': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '50'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.Template']", 'null': 'True', 'blank': 'True'}),
            'trafficLastDay': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trafficLastMonth': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trafficLastYear': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'doorsadmin.event': {
            'Meta': {'object_name': 'Event'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'info'", 'max_length': '50', 'blank': 'True'})
        },
        'doorsadmin.host': {
            'Meta': {'object_name': 'Host'},
            'company': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'controlPanelServerId': ('django.db.models.fields.IntegerField', [], {'default': '1', 'blank': 'True'}),
            'controlPanelType': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '50', 'blank': 'True'}),
            'controlPanelUrl': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'costPerMonth': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dateAdded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'dateChanged': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'diskSpace': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ftpLogin': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'ftpPassword': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'ftpPort': ('django.db.models.fields.IntegerField', [], {'default': '21', 'blank': 'True'}),
            'hostName': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastError': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'remarks': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'rootDocumentTemplate': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'stateSimple': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '50'}),
            'traffic': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'shared'", 'max_length': '50', 'blank': 'True'})
        },
        'doorsadmin.ipaddress': {
            'Meta': {'object_name': 'IPAddress'},
            'address': ('django.db.models.fields.IPAddressField', [], {'unique': 'True', 'max_length': '15'}),
            'dateAdded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'dateChanged': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'host': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.Host']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastError': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'remarks': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'stateSimple': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '50'})
        },
        'doorsadmin.keywordsset': {
            'Meta': {'object_name': 'KeywordsSet'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'dateAdded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'dateChanged': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'encoding': ('django.db.models.fields.CharField', [], {'default': "'cp1251'", 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywordsCount': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'lastError': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'localFolder': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'niche': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.Niche']", 'null': 'True'}),
            'remarks': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'stateSimple': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '50'})
        },
        'doorsadmin.net': {
            'Meta': {'object_name': 'Net'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'addDomainsNow': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'dateAdded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'dateChanged': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'dateEnd': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'dateStart': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'domainGroup': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'domainsPerDay': ('django.db.models.fields.IntegerField', [], {'default': '-1', 'null': 'True', 'blank': 'True'}),
            'doorsPerDay': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'generateDoorsNow': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywordsSet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.KeywordsSet']", 'null': 'True', 'blank': 'True'}),
            'lastError': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'makeSpam': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'maxPagesCount': ('django.db.models.fields.IntegerField', [], {'default': '900', 'null': 'True'}),
            'minPagesCount': ('django.db.models.fields.IntegerField', [], {'default': '500', 'null': 'True'}),
            'netPlan': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.NetPlan']", 'null': 'True', 'blank': 'True'}),
            'niche': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.Niche']", 'null': 'True'}),
            'redirect': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'redirectDelay': ('django.db.models.fields.IntegerField', [], {'default': '30', 'blank': 'True'}),
            'redirectType': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.RedirectType']", 'null': 'True', 'blank': 'True'}),
            'remarks': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'settings': ('django.db.models.fields.TextField', [], {'default': "'#gen'", 'blank': 'True'}),
            'stateSimple': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '50'}),
            'tdsId': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.Template']", 'null': 'True', 'blank': 'True'})
        },
        'doorsadmin.netplan': {
            'Meta': {'object_name': 'NetPlan'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'dateAdded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'dateChanged': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'dateEnd': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'dateStart': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'domainGroup': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'domainsPerDay': ('django.db.models.fields.IntegerField', [], {'default': '-1', 'null': 'True', 'blank': 'True'}),
            'doorsPerDay': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'generateNetsNow': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywordsSet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.KeywordsSet']", 'null': 'True', 'blank': 'True'}),
            'lastError': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'makeSpam': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'maxPagesCount': ('django.db.models.fields.IntegerField', [], {'default': '900', 'null': 'True'}),
            'minPagesCount': ('django.db.models.fields.IntegerField', [], {'default': '500', 'null': 'True'}),
            'netsCount': ('django.db.models.fields.IntegerField', [], {'default': '5', 'null': 'True', 'blank': 'True'}),
            'niche': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.Niche']", 'null': 'True'}),
            'redirect': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'redirectDelay': ('django.db.models.fields.IntegerField', [], {'default': '30', 'blank': 'True'}),
            'redirectType': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.RedirectType']", 'null': 'True', 'blank': 'True'}),
            'remarks': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'settings': ('django.db.models.fields.TextField', [], {'default': "'#gen'", 'blank': 'True'}),
            'stateSimple': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '50'}),
            'tdsId': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.Template']", 'null': 'True', 'blank': 'True'})
        },
        'doorsadmin.niche': {
            'Meta': {'object_name': 'Niche'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'dateAdded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'dateChanged': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lastError': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'redirect': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'redirectDelay': ('django.db.models.fields.IntegerField', [], {'default': '30', 'blank': 'True'}),
            'redirectType': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.RedirectType']", 'null': 'True', 'blank': 'True'}),
            'remarks': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'stateSimple': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '50'}),
            'stopwordsList': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'tdsId': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tdsSchemes': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'})
        },
        'doorsadmin.redirecttype': {
            'Meta': {'object_name': 'RedirectType'},
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'fileName': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'doorsadmin.report': {
            'Meta': {'object_name': 'Report'},
            'database': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'host': ('django.db.models.fields.CharField', [], {'default': "'localhost'", 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'sql': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'user': ('django.db.models.fields.CharField', [], {'default': "'admin'", 'max_length': '50'})
        },
        'doorsadmin.snippetsset': {
            'Meta': {'object_name': 'SnippetsSet'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'agent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.Agent']", 'null': 'True', 'blank': 'True'}),
            'dateAdded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'dateChanged': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'dateLastParsed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interval': ('django.db.models.fields.IntegerField', [], {'default': '100', 'null': 'True'}),
            'keywordsCount': ('django.db.models.fields.IntegerField', [], {'default': '200', 'null': 'True'}),
            'lastError': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'localFile': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'niche': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.Niche']", 'null': 'True'}),
            'phrasesCount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'priority': ('django.db.models.fields.CharField', [], {'default': "'std'", 'max_length': '20'}),
            'remarks': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'runTime': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'stateManaged': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '50'}),
            'stateSimple': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '50'})
        },
        'doorsadmin.spamtask': {
            'Meta': {'object_name': 'SpamTask'},
            'agent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.Agent']", 'null': 'True', 'blank': 'True'}),
            'dateAdded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'dateChanged': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'failsCount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'halfSuccessCount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastError': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'priority': ('django.db.models.fields.CharField', [], {'default': "'std'", 'max_length': '20'}),
            'profilesCount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'registeredAccountsCount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'remarks': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'runTime': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'stateManaged': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '50'}),
            'stateSimple': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '50'}),
            'successCount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'xrumerBaseSpam': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.XrumerBaseSpam']", 'null': 'True'})
        },
        'doorsadmin.template': {
            'Meta': {'object_name': 'Template'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'agent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.Agent']", 'null': 'True', 'blank': 'True'}),
            'dateAdded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'dateChanged': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastError': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'localFolder': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'niche': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.Niche']", 'null': 'True', 'blank': 'True'}),
            'remarks': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'stateSimple': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '50'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'classic'", 'max_length': '50'})
        },
        'doorsadmin.xrumerbasedoors': {
            'Meta': {'object_name': 'XrumerBaseDoors'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'agent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.Agent']", 'null': 'True', 'blank': 'True'}),
            'baseNumber': ('django.db.models.fields.IntegerField', [], {'default': '278', 'unique': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'creationType': ('django.db.models.fields.CharField', [], {'default': "'post'", 'max_length': '50'}),
            'dateAdded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'dateChanged': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'dateLastParsed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'emailAddress': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'failsCount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'halfSuccessCount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastError': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'linksCount': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'niche': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.Niche']", 'null': 'True'}),
            'nickName': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'priority': ('django.db.models.fields.CharField', [], {'default': "'std'", 'max_length': '20'}),
            'profilesCount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'realName': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'registerRun': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'registerRunDate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'registerRunTimeout': ('django.db.models.fields.IntegerField', [], {'default': '48', 'null': 'True', 'blank': 'True'}),
            'registeredAccountsCount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'remarks': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'runCount': ('django.db.models.fields.IntegerField', [], {'default': '100', 'null': 'True', 'blank': 'True'}),
            'runTime': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'snippetsSet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.SnippetsSet']", 'null': 'True', 'blank': 'True'}),
            'stateManaged': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '50'}),
            'stateSimple': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '50'}),
            'successCount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'xrumerBaseRaw': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.XrumerBaseRaw']", 'null': 'True'})
        },
        'doorsadmin.xrumerbaseprofiles': {
            'Meta': {'object_name': 'XrumerBaseProfiles'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'agent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.Agent']", 'null': 'True', 'blank': 'True'}),
            'baseNumber': ('django.db.models.fields.IntegerField', [], {'default': '278', 'unique': 'True'}),
            'creationType': ('django.db.models.fields.CharField', [], {'default': "'post'", 'max_length': '50'}),
            'dateAdded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'dateChanged': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'dateLastParsed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'emailAddress': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'failsCount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'halfSuccessCount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'homePage': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastError': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'linksCount': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'niche': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.Niche']", 'null': 'True'}),
            'nickName': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'priority': ('django.db.models.fields.CharField', [], {'default': "'std'", 'max_length': '20'}),
            'profilesCount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'realName': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'registerRun': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'registerRunDate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'registerRunTimeout': ('django.db.models.fields.IntegerField', [], {'default': '48', 'null': 'True', 'blank': 'True'}),
            'registeredAccountsCount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'remarks': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'runTime': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'signature': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'snippetsSet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.SnippetsSet']", 'null': 'True', 'blank': 'True'}),
            'stateManaged': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '50'}),
            'stateSimple': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '50'}),
            'successCount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'xrumerBaseRaw': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.XrumerBaseRaw']", 'null': 'True'})
        },
        'doorsadmin.xrumerbaseraw': {
            'Meta': {'object_name': 'XrumerBaseRaw'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'agent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.Agent']", 'null': 'True', 'blank': 'True'}),
            'baseNumber': ('django.db.models.fields.IntegerField', [], {'default': '278', 'unique': 'True'}),
            'creationType': ('django.db.models.fields.CharField', [], {'default': "'post'", 'max_length': '50'}),
            'dateAdded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'dateChanged': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'dateLastParsed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'emailAddress': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'failsCount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'halfSuccessCount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastError': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'linksCount': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'niche': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.Niche']", 'null': 'True'}),
            'nickName': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'parseParams': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'priority': ('django.db.models.fields.CharField', [], {'default': "'std'", 'max_length': '20'}),
            'profilesCount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'realName': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'registerRun': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'registerRunDate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'registerRunTimeout': ('django.db.models.fields.IntegerField', [], {'default': '48', 'null': 'True', 'blank': 'True'}),
            'registeredAccountsCount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'remarks': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'runTime': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'snippetsSet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.SnippetsSet']", 'null': 'True', 'blank': 'True'}),
            'stateManaged': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '50'}),
            'stateSimple': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '50'}),
            'successCount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'xrumerBaseRaw': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.XrumerBaseRaw']", 'null': 'True'})
        },
        'doorsadmin.xrumerbasespam': {
            'Meta': {'object_name': 'XrumerBaseSpam'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'agent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.Agent']", 'null': 'True', 'blank': 'True'}),
            'baseNumber': ('django.db.models.fields.IntegerField', [], {'default': '278', 'unique': 'True'}),
            'baseType': ('django.db.models.fields.CharField', [], {'default': "'RLinksList'", 'max_length': '50'}),
            'creationType': ('django.db.models.fields.CharField', [], {'default': "'post'", 'max_length': '50'}),
            'dateAdded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'dateChanged': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'dateLastParsed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'emailAddress': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'failsCount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'halfSuccessCount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastError': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'linksCount': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'niche': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.Niche']", 'null': 'True'}),
            'nickName': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'priority': ('django.db.models.fields.CharField', [], {'default': "'std'", 'max_length': '20'}),
            'profilesCount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'realName': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'registerRun': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'registerRunDate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'registerRunTimeout': ('django.db.models.fields.IntegerField', [], {'default': '48', 'null': 'True', 'blank': 'True'}),
            'registeredAccountsCount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'remarks': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'runTime': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'snippetsSet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.SnippetsSet']", 'null': 'True', 'blank': 'True'}),
            'spamTaskDomainLinksMax': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'spamTaskDomainLinksMin': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'spamTaskDomainsMax': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'spamTaskDomainsMin': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'stateManaged': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '50'}),
            'stateSimple': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '50'}),
            'successCount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'xrumerBaseRaw': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['doorsadmin.XrumerBaseRaw']", 'null': 'True'})
        }
    }

    complete_apps = ['doorsadmin']
