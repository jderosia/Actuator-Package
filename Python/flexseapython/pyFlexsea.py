from ctypes import *
import os
import sys
import platform

global flexsea
initialized = False

# Opens the given serial port at the given index and looks for devices
def fxOpen(port, idx, baudRate):
	global flexsea
	flexsea.fxOpen( port.encode('utf-8') , idx, baudRate)

# Returns a boolean that indicates whether the port is open
def fxIsOpen(idx):
	global flexsea
	return flexsea.fxIsOpen(idx)

# Returns a list of device ids corresponding to connected devices
def fxGetDeviceIds():
	global flexsea
	n = 6
	l = [-1] * 6
	c_l, c_n = list_to_int_arr(l)
	flexsea.fxGetDeviceIds(c_l, c_n)
	asList = c_l[:n]
	asList = asList[: asList.index(-1) ]
	return asList

# Starts streaming data read commands and act pack commands for the given device
# params:
# 		devId 		: the id of the device to stream
# 		freq 		: the frequency to stream at
# 		shouldLog 	: whether to log data received from this device to a log file
# 		shouldAuto 	: whether to use autostreaming or manual streaming
# returns:
# 		c_bool value indicating whether the request was a success
def fxStartStreaming(devId, freq, shouldLog, shouldAuto):
	global flexsea
	return	flexsea.fxStartStreaming(devId, freq, shouldLog, shouldAuto)

# Stops streaming data read commands and act pack commands for the given device
# params:
# 		devId 		: the id of the device to stop streaming
# returns:
# 		c_bool value indicating whether the request was a success
def fxStopStreaming(devId):
	global flexsea
	return	flexsea.fxStopStreaming(devId)

# Sets the active stream variables for the given device
# Note: changing the stream variables during a logged stream has undefined behaviour
# params:
# 		devId 		: the id of the device to set fields for
# 		fieldIds 	: a list containing the fields to stream 
def fxSetStreamVariables(devId, fieldIds):
	global flexsea
	c_fi, c_n = list_to_int_arr(fieldIds)
	flexsea.fxSetStreamVariables(devId, c_fi, c_n)

# Reads the most recent data received from the device
# params:
# 		devId 		: the id of the device to read
# 		fieldIds 	: a list containing the fields to read 
# returns:
# 		a python list containing the values of the requested fields 
#		(in the order requested), or None for fields that errored
def fxReadDevice(devId, fieldIds):
	global flexsea
	n = len(fieldIds)	

	c_fieldIds, c_n = list_to_int_arr(fieldIds)
	c_successBools, c_n = list_to_bool_arr( [0] * n )

	result = flexsea.fxReadDevice(devId, c_fieldIds, c_successBools, c_n)
	valsAsList = [result[i] for i in range(n)]
	#valsAsList = result[:n]
	boolsAsList = c_successBools[:n]

	for i in range(0, n):
		if(boolsAsList[i] == 0):
			valsAsList[i] = None

	return valsAsList

# Sets the control mode for the given device
# params:
# 		devId 		: the id of the device 
# 		ctrlMode 	: the control mode to use [must be one of values provided in pyFlexsea_def.py]
def setControlMode(devId, ctrlMode):
	global flexsea
	flexsea.setControlMode(devId, int(ctrlMode))

# Sets the voltage setpoint for the given device
# params:
# 		devId 		: the id of the device 
# 		mV 			: the voltage to set in milliVolts
def setMotorVoltage(devId, mV):
	global flexsea
	flexsea.setMotorVoltage(devId, int(mV))

# Sets the current setpoint for the given device
# params:
# 		devId 		: the id of the device 
# 		cur			: the current to use as setpoint in milliAmps
def setMotorCurrent(devId, cur):
	global flexsea
	flexsea.setMotorCurrent(devId, int(cur))

# Sets the position setpoint for the given device
# params:
# 		devId 		: the id of the device 
# 		pos			: the absolute encoder position to use as setpoint
def setPosition(devId, pos):
	global flexsea
	flexsea.setPosition(devId, int(pos))

