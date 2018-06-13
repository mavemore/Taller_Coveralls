# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def calcularDescuentoPension(pensionInicial,nHermanos, padresExAlumnos, promedioAcademico):
	pension = pensionInicial
	if nHermanos>=0 and nHermanos<2:
		if padresExAlumnos:
			pension*=0.95
	elif nHermanos>=2 and nHermanos<4:
		descuentoHermanos = nHermanos*0.1
		descuentoAcademico = 0.0
		if promedioAcademico>8.0:
			descuentoAcademico = 0.15
		pension*=(1-descuentoHermanos-descuentoAcademico)
	else:
		pension*=0.5	
	return pension
