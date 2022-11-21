#ifndef MD20_STRUCT_H
#define MD20_STRUCT_H

///
/// \file md20_struct.h
///
/// \brief AUTOGENERATED FILE! ONLY EDIT IF YOU ARE A MACHINE!
///
/// \core a05344cba0bfa98a1af4812a2da598d452d87249
///
/// \build 2f821977dd44a7d9ee9e4428a73f788ad506a233
///
/// \date 2022-07-22 16:12:39
///
/// \author Dephy, Inc.

#include "MD20_device_spec.h"
#include <stdio.h>
#include <time.h>
#include <string.h>
#include <stdint.h>
#include <stdbool.h>

#define MD20_SYSTEM_TIME_POS 55
#define MD20_STRUCT_DEVICE_FIELD_COUNT 56
#define MD20_LABEL_MAX_CHAR_LENGTH 19

/// This is The Device fields * 10 + deviceField + 1. Ten is the max string length of 2^32 in
/// decimal separated from commas
#define MD20_DATA_STRING_LENGTH 617

#ifdef __cplusplus
extern "C"
{
#endif

#pragma pack(1)

struct MD20State
{
	int rigid;
	int id;
	int state_time;
	int accelx;
	int accely;
	int accelz;
	int gyrox;
	int gyroy;
	int gyroz;
	int mot_ang;
	int mot_vel;
	int mot_acc;
	int mot_cur;
	int mot_volt;
	int batt_volt;
	int batt_curr;
	int temperature;
	int status_mn;
	int status_ex;
	int status_re;
	int genvar_0;
	int genvar_1;
	int genvar_2;
	int genvar_3;
	int genvar_4;
	int genvar_5;
	int genvar_6;
	int genvar_7;
	int genvar_8;
	int genvar_9;
	int genvar_10;
	int genvar_11;
	int genvar_12;
	int genvar_13;
	int genvar_14;
	int ank_ang;
	int ank_vel;
	int shank_ang;
	int shank_vel;
	int global_shank_ang;
	int ank_pos_x;
	int ank_pos_y;
	int ank_pos_z;
	int ank_linear_vel_x;
	int ank_linear_vel_y;
	int ank_linear_vel_z;
	int mot_from_ank;
	int ank_from_mot;
	int trans_ratio;
	int ank_torque;
	int step_count;
	int step_time;
	int gait_state;
	int intermediate_state;
	int movement;
	int systemTime; /// System time
};

#pragma pack()

///
/// \brief Assigns the data in the buffer to the correct struct parameters
///
/// \param MD20 is the struct with the data to be set
///
/// \param _deviceStateBuffer is the buffer containing the data to be assigned to the struct
///
/// \param systemStartTime the time the system started. If unknown, use 0.
///
void MD20SetData(struct MD20State *md20, const uint32_t _deviceStateBuffer[], int systemStartTime);

///
/// \brief takes all data and places it into single, comma separated string
///
/// \param MD20 is the struct with the data to be placed in the string
///
/// \param dataString is where the new string wll be placed
///
void MD20DataToString(struct MD20State *md20, char dataString[MD20_DATA_STRING_LENGTH]);

///
/// \brief retrieves the string equivalent of all parameter names
///
/// \param labels is the array of labels containing the parameter names
///
void MD20GetLabels(char labels[MD20_STRUCT_DEVICE_FIELD_COUNT][MD20_LABEL_MAX_CHAR_LENGTH]);

///
/// \brief retrieves the string equivalent of parameter names starting with state time.
/// Parameters prior to state time, such as id, are not included.
///
/// \param labels is the array of labels containing the parameter names
///
int MD20GetLabelsForLog(char labels[MD20_STRUCT_DEVICE_FIELD_COUNT][MD20_LABEL_MAX_CHAR_LENGTH]);

///
/// \brief Places data from struct into an array.
///
/// \param md20 the data to be converted to an array
///
/// \param md20DataArray the array in which to place the data
///
void MD20StructToDataArray(struct MD20State md20, int32_t md20DataArray[MD20_STRUCT_DEVICE_FIELD_COUNT]);

///
/// \brief Get data based on data position from device communication.
///
/// \param md20 the data to access
///
/// \param dataPosition the position of data to access
///
/// \param dataValid return false if requested data position is invalid
///
int GetMD20DataByDataPosition( struct MD20State md20, int dataPosition);

#ifdef __cplusplus
} //extern "C"
#endif

#endif //MD20_STRUCT_H
