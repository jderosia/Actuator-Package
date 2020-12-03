"""/*
 * EB603State.py
 *
 * AUTOGENERATED FILE! ONLY EDIT IF YOU ARE A MACHINE!
 * CORE:228bd6fc3380919b08a364fd9f852465520f7ad9
 * BUILD:67854c9424418977b9a32838d8a74f14013eba38
 *
 *
 * Created on: 2020-12-02
 * Author: Dephy, Inc.
 *
 */
"""
from ctypes import Structure, c_int

class EB603State(Structure):
	_pack_ = 1
	_fields_ = [
		("rigid", c_int),
		("id", c_int),
		("state_time", c_int),
		("accelx", c_int),
		("accely", c_int),
		("accelz", c_int),
		("gyrox", c_int),
		("gyroy", c_int),
		("gyroz", c_int),
		("mot_ang", c_int),
		("mot_vel", c_int),
		("mot_acc", c_int),
		("mot_cur", c_int),
		("mot_volt", c_int),
		("batt_volt", c_int),
		("batt_curr", c_int),
		("temperature", c_int),
		("status_mn", c_int),
		("status_ex", c_int),
		("status_re", c_int),
		("genvar_0", c_int),
		("genvar_1", c_int),
		("genvar_2", c_int),
		("genvar_3", c_int),
		("genvar_4", c_int),
		("genvar_5", c_int),
		("genvar_6", c_int),
		("genvar_7", c_int),
		("genvar_8", c_int),
		("genvar_9", c_int),
		("ank_ang", c_int),
		("ank_vel", c_int),
		("shank_ang", c_int),
		("shank_vel", c_int),
		("global_shank_ang", c_int),
		("ank_pos_x", c_int),
		("ank_pos_y", c_int),
		("ank_pos_z", c_int),
		("ank_linear_vel_x", c_int),
		("ank_linear_vel_y", c_int),
		("ank_linear_vel_z", c_int),
		("mot_from_ank", c_int),
		("ank_from_mot", c_int),
		("trans_ratio", c_int),
		("ank_torque", c_int),
		("peak_ank_torque", c_int),
		("step_energy", c_int),
		("step_time", c_int),
		("gait_state", c_int),
		("intermediate_state", c_int),
		("movement", c_int),
		("speed", c_int),
		("incline", c_int),
		("SystemTime", c_int)]