"""/*
 * HabsoluteState.py
 *
 * AUTOGENERATED FILE! ONLY EDIT IF YOU ARE A MACHINE!
 *
 * Created on: 2020-09-02 14:21:19.397132
 * Author: Dephy, Inc.
 *
 */
"""
from ctypes import Structure, c_int

class HabsoluteState(Structure):
	_pack_ = 1
	_fields_ = [
		("habsolute", c_int),
		("id", c_int),
		("state_time", c_int),
		("ank_ang", c_int),
		("ank_vel", c_int),
		("adc_0", c_int),
		("adc_1", c_int),
		("adc_2", c_int),
		("adc_3", c_int),
		("adc_4", c_int),
		("adc_5", c_int),
		("adc_6", c_int),
		("adc_7", c_int),
		("genVar_0", c_int),
		("genVar_1", c_int),
		("genVar_2", c_int),
		("genVar_3", c_int),
		("status", c_int),
		("SystemTime", c_int)]