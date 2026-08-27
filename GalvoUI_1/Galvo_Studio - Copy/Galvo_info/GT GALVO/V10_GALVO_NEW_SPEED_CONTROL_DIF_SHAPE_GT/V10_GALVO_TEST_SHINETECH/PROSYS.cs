using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Runtime.InteropServices;




namespace V10_GALVO_TEST
{


    #region DLL

    class PROSYS
    {
        const string DLL_NAME = "gt5motion.dll";

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        unsafe public static extern Int32 GT_PROSYS_U3_Initialize(Int32* NumCards);

        //[DllImport("gt5motion.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        //unsafe public static extern Int32 GT_PROSYS_U3_Initialize(Int32* NumCards);

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        public static extern Int16 GT_PROSYS_U3_all_motion_status();

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        unsafe public static extern Int32 GT_PROSYS_U3_SetPass(Int32 Password);

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        public static extern void GT_PROSYS_U3_set_do_bit(Int16 BitNo, Int16 SetVal);

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        unsafe public static extern void GT_PROSYS_U3_Close();

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        public static extern void GT_PROSYS_U3_set_continous_mode_on();

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        public static extern void GT_PROSYS_U3_set_continous_mode_off();

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        public static extern Int16 GT_PROSYS_U3_start_tr_move(Int16 AxisNo, double Dist, double StrVel, double MaxVel, double Tacc, double Tdec);

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        public static extern Int16 GT_PROSYS_U3_start_ta_move(Int16 AxisNo, double Pos, double StrVel, double MaxVel, double Tacc, double Tdec);

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        unsafe public static extern Int16 GT_PROSYS_U3_start_ta_move_line2(Int16 CardNo, Int16* AxisArray, double PosX, double PosY, double StrVel, double MaxVel, double Tacc, double Tdec);

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        unsafe public static extern Int16 GT_PROSYS_U3_start_tr_move_line2(Int16 CardNo, Int16* AxisArray, double DistX, double DistY, double StrVel, double MaxVel, double Tacc, double Tdec);

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        unsafe public static extern Int16 GT_PROSYS_U3_start_a_arc2(Int16 CardNo, Int16* AxisArray, double Cx, double Cy, double Ex, double Ey, Int16 dir, double MaxVel);

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        public static extern Int16 GT_PROSYS_U3_buf_abort();

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        public static extern Int16 GT_PROSYS_U3_SetArcErr(Int32 ArcErr);

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        public static extern Int16 GT_PROSYS_U3_delay(double milliSec);

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        public static extern Int16 GT_PROSYS_U3_set_alm(Int16 AxisNo, Int16 alm_logic, Int16 alm_mode);

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        public static extern Int16 GT_PROSYS_U3_start_a_arc_xy(Int16 CardNo, double Cx, double Cy, double Ex, double Ey, Int16 dir, double MaxVel);

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        unsafe public static extern Int16 GT_PROSYS_U3_start_r_arc2(Int16 CardNo, Int16* AxisArray, double OffsetCx, double OffsetCy, double OffsetEx, double OffsetEy, Int16 dir, double MaxVel);

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        public static extern Int16 GT_PROSYS_U3_buffer_maxsize(); // Get buffer maximum size

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        public static extern void GT_PROSYS_U3_send_buffer(); // Send filled buffer for execution

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        public static extern Int16 GT_PROSYS_U3_buffer_pause();

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        public static extern Int16 GT_PROSYS_U3_sd_stop(Int16 AxisNo, double Tdec);

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        public static extern void GT_PROSYS_U3_set_do(int d_out);


        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        public static extern Int16 GT_PROSYS_U3_get_do();
        
        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        public static extern Int16 GT_PROSYS_U3_p_change(Int16 AxisNo, double NewPos);

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        public static extern Int16 GT_PROSYS_U3_get_di_bit(Int16 BitNo);

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        public static extern Int16 GT_PROSYS_U3_tv_move(Int16 AxisNo, double StrVel, double MaxVel, double Tacc, Int16 dir);


        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        public static extern Int16 GT_PROSYS_U3_set_command(Int16 AxisNo, Int32 cmd);

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        public static extern Int16 GT_PROSYS_U3_home_axis(Int16 AxisNo, double StrVel, double MaxVel, double Tacc, Int16 dir);

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        unsafe public static extern Int16 GT_PROSYS_U3_start_ta_move_line3(Int16 CardNo, Int16* AxisArray, double PosX, double PosY, double PosZ, double StrVel, double MaxVel, double Tacc, double Tdec);


        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        unsafe public static extern Int16 GT_PROSYS_U3_get_buf_cur_id(UInt32* CMDId);

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        unsafe public static extern Int16 GetFreeBRAMSpace();

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        unsafe public static extern Int16 GetFIFOCommands();

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        //public static extern Int16 GTPROS2WriteRegister(GTPROS2_HANDLE Handle, Int32 Offset, Int16 Value);
        public static extern void GT_PROSYS_U3_set_analog_do_bit(double MaxVal, double CrtVal, double FreqVal, Int16 bit);


        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        public static extern Int16 GT_PROSYS_U3_motion_done(Int16 AxNo);

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        unsafe public static extern Int16 GT_PROSYS_U3_get_command(Int16 AxNo, Int32* CMD);

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        unsafe public static extern Int16 GT_PROSYS_U3_get_card_srno();

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        unsafe public static extern Int16 GT_PROSYS_U3_get_all_command(Int32* xCMD, Int32* yCMD, Int32* zCMD, Int32* uCMD, Int32* vCMD);

