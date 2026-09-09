Minimum speed of galvo in is 0
Maximum speed of galvo is 30000



Buffer Mode Galvo Commands
 GT_PROSYS_U3_set_continous_mode_on();
 GT_PROSYS_U3_set_continous_mode_off();
 GT_PROSYS_U3_galvo_move_XY((int)x2, (int)y2, gspeed, XOFFSET, YOFFSET, THETA);
 Here X2: X-Coordinate, Y2: Y-Coordinate, XOFFSET: 
 GT_PROSYS_U3_buffer_pause();
 GT_PROSYS_U3_buffer_resume();
 GT_PROSYS_U3_buf_abort();
 GT_PROSYS_U3_buffer_ready();				//1:buffer not empty; 0:buffer empty


Normal Mode Commands
 GT_PROSYS_U3_galvo_run_status();  			//1: Galvo is running; 0: Galvo is stopped
 GT_PROSYS_U3_get_XY_Data(Int32* Data1, Int32* Data2);  // Data1: x-Coordinate; Data2: y-Coordinate
 GT_PROSYS_U3_Run_Galvo(Int16 val1); 			//1: To run galvo; 
 GT_PROSYS_U3_XY_Data(Int16 val1, UInt32 val2);		//val1:0-x axis,1-y axis; val2: Axis Cordinate
 GT_PROSYS_U3_galvo_move_XY((int)x2, (int)y2, gspeed, XOFFSET, YOFFSET, THETA);
 GT_PROSYS_U3_galvo_stop();				// Stop Galvo