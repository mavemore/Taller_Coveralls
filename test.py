# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import descuento_pension

class Test(unittest.TestCase):

	def test_pension_1(self):
		pensionInicial = 250
		nHermanos = 1
		padresExAlumnos = True
		promedioAcademico = 8.5
		pension = descuento_pension.calcularDescuentoPension(pensionInicial,nHermanos, padresExAlumnos, promedioAcademico)
		self.assertEqual(pension, 237.5)

if __name__ == '__main__':
	unittest.main()