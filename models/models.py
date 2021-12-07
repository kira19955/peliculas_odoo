# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging 

logger = logging.getLogger(__name__)

class  Presupuesto(models.Model):
    _name = 'presupuesto'
    _inherit = ['image.mixin']

    name = fields.Char(string="Pelicula")
    fch_estreno = fields.Date(string="Fecha de estreno")
    clasificacion = fields.Selection(selection=[('g', 'G'),
                                               ('pg', 'PG'),
                                               ('pg-13', 'PG-13'),
                                               ('r', 'R'),
                                               ('nc-17', 'NC-17')
                                               ], string="Clasificacion")
    puntuacion = fields.Integer(string="Puntuacion", related="puntuacion2")
    active = fields.Boolean(string="Activo", default=True)
    director_id = fields.Many2one(comodel_name="res.partner", string="Director")
    generos_ids = fields.Many2many(comodel_name="genero", string="Genero")
    vista_general = fields.Text(string="Descripcion")
    link_trailer = fields.Char(string="Link Trailer")
    es_libro = fields.Boolean(string="Version Libro")
    libro = fields.Binary(string="Libro")
    puntuacion2 = fields.Integer(string="Puntuacion")
    libro_file = fields.Char(string="Nombre del libro")
    categoria_director_id = fields.Many2one(comodel_name="res.partner.category", string="Categoria Director", default=lambda self: self.env['res.partner.category'].search([('name', '=', 'Director')]))
    state = fields.Selection(selection=[('borrador', 'Borrador'),
                                        ('aprobado', 'Aprobado'),
                                        ('cancelado', 'Cancelado')],
                             default="borrador", string="Estados", copy=False)

    def aprobar_presupuesto(self):
        self.state = 'aprobado'


    def cancelar_presupuesto(self):
        self.state = 'cancelado'