        //[DllImport("gt5motion.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        //unsafe public static extern Int16 GT_PROSYS_U3_axis_move(Int16 rel_abs, Int16 Total_axis,Int16 CardNo,Int16* axisarray,double *positionarray,double strvel,double maxvel,double acc);
        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        unsafe public static extern Int16 GT_PROSYS_U3_axis_move(Int16 rel_abs, Int16 Total_axis, Int16* axisarray, double* positionarray, double strvel, double maxvel, double acc);

        //[DllImport("gt5motion.dll", CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        //unsafe public static extern Int16 GT_PROSYS_U3_SetPass(Int16 val1);                               

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        unsafe public static extern Int16 GT_PROSYS_U3_buffer_resume();

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        unsafe public static extern Int16 GT_PROSYS_U3_buffer_ready();

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        unsafe public static extern Int16 GT_PROSYS_U3_get_buffer_size();

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        unsafe public static extern Int16 GT_PROSYS_U3_XY_Data(Int16 val1, UInt32 val2);

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        unsafe public static extern Int16 GT_PROSYS_U3_Run_Galvo(Int16 val1);

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        unsafe public static extern Int16 GT_PROSYS_U3_get_XY_Data(Int32* Data1, Int32* Data2);

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        //unsafe public static extern void GT_PROSYS_U3_galvo_move_XY (Int32 val1, Int32 val2, Int32 val3);
        unsafe public static extern void GT_PROSYS_U3_galvo_move_XY(Int32 XPosn, Int32 YPosn, Int32 Speed, double XOffset, double YOffset, double Xtheta);

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        unsafe public static extern Int16 GT_PROSYS_U3_galvo_run_status();
        
        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        unsafe public static extern Int16 GT_PROSYS_U3_get_alm(Int16 AxNo);
        
        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        unsafe public static extern void GT_PROSYS_U3_galvo_stop();

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        unsafe public static extern void GT_PROSYS_U3_galvo_set_XY_Mode(Int32 Mode);

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        unsafe public static extern void GT_PROSYS_U3_set_galvo_delay (Int16 delay);

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        unsafe public static extern void GT_PROSYS_U3_buf_exclude_axis(Int16 AxisNo);

        [DllImport(DLL_NAME, CharSet = CharSet.Unicode, CallingConvention = CallingConvention.StdCall)]
        unsafe public static extern void GT_PROSYS_U3_buf_include_axis(Int16 AxisNo);
    }

    #endregion



}
