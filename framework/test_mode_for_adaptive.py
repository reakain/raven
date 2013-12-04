
''' from wikipedia: dx/dt = sigma*(y-x)  ; dy/dt = x*(rho-z)-y  dz/dt = x*y-beta*z  ; '''

import numpy as np
import copy
#import pylab as pyl
#import random
#import mpl_toolkits.mplot3d.axes3d as p3

def initialize(self,runInfoDict,inputFiles):
  self.SampledVars = None
  self.auxTime  = 0.0
  self.auxTime2 = 0.0
  self.temp     = 0.0
  self.tempTH   = 0.0
  self.m        = 5.0
  self.q        = 300.0  
  return 

def createNewInput(self,myInput,samplerType,**Kwargs):
  self.SampledVars = copy.deepcopy(Kwargs['SampledVars'])
  newInput = copy.deepcopy(myInput)
  newInput[0].updateInputValue('auxTime',self.SampledVars['auxTime'])
  try: newInput[0].updateInputValue('auxTime2',self.SampledVars['auxTime2'])
  except: pass
  newInput[0].updateInputValue('tempTH',self.SampledVars['tempTH'])
  return newInput

def readMoreXML(self,xmlNode):
  return None

def run(self,Input,jobHandler):
  self.auxTime = float(Input[0][0].extractValue('float','auxTime',varID=-1))
  try:self.auxTime2 = float(Input[0][0].extractValue('float','auxTime2',varID=-1))
  except:pass
  self.tempTH = float(Input[0][0].extractValue('float','tempTH',varID=-1))
  try:  self.temp = float(Input[0][0].extractValue('float','tempTH',varID=-1) + Input[0][0].extractValue('float','auxTime2',varID=-1) + Input[0][0].extractValue('float','auxTime',varID=-1)*self.m)
  except: self.temp = float(Input[0][0].extractValue('float','tempTH',varID=-1)  + Input[0][0].extractValue('float','auxTime',varID=-1)*self.m)
  return

