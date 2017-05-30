# -*- coding: utf-8 -*-

from odoo import models, fields, api

		
class PartnerAcicf(models.Model):
	_inherit = 'res.partner'

	
	cae1 = fields.Char('CAE Principal')
	dcae1 = fields.Char('Descritivo CAE Principal')
	cae2 = fields.Char('CAE Secundario')
	socio = fields.Boolean('Sócio da ACICF')
	
	hab = fields.Char('Habilitações Literárias')
	capital = fields.Float('% Capital Social')
	
	formajuridica = fields.Char('Forma Jurídica da Empresa')
	capsocial = fields.Float('Capital Social')
	dataconst = fields.Date('Data de Constituição')

	colab = fields.Integer('Número de Trabalhadores')	
	tipo_empresa = fields.Char('Dimensão da Empresa :: Rever Funcionalidade', compute='_type_define')


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
