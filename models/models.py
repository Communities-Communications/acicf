# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
		
class PartnerAcicf(models.Model):
	_inherit = 'res.partner'

	
	cae1 = fields.Char('CAE Principal')
	dcae1 = fields.Char('Descritivo CAE Principal')
	cae2 = fields.Char('CAE Secundario')
	socio = fields.Boolean('Sócio da ACICF')
	
	hab = fields.Char('Habilitações Literárias')
	capital = fields.Float('% Capital Social')
	data_nasc = fields.Date('Data de Nascimento')
	idade = fields.Char(compute='_calculo_idade')
	
	formajuridica = fields.Char('Forma Jurídica da Empresa')
	capsocial = fields.Float('Capital Social')
	dataconst = fields.Date('Data de Constituição')

	colab = fields.Integer('Número de Trabalhadores')	
	tipo_empresa = fields.Char('Dimensão da Empresa :: Rever Funcionalidade', compute='_type_define')
	
#	def _calculo_idade(self):
#		days_in_year = 365.2425
#		age = int((date.today() - self.data_nasc).days / days_in_year)
#		return age

	@api.multi
	@api.depends('data_nasc')
	def _calculo_idade(self):
		for record in self:
			if record.data_nasc:
				record.idade = relativedelta(
					fields.Date.from_string(fields.Date.today()),
					fields.Date.from_string(record.data_nasc)).years
			else:
					record.idade = 0
	
# Esta função não está a funcionar rever mais tarde	
	@api.depends('colab')
	def _type_define(self):
#		if self.colab > 0 and self.colab <= 9:
#			self.tipo_empresa = 'micro'
			
#		if self.colab > 9 and self.colab < 50:
#			self.tipo_empresa = 'pequena'
				
#		if self.colab > 50 and self.colab < 100:
#			self.tipo_empresa = 'media'
		
#		if self.colab >= 101:
#			self.tipo_empresa = 'grande'
		return ()
