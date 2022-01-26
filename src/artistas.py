# -*- coding:utf-8 -*-
'''
Created on 26 ene 2022

@author: willi
'''
import csv
from collections import namedtuple
from parsers import *
import statistics
from collections import Counter

Concierto= namedtuple('Concierto','artista, artistas_invitados, fecha, hora_apertura, hora_concierto, precio, aforo, admite_menores')

def lee_fichero(fichero):
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        res =[]
        for artista, artistas_invitados, fecha, hora_apertura, hora_concierto, precio, aforo, admite_menores in lector:
            tupla = Concierto(artista, artistas_invitados, parsea_fecha(fecha), parsea_hora(hora_apertura), parsea_hora(hora_concierto), float(precio), int(aforo), parsea_booleano(admite_menores))
            res.append(tupla)
    return res

def ejercicio1(registros,artista):
    return [t for t in registros if t.artista ==artista or artista in t.artistas_invitado]

def ejercicio2(registros,hora):
    res =[(t.artista,t.artistas_invitados,t.fecha) for t in registros if hora>t.hora_apertura and t.admite_menores == True]
    return sorted(res,key=lambda x:x[2])
def ejercicio3(registros, fecha):
    res = [t for t in registros if t.fecha>=fecha]
    minimo = min(res, key=lambda x:x.hora_apertura)
    return(minimo.artista,minimo.fecha)

def ejercicio4(registros,mes,a�o):
    res = [t for t in registros if t.fecha.year==a�o and t.fecha.month==mes]
    lista_ordenada = sorted(res, key=lambda x:x.fecha)
    lista_artistas =[]
    for t in lista_ordenada:
        if t.artista not in lista_artistas:
            lista_artistas.append(t.artista)
        for c in t.artistas_invitados:
            if c not in lista_artistas:
                lista_artistas.append(c)
    return lista_artistas

def ejercicio5(registros):
    artista = set()
    for c in registros:
        artista.add(c.artista)
        for a in c.artistas_invitados:
            artista.add(a)
    pago = []
    for t in artista:
        pago.append(t,calcula_pagos(registros,t))
    return max(pago, key = lambda x:x[1])
        
    
def calcula_pagos(registros,t):
    pago = 0
    for c in registros:
        cantidad = (c.aforo*c.precio)/3
        if t== c.artista:
            pago +=cantidad
        elif t in c.artista_invitado:
            pago += cantidad/len(c.artista_invitado)
    return pago
def ejercicio6(registros):
    dicc_precio = {}
    dicc_aforo={}
    dicc_num = {}
    for t in registros:
        clave = t.fecha.month+ "_"+ t.fecha.year
        if clave in dicc_precio:
            dicc_precio[clave] += t.precio
            dicc_aforo[clave] += t.aforo
            dicc_num[clave]+= 1
        else:
            dicc_precio[clave] = t.precio
            dicc_aforo[clave] = t.aforo
            dicc_num[clave]= 1
    res = {}
    for k in dicc_precio:
        res[k] = (dicc_precio[k]/dicc_num[k], dicc_aforo[k])
    return res
        
            
            
        
    

    
    
    
