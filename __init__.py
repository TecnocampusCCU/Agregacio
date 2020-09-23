# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Agregacio
                                 A QGIS plugin
 Aquest plugin permet fer agregacions espaciasl i per atributs
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-09-23
        copyright            : (C) 2020 by Josep Lopez Xarbau
        email                : jlopez@tecnocampus.cat
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Agregacio class from file Agregacio.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Agregacio import Agregacio
    return Agregacio(iface)
