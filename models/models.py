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
	ies_id = fields.Many2one('res.partner.ies', 'IES')
	
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



class InfoIESAcicf(models.Model):
	_name = 'res.partner.ies'
	
	
	year = fields.Char('Anos de Actividade')
	total_assets = fields.Float('Total de Ativos')
	shareholders_funds = fields.Float('Fundos de Acionistas')
	number_of_employees = fields.Float('Número de Empregados')
	turnover = fields.Float('Volume de Negócios')
	sales = fields.Float('Vendas')
	costs_of_goods_sold = fields.Float('Custos de Bens Vendidos')
	gross_profit = fields.Float('Rendimento Bruto')
	other_operating_expenses = fields.Float('Outras despesas de operação')
	financial_profit = fields.Float('Lucro')
	financial_revenue = fields.Float('Receita')
	financial_expenses = fields.Float('Despesas')
	profit_before_tax = fields.Float('Rendimento Antes de Impostos')
	taxation = fields.Float('Tributação')
	profit_after_tax = fields.Float('Rendimento Depois do Imposto')
	profit_for_period = fields.Float('Lucro por período')
	material_costs = fields.Float('Custos de Materiais')
	costs_of_employees = fields.Float('Custos dos Empregados')
	depreciation = fields.Float('Depreciação')
	cash_flow = fields.Float('Fluxo de Caixa')
	added_value = fields.Float('Valor Acrescentado')
	
	



