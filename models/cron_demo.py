from odoo import models, fields
import logging


class DemoClass(models.Model):
   _name = 'cron.demo'
   student_name = fields.Char(string='Name of the student', required=True)
   def cron_demo_method(self):
       logging.basicConfig(filename="logs.log", filemode="w", format="%(name)s → %(levelname)s: %(message)s")
       logging.info("record updated")
