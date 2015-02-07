__author__ = 'Marcelino'

import xbmc
import os
import sys
import xbmcaddon
import xbmcgui

PLUGIN_DATA_PATH = xbmc.translatePath(os.path.join("special://profile/addon_data","plugin.program.advanced.launcher"))
BASE_PATH = xbmc.translatePath(os.path.join("special://","profile"))
HOME_PATH = xbmc.translatePath(os.path.join("special://","home"))
FAVOURITES_PATH = xbmc.translatePath( 'special://profile/favourites.xml' )
ADDONS_PATH = xbmc.translatePath(os.path.join(HOME_PATH,"addons"))
CURRENT_ADDON_PATH = xbmc.translatePath(os.path.join(ADDONS_PATH,"service.cecanyway"))
RESOURCES_PATH = xbmc.translatePath(os.path.join(CURRENT_ADDON_PATH,"Resources"))
CECANYWAY_PATH = xbmc.translatePath(os.path.join(RESOURCES_PATH,"cecanyway"))

arguments = "-d -f cecanyway.conf"

os.system("chmod +x \"%s\"" % CECANYWAY_PATH)
os.system("\"%s\" %s " % (CECANYWAY_PATH, arguments))