# Sets the PID controller gains for the given device
# params:
# 		devId 		: the id of the device 
# 		g0			: the proportional gain to set for the active setpoint
# 		g1			: the integral gain to set for the active setpoint
# 		g2		: the proportional gain to set for the underlying current controller (only relevant for impedance control)
# 		g3		: the integral gain to set for the underlying current controller (only relevant for impedance control)
def setGains(devId, g0, g1, g2, g3):
	global flexsea
	flexsea.setGains(devId, int(g0), int(g1), int(g2), int(g3))

# Sets the activation state for FSM2 on the given device
# params:
# 		devId 		: the id of the device 
# 		on			: whether to set the FSM on or off
def actPackFSM2(devId, on):
	global flexsea
	flexsea.actPackFSM2(devId, int(on))

# Tells the given device to run a find poles routine
# params:
# 		devId 		: the id of the device 
# 		block 		: whether to block for 60 seconds while the device runs the routine
def findPoles(devId, block):
	global flexsea
	flexsea.findPoles(devId, int(block))

# Loads the library from the c lib
def loadFlexsea():
	global flexsea
	#Init code:
	print('[pyFlexsea Module]\n')

	loadSucceeded  = False
	is_64bits = sys.maxsize > 2**32
	sysOS = platform.system().lower()
	dir_path = os.path.dirname(os.path.realpath(__file__))
	# we currently support Ubuntu and Raspbian so need to make sure we are pulling
	# in correct library depending on which version of linux
	linux_distro = platform.linux_distribution()[0]

	librarypath=""
	print(platform)
	if("win" in sysOS):
		lpath_base = os.path.join(dir_path,'../../fx_plan_stack/libs/windows')
		librarypath = os.path.join(lpath_base,'libfx_plan_stack.dll')
	elif("Ubuntu" in linux_distro):
		lpath_base = os.path.join(dir_path,'../../fx_plan_stack/libs/linux')
		librarypath = os.path.join(lpath_base,'libfx_plan_stack.so')
	else:
		# TODO: as of now we'll assume we're compiling for a raspberry Pi if it's not Ubuntu
		# or windows but we'll likely want to make OS library versions clearer
		lpath_base = os.path.join(dir_path,'../../fx_plan_stack/libs/raspberryPi')
		librarypath = os.path.join(lpath_base,'libfx_plan_stack.so')

	try:
		print("loading... " + librarypath)
		flexsea = cdll.LoadLibrary(librarypath)
	except OSError as arg:
		print( "\n\nThere was a problem loading the library\n {0}\n".format(arg))
	else:
		loadSucceeded  = True

	if(loadSucceeded  != True):
		return False

	print("Loaded!")
	initialized = True
	flexsea.fxSetup()
	# set arg types
	flexsea.fxOpen.argtypes = [c_char_p, c_int, c_int]
	flexsea.fxSetStreamVariables.restype = c_bool
	flexsea.fxStartStreaming.argtypes = [c_int, c_int, c_bool, c_int]
	flexsea.fxStopStreaming.argtypes = [c_int]
	flexsea.fxReadDevice.restype = POINTER(c_int)
	flexsea.getUserRead.restype = POINTER(c_int)
	flexsea.getUserWrite.restype = POINTER(c_int)
	flexsea.setControlMode.argtypes = [c_int, c_int]
	flexsea.setMotorVoltage.argtypes = [c_int, c_int]
	flexsea.setMotorCurrent.argtypes = [c_int, c_int]
	flexsea.fxClose.argtypes = [c_int]

	return True

def list_to_int_arr(l):
	c_arr = (c_int * len(l))(*l)
	c_len = c_int(len(l))
	return c_arr, c_len

def list_to_bool_arr(l):
	c_arr = (c_bool * len(l))(*l)
	c_len = c_int(len(l))
	return c_arr, c_len

def getUserRead():
	global flexsea
	result = flexsea.getUserRead()
	valAsList = [result[i] for i in range(6)]
	return valAsList

def getUserWrite():
	global flexsea
	result = flexsea.getUserWrite()
	valAsList = [result[i] for i in range(10)]
	return valAsList

def writeUser(devId,index, value):
	global flexsea
	flexsea.writeUser(devId,index,value)

def readUser(devId):
	global flexsea
	flexsea.readUser(devId)

# Takes in an iterable (example a list) and closes that port
def closePort(port):
	global flexsea
	flexsea.fxClose(port)

def cleanupPlanStack():
	global flexsea
	flexsea.fxCleanup()
