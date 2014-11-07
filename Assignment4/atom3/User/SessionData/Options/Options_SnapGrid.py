"""
Options_SnapGrid.py

This file is automatically generated/modified when Options are configured.
If this file is corrupted/deleted, it will be re-created next time Options are configured.
So use the Options dialog instead of messing around in here :D

Format: [ initialValue, typeCode, stringPrompt, helpString ] 
See OptionDialog.py in UserInterface for typeCodes. 

Last modified on Mon Mar 15 18:38:12 2010 by Unamed
"""

def getOptionDictionary():

  optionDictionary = dict()

  optionDictionary['snapgrid enabled'] = [True, [0], 'Enable Snap Grid', '']
  optionDictionary['snap arrow node'] = [False, [0], 'Snap arrow node', '']
  optionDictionary['snap control points'] = [False, [0], 'Snap arrow control points', '']
  optionDictionary['gridsquare pixels'] = [20, [1], 'Grid square size in pixels', 'Snapping will occur at every X pixels square']
  optionDictionary['use gridsquare dots'] = [True, [0], 'Grid dots', 'Dot mode is much slower than using lines']
  optionDictionary['gridsquare width'] = [1, [1], 'Grid square width in pixels', '']
  optionDictionary['gridsquare color'] = ['#c8c8c8', [5, 'Choose Color'], 'Grid square color', '']
  optionDictionary['gridsquare subdivisions'] = [5, [1], 'Grid square subdivisions', 'Every X number of divisions, a subdivsion will be placed']
  optionDictionary['enable gridsquare subdivisions'] = [True, [0], 'Show subdivision lines', 'Makes it easier to visually measure distances']
  optionDictionary['gridsquare sudvision width'] = [1, [1], 'Grid square sudivision width', '']
  optionDictionary['gridsquare subdivision color'] = ['#e8e8e8', [5, 'Choose Color'], 'Grid square subdivision color', '']
  return optionDictionary