using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Diagnostics;





namespace V10_GALVO_TEST
{
    public partial class Form1 : Form
    {
        MicroLibrary.MicroStopwatch microSW = new MicroLibrary.MicroStopwatch();
        MicroLibrary.MicroStopwatch microSW1 = new MicroLibrary.MicroStopwatch();
        MicroLibrary.MicroStopwatch microSW2 = new MicroLibrary.MicroStopwatch();
        MicroLibrary.MicroStopwatch microSW3 = new MicroLibrary.MicroStopwatch();
        int gspeed = 100000;
        int XOFFSET = 0;
        int YOFFSET = 0;
        double THETA = 0;
        double THETA1 = 0;
        //int YTHETA = 0;
        int XORIGIN = 32767;
        int YORIGIN = 32767;
        bool feven = true;
        Graphics gr;
        Bitmap bm;
        uint X1 = 0, Y1 = 0, X2 = 40000, Y2 =30000;
        float New_Cx, New_Cy;
        float Pre_Cx = 319.99F;
        float Pre_Cy = 250.17F;
        bool once = false;
        bool bstop = true;
        bool buff_ = false;
       public Form1()
        {
             
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            int Card = 0;
            int alam = 5;
            int PASS_rET = 5;
           // #region Graphics

            bm = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            gr = Graphics.FromImage(bm);
            //gr.DrawArc(Pens.Yellow, pictureBox1.Width / 2 - Int_R, pictureBox1.Height / 2 - Int_R, Int_R * 2, Int_R * 2, 0, 360);
            //gr.DrawLine(Pens.Black, pictureBox1.Width / 2 - 5, pictureBox1.Height / 2, pictureBox1.Width / 2 + 5, pictureBox1.Height / 2);
            //gr.DrawLine(Pens.Black, pictureBox1.Width / 2, pictureBox1.Height / 2 - 5, pictureBox1.Width / 2, pictureBox1.Height / 2 + 5);
            //gr.DrawLine(Pens.Black, pictureBox1.Width / 2, 0, pictureBox1.Width / 2, pictureBox1.Height);
            //gr.DrawLine(Pens.Black, 0, pictureBox1.Height / 2, pictureBox1.Width, pictureBox1.Height / 2);
            //pictureBox1.Image = bm;
            unsafe
            {

                PASS_rET = PROSYS.GT_PROSYS_U3_SetPass(/*11593*/12242);
               
                PROSYS.GT_PROSYS_U3_Initialize(&Card);
                delay_ms(1000);
                PROSYS.GT_PROSYS_U3_XY_Data(0, 0);
                PROSYS.GT_PROSYS_U3_XY_Data(1, 0);
                PROSYS.GT_PROSYS_U3_Run_Galvo(1);
                alam=PROSYS.GT_PROSYS_U3_get_alm(0);
                alam=PROSYS.GT_PROSYS_U3_get_alm(1);
                alam=PROSYS.GT_PROSYS_U3_get_alm(2);
                alam = PROSYS.GT_PROSYS_U3_get_alm(3);
                alam = PROSYS.GT_PROSYS_U3_get_alm(4);
            }
          Position_timer.Enabled = true;
        }

        private void Button4_Click(object sender, EventArgs e)
        {
            PROSYS.GT_PROSYS_U3_XY_Data(0, UInt32.Parse(TbGalvoX.Text));
            PROSYS.GT_PROSYS_U3_XY_Data(1, UInt32.Parse(TbGalvoY.Text));
            PROSYS.GT_PROSYS_U3_Run_Galvo(1);

        }

       

        void delay_us(int us)
        {
            MicroLibrary.MicroStopwatch microSW = new MicroLibrary.MicroStopwatch();
            microSW.Start();
            while (microSW.ElapsedMicroseconds < us)
            {
                Application.DoEvents();
            }
        }
        void delay_ms(int ms)
        {
            Stopwatch sw = new Stopwatch();
            sw.Start();
            while (sw.ElapsedMilliseconds < ms)
            {
                Application.DoEvents();
            }
        }
        
        void Run_Galvo(UInt32 x, UInt32 y)
        {
            PROSYS.GT_PROSYS_U3_XY_Data(0, x);
            PROSYS.GT_PROSYS_U3_XY_Data(1, y);
            PROSYS.GT_PROSYS_U3_Run_Galvo(1);
        }

       

        private void button3_Click(object sender, EventArgs e)
        {
            gspeed = Convert.ToInt32(txtSpeed.Text);
            X1 = (uint)Convert.ToInt32(txtLineX1.Text);
            Y1 = (uint)Convert.ToInt32(txtLineY1.Text);
            X2 = (uint)Convert.ToInt32(txtLineX2.Text);
            Y2 = (uint)Convert.ToInt32(txtLineY2.Text);
            
        }


        private void button6_Click(object sender, EventArgs e)
        {
            
            uint L1;
            L1 = (uint)Convert.ToInt32(txtCircleR.Text);
            //L1 = (uint)Convert.ToInt32(txtRSLength.Text);
                         Int16[] axis_array = new Int16[3];
            //Int16 Motion;
            //double[] position_array = new double[5];
            //Int16 rel_abs ;
            //Int16 Total_axis_to_move = 1;
            //double low_speed ;
            //double max_speed ;
            //double acc_time  ;
            //                rel_abs =1;
            //    axis_array[0] = 0;
            //    position_array[0] = 100;
            //    low_speed = 10000;
            //    max_speed = 50000;
            //    acc_time = 0.1;
            
            //unsafe
            //{
            //    fixed (double* position_ref = position_array) fixed (Int16* axis_ref = axis_array) PROSYS.GT_PROSYS_U3_axis_move(rel_abs, Total_axis_to_move, axis_ref, position_ref, low_speed, max_speed, acc_time);
            //}
            for (UInt16 loop = 0; loop <= 10; loop++)
            {
                


            //    //------------irregular shape Normal Mode--------------------//
            //    //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)0, (int)40000, gspeed, XOFFSET, YOFFSET,  THETA);
            //    //while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
            //    //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)0, (int)50000, gspeed, XOFFSET, YOFFSET,  THETA);
            //    //while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
            //    //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)20000, (int)50000, gspeed, XOFFSET, YOFFSET,  THETA);
            //    //while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
            //    //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)23000, (int)54000, gspeed, XOFFSET, YOFFSET,  THETA);
            //    //while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
            //    //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)43000, (int)54000, gspeed, XOFFSET, YOFFSET,  THETA);
            //    //while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
            //    //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)43000, (int)50000, gspeed, XOFFSET, YOFFSET,  THETA);
            //    //while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
            //    //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)40000, (int)46000, gspeed, XOFFSET, YOFFSET,  THETA);
            //    //while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
            //    //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)20000, (int)46000, gspeed, XOFFSET, YOFFSET,  THETA);
            //    //while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
            //    //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)20000, (int)40000, gspeed, XOFFSET, YOFFSET,  THETA);
            //    //while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;


            //    //------------irregular shape Buffer Mode--------------------//
            //    //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)0, (int)40000, gspeed, XOFFSET, YOFFSET, THETA);
            //    ////while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
            //    //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)0, (int)50000, gspeed, XOFFSET, YOFFSET, THETA);
            //    ////while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
            //    //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)20000, (int)50000, gspeed, XOFFSET, YOFFSET, THETA);
            //    ////while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
            //    //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)23000, (int)54000, gspeed, XOFFSET, YOFFSET, THETA);
            //    //// while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
            //    //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)43000, (int)54000, gspeed, XOFFSET, YOFFSET, THETA);
            //    ////while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
            //    //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)43000, (int)50000, gspeed, XOFFSET, YOFFSET, THETA);
            //    ////while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
            //    //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)40000, (int)46000, gspeed, XOFFSET, YOFFSET, THETA);
            //    ////while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
            //    //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)20000, (int)46000, gspeed, XOFFSET, YOFFSET, THETA);
            //    ////while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
            //    //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)20000, (int)40000, gspeed, XOFFSET, YOFFSET, THETA);
            //    ////while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;

            //    //------------------------------- Square --------------------------------------//

                PROSYS.GT_PROSYS_U3_galvo_move_XY((int)10000, (int)10000, gspeed, XOFFSET, YOFFSET, THETA); //delay_ms(10);
                //while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
                PROSYS.GT_PROSYS_U3_galvo_move_XY((int)10000, (int)L1 + 10000, gspeed, XOFFSET, YOFFSET, THETA); //delay_ms(10);
                // while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
                PROSYS.GT_PROSYS_U3_galvo_move_XY((int)L1 + 10000, (int)L1 + 10000, gspeed, XOFFSET, YOFFSET, THETA);// delay_ms(10);
                // while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
                PROSYS.GT_PROSYS_U3_galvo_move_XY((int)L1 + 10000, (int)0 + 10000, gspeed, XOFFSET, YOFFSET, THETA); //delay_ms(10);
                //while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;

            //    //-------------------------------  R - Square --------------------------------------//
            //   // PROSYS.GT_PROSYS_U3_galvo_move_XY((int)0, (int)(L1 / 2) , gspeed, XOFFSET, YOFFSET, THETA);
            //   // //while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
            //   // PROSYS.GT_PROSYS_U3_galvo_move_XY((int)(L1 / 2) , (int)L1, gspeed, XOFFSET, YOFFSET, THETA);
            //   //// while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
            //   // PROSYS.GT_PROSYS_U3_galvo_move_XY((int)L1 , (int)(L1 / 2) , gspeed, XOFFSET, YOFFSET, THETA);
            //   // //while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
            //   // PROSYS.GT_PROSYS_U3_galvo_move_XY((int)(L1 / 2) , (int)0, gspeed, XOFFSET, YOFFSET, THETA);
            //   // //while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;


            //    //------------------------------- NEW Square --------------------------------------//
            //    PROSYS.GT_PROSYS_U3_galvo_move_XY((int)(XORIGIN - L1 / 2), (int)(YORIGIN - L1 / 2), gspeed, XOFFSET, YOFFSET, THETA); //delay_ms(10);
            //   // while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
            //    PROSYS.GT_PROSYS_U3_galvo_move_XY((int)(XORIGIN - L1 / 2), (int)(YORIGIN + L1 / 2), gspeed, XOFFSET, YOFFSET, THETA); //delay_ms(10);
            //   // while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
            //    PROSYS.GT_PROSYS_U3_galvo_move_XY((int)(XORIGIN + L1 / 2), (int)(YORIGIN + L1 / 2), gspeed, XOFFSET, YOFFSET, THETA);// delay_ms(10);
            //   // while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
            //    PROSYS.GT_PROSYS_U3_galvo_move_XY((int)(XORIGIN + L1 / 2), (int)(YORIGIN - L1 / 2), gspeed, XOFFSET, YOFFSET, THETA); //delay_ms(10);
            //   // while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;

            //   // //------------------------------- NEW R - Square --------------------------------------//
                //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)(XORIGIN - (L1 / 2)), (int)(YORIGIN), gspeed, XOFFSET, YOFFSET, THETA);
                ////while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
                //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)XORIGIN, (int)(YORIGIN + (L1 / 2)), gspeed, XOFFSET, YOFFSET, THETA);
                //// while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
                //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)(XORIGIN + (L1 / 2)), (int)(YORIGIN), gspeed, XOFFSET, YOFFSET, THETA);
                //// while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
                //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)XORIGIN, (int)(YORIGIN - (L1 / 2)), gspeed, XOFFSET, YOFFSET, THETA);
                //// while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;


            //   // //------------------------------- NEW Line --------------------------------------//
            //   // PROSYS.GT_PROSYS_U3_galvo_move_XY((int)(XORIGIN - (X2 / 2)), (int)(YORIGIN - (Y2 / 2)), gspeed, XOFFSET, YOFFSET, THETA);
            //   //// while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
            //   // //X2 = X2 + 4000; Y2 = Y2 + 4000;
            //   // //delay_ms(5000);
            //   // PROSYS.GT_PROSYS_U3_galvo_move_XY((int)(XORIGIN + (X2 / 2)), (int)(YORIGIN + (Y2 / 2)), gspeed, XOFFSET, YOFFSET, THETA);
            //   // //// delay_ms(1000);
            //   //// while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
            //}






                //------------------------------- Half Circle --------------------------------------//
                    //for (double i = 0; i < 180; i += 0.5)
                    //{
                    //    UInt32 x2 = (uint)(32767 + (L1 * Math.Sin(i * (3.14 / 180))));
                    //    UInt32 y2 = (uint)(32767 + (L1 * Math.Cos(i * (3.14 / 180))));
                    //    // while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
                    //    PROSYS.GT_PROSYS_U3_galvo_move_XY((int)x2, (int)y2, gspeed, XOFFSET, YOFFSET, THETA);


                    //}
              
                    //for (double i = 180; i > 0; i -= 0.5)
                    //{
                    //    UInt32 x2 = (uint)(32767 + (L1 * Math.Sin(i * (3.14 / 180))));
                    //    UInt32 y2 = (uint)(32767 + (L1 * Math.Cos(i * (3.14 / 180))));
                    //     //while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
                    //    PROSYS.GT_PROSYS_U3_galvo_move_XY((int)x2, (int)y2, gspeed, XOFFSET, YOFFSET, THETA);


                    //}
                   




               //position_array[0] = 200;
            //unsafe
            //{
            //    fixed (double* position_ref = position_array) fixed (Int16* axis_ref = axis_array) PROSYS.GT_PROSYS_U3_axis_move(rel_abs, Total_axis_to_move, axis_ref, position_ref, low_speed, max_speed, acc_time);
            //}
            //microSW.Stop();
            //t = microSW.ElapsedMicroseconds;
            //txtbTime.Text = t.ToString();

            
            
            
           }
            
          //txtbTime.Text = t.ToString();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            MessageBox.Show("button Line");
            X1 = (uint)Convert.ToInt32(txtLineX1.Text);
            Y1 = (uint)Convert.ToInt32(txtLineY1.Text);
            X2 = (uint)Convert.ToInt32(txtLineX2.Text);
            Y2 = (uint)Convert.ToInt32(txtLineY2.Text);
            //lstop = true;
            long t;
            microSW.Reset();
            microSW.Start();
            for (UInt16 loop = 0; loop <= 5; loop++)
            {
                if (loop % 2 == 0)
                    feven = true;
                else
                    feven = false;

                if (bstop == true)
                {
                    PROSYS.GT_PROSYS_U3_galvo_move_XY((int)(XORIGIN - (X2 / 2)), (int)(YORIGIN - (Y2 / 2)), gspeed, XOFFSET, YOFFSET, THETA);
                    while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1)
                    {
                        Application.DoEvents();
                    }
                    PROSYS.GT_PROSYS_U3_galvo_move_XY((int)(XORIGIN + (X2 / 2)), (int)(YORIGIN + (Y2 / 2)), gspeed, XOFFSET, YOFFSET, THETA);
                    while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1)
                    {
                        Application.DoEvents();
                    }
                }
                else
                {
                    bstop = true;
                    break;

                }

            }
            microSW.Stop();
            t = microSW.ElapsedMicroseconds;
            txtbTime.Text = t.ToString();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            uint L1;
            L1 = (uint)Convert.ToInt32(txtSqLength.Text);
            long t;
            microSW.Reset();
            microSW.Start();
            MessageBox.Show("button square");
            //lstop = true;
            for (UInt16 loop = 0; loop <= 5; loop++)
            {
                if (loop % 2 == 0)
                    feven = true;
                else
                    feven = false;

                if (bstop == true)
                {
                    //------------------------------- NEW Square --------------------------------------//
                    PROSYS.GT_PROSYS_U3_galvo_move_XY((int)(XORIGIN - L1 / 2), (int)(YORIGIN - L1 / 2), gspeed, XOFFSET, YOFFSET, THETA); //delay_ms(10);
                    while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1)
                    {
                        Application.DoEvents();
                    }
                    PROSYS.GT_PROSYS_U3_galvo_move_XY((int)(XORIGIN - L1 / 2), (int)(YORIGIN + L1 / 2), gspeed, XOFFSET, YOFFSET, THETA); //delay_ms(10);
                    while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1)
                    {
                        Application.DoEvents();
                    }
                    PROSYS.GT_PROSYS_U3_galvo_move_XY((int)(XORIGIN + L1 / 2), (int)(YORIGIN + L1 / 2), gspeed, XOFFSET, YOFFSET, THETA);// delay_ms(10);
                    while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1)
                    {
                        Application.DoEvents();
                    }
                    PROSYS.GT_PROSYS_U3_galvo_move_XY((int)(XORIGIN + L1 / 2), (int)(YORIGIN - L1 / 2), gspeed, XOFFSET, YOFFSET, THETA); //delay_ms(10);
                    while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1)
                    {
                        Application.DoEvents();
                    }
                }
                else
                {
                    bstop = true;
                    break;

                }
            }
            microSW.Stop();
            t = microSW.ElapsedMicroseconds;
            txtbTime.Text = t.ToString();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            uint L1;
            L1 = (uint)Convert.ToInt32(txtRSLength.Text);
            long t;
            microSW.Reset();
            microSW.Start();
            MessageBox.Show("button R-square");
            //lstop = true;
            for (UInt16 loop = 0; loop <= 5; loop++)
            {
                if (loop % 2 == 0)
                    feven = true;
                else
                    feven = false;

                if (bstop == true)
                {
                    if (THETA == 0)
                    {
                        PROSYS.GT_PROSYS_U3_galvo_move_XY((int)(XORIGIN - (L1 / 2)), (int)(YORIGIN), gspeed, XOFFSET, YOFFSET, THETA);
                        /*while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1)
                        {
                            Application.DoEvents();
                        }*/
                        PROSYS.GT_PROSYS_U3_galvo_move_XY((int)XORIGIN, (int)(YORIGIN + (L1 / 2)), gspeed, XOFFSET, YOFFSET, THETA);
                       /* while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1)
                        {
                            Application.DoEvents();
                        }*/
                        PROSYS.GT_PROSYS_U3_galvo_move_XY((int)(XORIGIN + (L1 / 2)), (int)(YORIGIN), gspeed, XOFFSET, YOFFSET, THETA);
                        while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1)
                        {
                            Application.DoEvents();
                        }
                        PROSYS.GT_PROSYS_U3_galvo_move_XY((int)XORIGIN, (int)(YORIGIN - (L1 / 2)), gspeed, XOFFSET, YOFFSET, THETA);
                        while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1)
                        {
                            Application.DoEvents();
                        }
                    }
                    else if (THETA == 1)
                    {
                        PROSYS.GT_PROSYS_U3_galvo_move_XY((int)(YORIGIN - (L1 / 2)), (int)(XORIGIN), gspeed, YOFFSET, XOFFSET, THETA);
                        while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1)
                        {
                            Application.DoEvents();
                        }
                        PROSYS.GT_PROSYS_U3_galvo_move_XY((int)YORIGIN, (int)(XORIGIN + (L1 / 2)), gspeed, YOFFSET, XOFFSET, THETA);
                        while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1)
                        {
                            Application.DoEvents();
                        }
                        PROSYS.GT_PROSYS_U3_galvo_move_XY((int)(YORIGIN + (L1 / 2)), (int)(XORIGIN), gspeed, YOFFSET, XOFFSET, THETA);
                        while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1)
                        {
                            Application.DoEvents();
                        }
                        PROSYS.GT_PROSYS_U3_galvo_move_XY((int)YORIGIN, (int)(XORIGIN - (L1 / 2)), gspeed, YOFFSET, XOFFSET, THETA);
                        while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1)
                        {
                            Application.DoEvents();
                        }                    
                    }
                }
                else
                {
                    bstop = true;
                    break;

                }
            }
            microSW.Stop();
            t = microSW.ElapsedMicroseconds;
            txtbTime.Text = t.ToString();
        }

        private void button9_Click(object sender, EventArgs e)
        {
            uint L1;
            L1 = (uint)Convert.ToInt32(txtCircleR.Text);
            long t;
            microSW.Reset();
            microSW.Start();
            //lstop = true;
            MessageBox.Show("button Circle");
            if (L1 <= 32767)
            {
                for (UInt16 loop = 0; loop <= 3; loop++)
                {
                    if (loop % 2 == 0)
                        feven = true;
                    else
                        feven = false;

                    if (bstop == true)
                    {

                        double ii = 0.00;
                        UInt32 x2 = (uint)(32767 + (L1 * Math.Sin(ii * (3.14 / 180))));
                        UInt32 y2 = (uint)(32767 + (L1 * Math.Cos(ii * (3.14 / 180))));
                        PROSYS.GT_PROSYS_U3_galvo_move_XY((int)x2, (int)y2, gspeed, XOFFSET, YOFFSET, THETA);
                        while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1)
                        {
                            Application.DoEvents();
                        }

                        
                        for (double i = 2; i < 360; i += 2)
                        {
                            if (bstop == true)
                            {
                                 x2 = (uint)(32767 + (L1 * Math.Sin(i * (3.14 / 180))));
                                 y2 = (uint)(32767 + (L1 * Math.Cos(i * (3.14 / 180))));
                                PROSYS.GT_PROSYS_U3_galvo_move_XY((int)x2, (int)y2, gspeed, XOFFSET, YOFFSET, THETA);
                                while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1)
                                {
                                    Application.DoEvents();
                                }
                            }
                            else
                            {
                                //bstop = true;
                                break; 
                            }



                        }
                    }
                    else
                    {
                        bstop = true;
                        break;

                    }

                }
            }
            microSW.Stop();
            t = microSW.ElapsedMicroseconds;
            txtbTime.Text = t.ToString();
        }

        private void button5_Click_1(object sender, EventArgs e)
        {
            PROSYS.GT_PROSYS_U3_set_continous_mode_on();
            //microSW2.Reset();
            //microSW2.Start();
            //buff_ = true;
        }

        private void button10_Click_1(object sender, EventArgs e)
        {
            PROSYS.GT_PROSYS_U3_set_continous_mode_off();
            while (PROSYS.GT_PROSYS_U3_buffer_ready() == 1)
            {

                Application.DoEvents();
            }
            //microSW2.Stop();
            ////t = microSW2.ElapsedMicroseconds;
            //txtbTime.Text = microSW2.ElapsedMicroseconds.ToString();
           // buff_ = false;
            
           
        }

        private void Position_timer_Tick(object sender, EventArgs e)
        {
            //UInt32 CMDId = new UInt32();
            UInt32 cmd_id = new UInt32();
            long t=0;

            
            unsafe
            {

                PROSYS.GT_PROSYS_U3_get_buf_cur_id(&cmd_id);

            }
            txtBuffid_1.Text = cmd_id.ToString();
            //    if (cmd_x == 100 && bstop == true)
            //    {
            //        txtbTime.Text = t.ToString();
            //        microSW.Reset();
            //        microSW.Start();
            //        bstop = false;
            //        txtBuffid.Text = "1";
            //    }
            //    if (cmd_x == 200)
            //    {
            //        microSW.Stop();
            //        t = microSW.ElapsedMicroseconds;
            //        txtbTime.Text = t.ToString();
            //        txtBuffid.Text = "0";
            //    }


            //}
            unsafe
            {
                Int32 cmd_x = new Int32();
                Int32 cmd_y = new Int32();
                Int32 cmd_z = new Int32();
                Int32 cmd_u = new Int32();
                Int32 cmd_v = new Int32();
                Int32 cmd_w = new Int32();
                Int32 cmd_xg = new Int32();
                Int32 cmd_yg = new Int32();
                PROSYS.GT_PROSYS_U3_get_command(0, &cmd_x);
                PROSYS.GT_PROSYS_U3_get_command(1, &cmd_y);
                PROSYS.GT_PROSYS_U3_get_command(2, &cmd_z);
                PROSYS.GT_PROSYS_U3_get_command(3, &cmd_u);
                PROSYS.GT_PROSYS_U3_get_command(4, &cmd_v);
               PROSYS.GT_PROSYS_U3_get_command(5, &cmd_w);
                x_pos.Text = cmd_x.ToString();
                y_pos.Text = cmd_y.ToString();
                z_pos.Text = cmd_z.ToString();
                u_pos.Text = cmd_u.ToString();
                v_pos.Text = cmd_v.ToString();
                w_pos.Text = cmd_w.ToString();
                if (THETA == 0)
                {
                    PROSYS.GT_PROSYS_U3_get_XY_Data(&cmd_xg, &cmd_yg);
                }
                else if (THETA == 1)
                {
                    PROSYS.GT_PROSYS_U3_get_XY_Data(&cmd_yg, &cmd_xg);
                }
                x_gpos.Text = cmd_xg.ToString();
                y_gpos.Text = cmd_yg.ToString();
            }
            //x_alm.Text = PROSYS.GT_PROSYS_U3_get_alm(0).ToString();
            //y_alm.Text = PROSYS.GT_PROSYS_U3_get_alm(1).ToString();
            //z_alm.Text = PROSYS.GT_PROSYS_U3_get_alm(2).ToString();
            //u_alm.Text = PROSYS.GT_PROSYS_U3_get_alm(3).ToString();
            //v_alm.Text = PROSYS.GT_PROSYS_U3_get_alm(4).ToString();
            Int16 L1;
            L1 = PROSYS.GT_PROSYS_U3_get_do();
            lbDO.Text = L1.ToString();

            t = PROSYS.GT_PROSYS_U3_buffer_ready();
            //if (t == 1)
            //{
            //   // microSW2.Stop();
            //    //t = microSW2.ElapsedMicroseconds;
            //    txtbTime.Text = microSW2.ElapsedMicroseconds.ToString();
            //}
            //else 
            //{
            //    microSW2.Stop();

            //}
            txtBuffid.Text = t.ToString();
           t = PROSYS.GetFreeBRAMSpace();

            
           txtBRAM_space.Text = t.ToString();

           t = PROSYS.GetFIFOCommands();
           txtFIFO_space.Text = t.ToString();


          
         
            New_Cx = (float.Parse(x_gpos.Text)) * 3 / 400;
            New_Cy = (float.Parse(y_gpos.Text)) * 3 / 400;
            if (!once)
            {
                Pre_Cx = New_Cx;
                Pre_Cy = New_Cy;
                once = true;
            }


            //gr.DrawLine(Pens.Red, Rotated_Center_X_L[(int)j] - 5, Rotated_Center_Y_L[(int)j], Rotated_Center_X_L[(int)j] + 5, Rotated_Center_Y_L[(int)j]);
            //gr.DrawLine(Pens.Red, Rotated_Center_X_L[(int)j], Rotated_Center_Y_L[(int)j] - 5, Rotated_Center_X_L[(int)j], Rotated_Center_Y_L[(int)j] + 5);
            //gr.DrawArc(Pens.Red, Rotated_Center_X_L[(int)j] - Out_R, Rotated_Center_Y_L[(int)j] - Out_R, Out_R * 2, Out_R * 2, (270 - (float)rotate_angle), 180);
            //gr.DrawLine(
            if (feven)
            {
                gr.DrawLine(Pens.YellowGreen, Pre_Cx, Pre_Cy, New_Cx, New_Cy);
            }
            else
            {
                gr.DrawLine(Pens.Red, Pre_Cx, Pre_Cy, New_Cx, New_Cy);
            }
            pictureBox1.Image = bm;
            Pre_Cx = New_Cx;
            Pre_Cy = New_Cy;
            
        }

        private void Set_Offset_Click(object sender, EventArgs e)
        {
            XOFFSET = Convert.ToInt32(TbOffX.Text);
            YOFFSET = Convert.ToInt32(TbOffY.Text);

            PROSYS.GT_PROSYS_U3_galvo_move_XY((int)0, (int)0, gspeed, XOFFSET, YOFFSET, THETA);
        }

        private void button1_Click(object sender, EventArgs e)
        {
           
        }

        private void button11_Click(object sender, EventArgs e)
        {
            PROSYS.GT_PROSYS_U3_buffer_pause();
        }

        private void button12_Click(object sender, EventArgs e)
        {
            PROSYS.GT_PROSYS_U3_buffer_resume();
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            PROSYS.GT_PROSYS_U3_Close();
        }

        private void button13_Click(object sender, EventArgs e)
        {
            Int16[] axis_array = new Int16[3];
            Int16 Motion;
            double[] position_array = new double[5];
            Int16 rel_abs;
            Int16 Total_axis_to_move = 1;
            double low_speed;
            double max_speed;
            double acc_time;

            rel_abs = Convert.ToInt16(relabs.Text);
            axis_array[0] = Convert.ToInt16(axis.Text);
            position_array[0] = Convert.ToDouble(count.Text);
            low_speed = Convert.ToDouble(str_vel.Text);
            max_speed = Convert.ToDouble(max_vel.Text);
            acc_time = Convert.ToDouble(acc.Text);

            unsafe
            {
                fixed (double* position_ref = position_array) fixed (Int16* axis_ref = axis_array) PROSYS.GT_PROSYS_U3_axis_move(rel_abs, Total_axis_to_move, axis_ref, position_ref, low_speed, max_speed, acc_time);
            }
            //while (PROSYS.GT_PROSYS_U3_motion_done(0) > 0)
            //{
            //    Application.DoEvents();
            //}
        }

        private void button14_Click(object sender, EventArgs e)
        {
            PROSYS.GT_PROSYS_U3_buf_abort();
        }

        private void button15_Click(object sender, EventArgs e)
        {
            uint L1,stat;

            L1 = (uint)Convert.ToInt32(txtCircleR.Text);
            //------------------------------- Half Circle --------------------------------------//
                for (UInt16 loop = 0; loop <= 5; loop++)
                {
                    PROSYS.GT_PROSYS_U3_set_continous_mode_on();
                    for (double i = 0; i < 180; i += 0.5)
                    {
                        UInt32 x2 = (uint)(32767 + (L1 * Math.Sin(i * (3.14 / 180))));
                        UInt32 y2 = (uint)(32767 + (L1 * Math.Cos(i * (3.14 / 180))));
                        PROSYS.GT_PROSYS_U3_galvo_move_XY((int)x2, (int)y2, gspeed, XOFFSET, YOFFSET, THETA);


                    }
                    PROSYS.GT_PROSYS_U3_set_continous_mode_off();
                   while (PROSYS.GT_PROSYS_U3_buffer_ready()==1)
                   {
                       Application.DoEvents();
                   }
                    PROSYS.GT_PROSYS_U3_set_continous_mode_on();
                    for (double i = 180; i > 0; i -= 0.5)
                    {
                        UInt32 x2 = (uint)(32767 + (L1 * Math.Sin(i * (3.14 / 180))));
                        UInt32 y2 = (uint)(32767 + (L1 * Math.Cos(i * (3.14 / 180))));
                        PROSYS.GT_PROSYS_U3_galvo_move_XY((int)x2, (int)y2, gspeed, XOFFSET, YOFFSET, THETA);
                    }
                    PROSYS.GT_PROSYS_U3_set_continous_mode_off();
                    while (PROSYS.GT_PROSYS_U3_buffer_ready() == 1) 
                    {
                        Application.DoEvents();
                    }
               }
        }

        private void button16_Click(object sender, EventArgs e)
        {
            uint L1;
            L1 = (uint)Convert.ToInt32(txtCircleR.Text);
            if (L1 <= 32767)
            {
                for (UInt16 loop = 0; loop <= 5; loop++)
                {
                   
                    if (bstop == true)
                    {
                        for (double i = 0; i < 180; i += 0.5)
                        {
                            feven = true;
                            if (bstop == true)
                            {
                                UInt32 x2 = (uint)(32767 + (L1 * Math.Sin(i * (3.14 / 180))));
                                UInt32 y2 = (uint)(32767 + (L1 * Math.Cos(i * (3.14 / 180))));
                                PROSYS.GT_PROSYS_U3_galvo_move_XY((int)x2, (int)y2, gspeed, XOFFSET, YOFFSET, THETA);
                                while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1)
                                {
                                    Application.DoEvents();
                                }
                            }
                            else 
                            {
                                break;
                            }

                        }
                        for (double i = 180; i > 0; i -= 0.5)
                        {
                            feven = false;
                            if (bstop == true)
                            {
                                UInt32 x2 = (uint)(32767 + (L1 * Math.Sin(i * (3.14 / 180))));
                                UInt32 y2 = (uint)(32767 + (L1 * Math.Cos(i * (3.14 / 180))));
                                PROSYS.GT_PROSYS_U3_galvo_move_XY((int)x2, (int)y2, gspeed, XOFFSET, YOFFSET, THETA);
                                while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1)
                                {
                                    Application.DoEvents();
                                }
                            }
                            else
                            {
                                break;
                            }

                        }

                    }
                    else
                    {
                        bstop = true;
                        break;

                    }

                }
            }
        }

        private void button17_Click(object sender, EventArgs e)
        {
            
            PROSYS.GT_PROSYS_U3_galvo_stop();
            bstop = false;
        }

        private void button19_Click(object sender, EventArgs e)
        {
            gr.Clear(System.Drawing.SystemColors.ControlDark);
        }

        private void button20_Click(object sender, EventArgs e)
        {
            Int16 L1;
            L1 = PROSYS.GT_PROSYS_U3_get_do();
            lbDO.Text = L1.ToString();
            
        }

        private void button18_Click(object sender, EventArgs e)
        {
            Int16 L1;
            L1 = Convert.ToInt16(tbDO.Text);
            
            PROSYS.GT_PROSYS_U3_set_do_bit(3, L1);
            
        }

        private void button21_Click(object sender, EventArgs e)
        {
            Int16[] axis_array = new Int16[3];
            Int16 Motion;
            double[] position_array = new double[5];
            Int16 rel_abs;
            Int16 Total_axis_to_move = 1;
            double low_speed;
            double max_speed;
            double acc_time;

            rel_abs = Convert.ToInt16(relabs.Text);
            axis_array[0] = Convert.ToInt16(axis.Text);
            position_array[0] = Convert.ToDouble(count.Text);
            low_speed = Convert.ToDouble(str_vel.Text);
            max_speed = Convert.ToDouble(max_vel.Text);
            acc_time = Convert.ToDouble(acc.Text);



            for (UInt16 loop = 0; loop < 50; loop++)
            {
                unsafe
                {
                    fixed (double* position_ref = position_array) fixed (Int16* axis_ref = axis_array) PROSYS.GT_PROSYS_U3_axis_move(rel_abs, Total_axis_to_move, axis_ref, position_ref, low_speed, max_speed, acc_time);
                }
            }
            
        }

        private void button22_Click(object sender, EventArgs e)
        {
            PROSYS.GT_PROSYS_U3_send_buffer();
        }

        private void button23_Click(object sender, EventArgs e)
        {
            uint L1;
            uint L2;
            L1 = (uint)Convert.ToInt32(tbA.Text)*1000;
            L2 = (uint)Convert.ToInt32(tbB.Text)*1000;
            long t;
            microSW.Reset();
            microSW.Start();
            //lstop = true;
            MessageBox.Show("button Ellipse");
            if (L1 <= 32767 && L2 <= 32767)
            {
                for (UInt16 loop = 0; loop <= 1; loop++)
                {
                    if (loop % 2 == 0)
                        feven = true;
                    else
                        feven = false;

                    if (bstop == true)
                    {
                        for (double i = 1; i < 360; i += 2)
                        {
                            if (bstop == true)
                            {
                                UInt32 x2 = (uint)(32767 + (L1 * Math.Sin(i * (3.14 / 180))));
                                UInt32 y2 = (uint)(32767 + (L2 * Math.Cos(i * (3.14 / 180))));
                                PROSYS.GT_PROSYS_U3_galvo_move_XY((int)x2, (int)y2, gspeed, XOFFSET, YOFFSET, THETA);
                                while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1)
                                {
                                    Application.DoEvents();
                                }
                            }
                            else
                            {
                                //bstop = true;
                                break;
                            }



                        }
                    }
                    else
                    {
                        bstop = true;
                        break;

                    }

                }
            }
            microSW.Stop();
            t = microSW.ElapsedMicroseconds;
            txtbTime.Text = t.ToString();
        }

        private void button24_Click(object sender, EventArgs e)
        {
            MessageBox.Show("button Line");
            X1 = (uint)Convert.ToInt32(txtLineX1.Text);
            Y1 = (uint)Convert.ToInt32(txtLineY1.Text);
            X2 = (uint)Convert.ToInt32(txtLineX2.Text);
            Y2 = (uint)Convert.ToInt32(txtLineY2.Text);
            //lstop = true;
            long t;
            microSW.Reset();
            microSW.Start();
           // for (UInt16 loop = 0; loop <= 5; loop++)
            {
                //if (loop % 2 == 0)
                //    feven = true;
                //else
                //    feven = false;

                if (bstop == true)
                {
                    PROSYS.GT_PROSYS_U3_galvo_move_XY((int)(XORIGIN + 1000), (int)(YORIGIN - 500 ), gspeed, XOFFSET, YOFFSET, THETA);
                    while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1)
                    {
                        Application.DoEvents();
                    }
                    PROSYS.GT_PROSYS_U3_galvo_move_XY((int)(XORIGIN + 25000), (int)(YORIGIN - 15000), gspeed, XOFFSET, YOFFSET, THETA);
                    while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1)
                    {
                        Application.DoEvents();
                    }
                }
                else
                {
                    bstop = true;
                   // break;

                }

            }
            microSW.Stop();
            t = microSW.ElapsedMicroseconds;
            txtbTime.Text = t.ToString();
        }

        private void button25_Click(object sender, EventArgs e)
        {
            double MaxVal=100.0;
            double CurVal=80.0;
            double FreqVal = 1000.0;
            short bit=0;

            PROSYS.GT_PROSYS_U3_set_analog_do_bit(MaxVal, CurVal, FreqVal, bit);

        }

        private void button26_Click(object sender, EventArgs e)
        {
            Int16[] axis_array = new Int16[3];
            Int16 Motion;
            double[] position_array = new double[5];
            Int16 rel_abs;
            Int16 Total_axis_to_move = 1;
            double low_speed;
            double max_speed;
            double acc_time;
            Int16 size;
            size = Convert.ToInt16(tbSize.Text);
            rel_abs = Convert.ToInt16(relabs.Text);
            axis_array[0] = Convert.ToInt16(axis.Text);
            position_array[0] = Convert.ToDouble(count.Text);
            low_speed = 10000;
            max_speed = 300000;
            acc_time = Convert.ToDouble(acc.Text);

            for (int i = 0; i < (4000*size); i++)
            {
                unsafe
                {
                    fixed (double* position_ref = position_array) fixed (Int16* axis_ref = axis_array) PROSYS.GT_PROSYS_U3_axis_move(rel_abs, Total_axis_to_move, axis_ref, position_ref, low_speed, max_speed, acc_time);
                }
            }
        }

        private void button27_Click(object sender, EventArgs e)
        {
           // uint L1;
           // L1 = (uint)Convert.ToInt32(txtCircleR.Text);
           // PROSYS.GT_PROSYS_U3_set_do_bit(5, 1);
           //// delay_ms(10);
           // microSW3.Reset();
           // microSW3.Start();
           // for (UInt16 loop0 = 0; loop0 <= 10; loop0++)
           // {
           //     PROSYS.GT_PROSYS_U3_set_continous_mode_on();
               
           //     for (UInt16 loop = 0; loop <= 3; loop++)
           //     {



           //         //    //------------irregular shape Normal Mode--------------------//
           //         //    //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)0, (int)40000, gspeed, XOFFSET, YOFFSET,  THETA);
           //         //    //while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
           //         //    //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)0, (int)50000, gspeed, XOFFSET, YOFFSET,  THETA);
           //         //    //while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
           //         //    //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)20000, (int)50000, gspeed, XOFFSET, YOFFSET,  THETA);
           //         //    //while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
           //         //    //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)23000, (int)54000, gspeed, XOFFSET, YOFFSET,  THETA);
           //         //    //while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
           //         //    //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)43000, (int)54000, gspeed, XOFFSET, YOFFSET,  THETA);
           //         //    //while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
           //         //    //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)43000, (int)50000, gspeed, XOFFSET, YOFFSET,  THETA);
           //         //    //while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
           //         //    //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)40000, (int)46000, gspeed, XOFFSET, YOFFSET,  THETA);
           //         //    //while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
           //         //    //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)20000, (int)46000, gspeed, XOFFSET, YOFFSET,  THETA);
           //         //    //while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
           //         //    //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)20000, (int)40000, gspeed, XOFFSET, YOFFSET,  THETA);
           //         //    //while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;


           //         //    //------------irregular shape Buffer Mode--------------------//
           //         //    //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)0, (int)40000, gspeed, XOFFSET, YOFFSET, THETA);
           //         //    ////while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
           //         //    //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)0, (int)50000, gspeed, XOFFSET, YOFFSET, THETA);
           //         //    ////while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
           //         //    //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)20000, (int)50000, gspeed, XOFFSET, YOFFSET, THETA);
           //         //    ////while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
           //         //    //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)23000, (int)54000, gspeed, XOFFSET, YOFFSET, THETA);
           //         //    //// while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
           //         //    //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)43000, (int)54000, gspeed, XOFFSET, YOFFSET, THETA);
           //         //    ////while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
           //         //    //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)43000, (int)50000, gspeed, XOFFSET, YOFFSET, THETA);
           //         //    ////while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
           //         //    //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)40000, (int)46000, gspeed, XOFFSET, YOFFSET, THETA);
           //         //    ////while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
           //         //    //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)20000, (int)46000, gspeed, XOFFSET, YOFFSET, THETA);
           //         //    ////while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
           //         //    //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)20000, (int)40000, gspeed, XOFFSET, YOFFSET, THETA);
           //         //    ////while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;

           //         //    //------------------------------- Square --------------------------------------//

           //         //   // PROSYS.GT_PROSYS_U3_galvo_move_XY((int)10000, (int)10000, gspeed, XOFFSET, YOFFSET,  THETA); //delay_ms(10);
           //         //   // //while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
           //         //   // PROSYS.GT_PROSYS_U3_galvo_move_XY((int)10000, (int)L1 + 10000, gspeed, XOFFSET, YOFFSET,  THETA); //delay_ms(10);
           //         //   //// while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
           //         //   // PROSYS.GT_PROSYS_U3_galvo_move_XY((int)L1 + 10000, (int)L1 + 10000, gspeed, XOFFSET, YOFFSET,  THETA);// delay_ms(10);
           //         //   //// while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
           //         //   // PROSYS.GT_PROSYS_U3_galvo_move_XY((int)L1 + 10000, (int)0 + 10000, gspeed, XOFFSET, YOFFSET,  THETA); //delay_ms(10);
           //         //   // //while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;

           //         //    //-------------------------------  R - Square --------------------------------------//
           //         //   // PROSYS.GT_PROSYS_U3_galvo_move_XY((int)0, (int)(L1 / 2) , gspeed, XOFFSET, YOFFSET, THETA);
           //         //   // //while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
           //         //   // PROSYS.GT_PROSYS_U3_galvo_move_XY((int)(L1 / 2) , (int)L1, gspeed, XOFFSET, YOFFSET, THETA);
           //         //   //// while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
           //         //   // PROSYS.GT_PROSYS_U3_galvo_move_XY((int)L1 , (int)(L1 / 2) , gspeed, XOFFSET, YOFFSET, THETA);
           //         //   // //while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
           //         //   // PROSYS.GT_PROSYS_U3_galvo_move_XY((int)(L1 / 2) , (int)0, gspeed, XOFFSET, YOFFSET, THETA);
           //         //   // //while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;


           //         //    //------------------------------- NEW Square --------------------------------------//
           //         //    PROSYS.GT_PROSYS_U3_galvo_move_XY((int)(XORIGIN - L1 / 2), (int)(YORIGIN - L1 / 2), gspeed, XOFFSET, YOFFSET, THETA); //delay_ms(10);
           //         //   // while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
           //         //    PROSYS.GT_PROSYS_U3_galvo_move_XY((int)(XORIGIN - L1 / 2), (int)(YORIGIN + L1 / 2), gspeed, XOFFSET, YOFFSET, THETA); //delay_ms(10);
           //         //   // while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
           //         //    PROSYS.GT_PROSYS_U3_galvo_move_XY((int)(XORIGIN + L1 / 2), (int)(YORIGIN + L1 / 2), gspeed, XOFFSET, YOFFSET, THETA);// delay_ms(10);
           //         //   // while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
           //         //    PROSYS.GT_PROSYS_U3_galvo_move_XY((int)(XORIGIN + L1 / 2), (int)(YORIGIN - L1 / 2), gspeed, XOFFSET, YOFFSET, THETA); //delay_ms(10);
           //         //   // while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;

           //         //   // //------------------------------- NEW R - Square --------------------------------------//
           //         //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)(XORIGIN - (L1 / 2)), (int)(YORIGIN), gspeed, XOFFSET, YOFFSET, THETA);
           //         ////while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
           //         //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)XORIGIN, (int)(YORIGIN + (L1 / 2)), gspeed, XOFFSET, YOFFSET, THETA);
           //         //// while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
           //         //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)(XORIGIN + (L1 / 2)), (int)(YORIGIN), gspeed, XOFFSET, YOFFSET, THETA);
           //         //// while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
           //         //PROSYS.GT_PROSYS_U3_galvo_move_XY((int)XORIGIN, (int)(YORIGIN - (L1 / 2)), gspeed, XOFFSET, YOFFSET, THETA);
           //         //// while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;


           //         //   // //------------------------------- NEW Line --------------------------------------//
           //         //   // PROSYS.GT_PROSYS_U3_galvo_move_XY((int)(XORIGIN - (X2 / 2)), (int)(YORIGIN - (Y2 / 2)), gspeed, XOFFSET, YOFFSET, THETA);
           //         //   //// while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
           //         //   // //X2 = X2 + 4000; Y2 = Y2 + 4000;
           //         //   // //delay_ms(5000);
           //         //   // PROSYS.GT_PROSYS_U3_galvo_move_XY((int)(XORIGIN + (X2 / 2)), (int)(YORIGIN + (Y2 / 2)), gspeed, XOFFSET, YOFFSET, THETA);
           //         //   // //// delay_ms(1000);
           //         //   //// while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
           //         //}






           //         //------------------------------- Half Circle --------------------------------------//
           //         for (double i = 0; i < 180; i += 0.5)
           //         {
           //             UInt32 x2 = (uint)(32767 + (L1 * Math.Sin(i * (3.14 / 180))));
           //             UInt32 y2 = (uint)(32767 + (L1 * Math.Cos(i * (3.14 / 180))));
           //             // while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
           //             PROSYS.GT_PROSYS_U3_galvo_move_XY((int)x2, (int)y2, gspeed, XOFFSET, YOFFSET, THETA);


           //         }

           //         for (double i = 180; i > 0; i -= 0.5)
           //         {
           //             UInt32 x2 = (uint)(32767 + (L1 * Math.Sin(i * (3.14 / 180))));
           //             UInt32 y2 = (uint)(32767 + (L1 * Math.Cos(i * (3.14 / 180))));
           //             //while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
           //             PROSYS.GT_PROSYS_U3_galvo_move_XY((int)x2, (int)y2, gspeed, XOFFSET, YOFFSET, THETA);


           //         }





           //         //position_array[0] = 200;
           //         //unsafe
           //         //{
           //         //    fixed (double* position_ref = position_array) fixed (Int16* axis_ref = axis_array) PROSYS.GT_PROSYS_U3_axis_move(rel_abs, Total_axis_to_move, axis_ref, position_ref, low_speed, max_speed, acc_time);
           //         //}
           //         //microSW.Stop();
           //         //t = microSW.ElapsedMicroseconds;
           //         //txtbTime.Text = t.ToString();




           //     }
           //     PROSYS.GT_PROSYS_U3_set_continous_mode_off();
           //     while (PROSYS.GT_PROSYS_U3_buffer_ready() == 1)
           //     {
           //         Application.DoEvents();
           //     }
           // }
           // PROSYS.GT_PROSYS_U3_set_do_bit(5, 0);
            
           // txtbTime.Text = microSW3.ElapsedMicroseconds.ToString();
           // microSW3.Stop();
            //======================================================================================================//
            Int16[] axis_array = new Int16[3];
            Int32 Cx, Cy, Ex, Ey, V;
            double[] position_array = new double[5];

            axis_array[0] = 0;
            axis_array[1] = 1;
            position_array[0] = 0; //Cx
            position_array[1] = 0;  //Cy
            position_array[2] = 168438; //Ex
            position_array[3] = 79202;  //Ey
            position_array[4] = 0;  //Dir
           
            V = 20000;
            long t;
            //microSW.Reset();
            //microSW.Start();
            unsafe
            {
                fixed (double* position_ref = position_array) fixed (Int16* axis_ref = axis_array) PROSYS.GT_PROSYS_U3_axis_move(0, 2, axis_ref, position_ref, 1000, 10000, 0.1);
            }
            //unsafe
            //{
            //    fixed (Int16* axis_ref = axis_array) PROSYS.GTPROS2_start_ta_move_line2(0, axis_ref, Ex, Ey, 45000, 50000, 0.1, 0.1);
            //}
            while (PROSYS.GT_PROSYS_U3_motion_done(0) > 0)
            {
                Application.DoEvents();
            }
            position_array[0] = 10000;// 164265; //Cx
            position_array[1] = 0;// 79202;  //Cy
            position_array[2] = 20000;// 168438; //Ex
            position_array[3] = 0;// 79202;  //Ey
            position_array[4] = 0;  //Dir
          //  for (int i = 0; i <= 4; i++)
            {
                feven = !feven;
                unsafe
                {
                    unsafe
                    {
                        fixed (double* position_ref = position_array) fixed (Int16* axis_ref = axis_array) PROSYS.GT_PROSYS_U3_axis_move(0, 4, axis_ref, position_ref, 1000, 10000, 0.1);
                    }
                }

               
                
            }
            while (PROSYS.GT_PROSYS_U3_buffer_ready() == 1)
            {

                Application.DoEvents();
            }
        }

        private void button28_Click(object sender, EventArgs e)
        {
            unsafe
            {
                Int32 cmd_x = new Int32();
                Int32 cmd_y = new Int32();
                Int32 cmd_z = new Int32();
                Int32 cmd_u = new Int32();
                Int32 cmd_v = new Int32();
              //  Int32 cmd_w = new Int32();
                Int32 cmd_xg = new Int32();
                Int32 cmd_yg = new Int32();
                PROSYS.GT_PROSYS_U3_get_command(0, &cmd_x);
                PROSYS.GT_PROSYS_U3_get_command(1, &cmd_y);
                PROSYS.GT_PROSYS_U3_get_command(2, &cmd_z);
                PROSYS.GT_PROSYS_U3_get_command(3, &cmd_u);
                PROSYS.GT_PROSYS_U3_get_command(4, &cmd_v);
                 //  PROSYS.GT_PROSYS_U3_get_command(5, &cmd_w);
                x_pos.Text = cmd_x.ToString();
                y_pos.Text = cmd_y.ToString();
                z_pos.Text = cmd_z.ToString();
                u_pos.Text = cmd_u.ToString();
                v_pos.Text = cmd_v.ToString();
               // w_pos.Text = cmd_w.ToString();
                if (THETA == 0)
                {
                    PROSYS.GT_PROSYS_U3_get_XY_Data(&cmd_xg, &cmd_yg);
                }
                else if (THETA == 1)
                {
                    PROSYS.GT_PROSYS_U3_get_XY_Data(&cmd_yg, &cmd_xg);
                }
                x_gpos.Text = cmd_xg.ToString();
                y_gpos.Text = cmd_yg.ToString();
            }

            UInt32 cmd_id = new UInt32();
            long t = 0;


            unsafe
            {

                PROSYS.GT_PROSYS_U3_get_buf_cur_id(&cmd_id);

            }
            txtBuffid_1.Text = cmd_id.ToString();

            t = PROSYS.GT_PROSYS_U3_buffer_ready();
           
            txtBuffid.Text = t.ToString();
            t = PROSYS.GetFreeBRAMSpace();


            txtBRAM_space.Text = t.ToString();

            t = PROSYS.GetFIFOCommands();
            txtFIFO_space.Text = t.ToString();

        }

        private void button29_Click(object sender, EventArgs e)
        {
            Int16[] axis_array = new Int16[5];
            Int16 Motion;
            double[] position_array = new double[5];
            Int16 rel_abs;
            Int16 Total_axis_to_move = 1;
            double low_speed;
            double max_speed;
            double acc_time;

            rel_abs = 0;
            axis_array[0] = Convert.ToInt16(axis.Text);
            axis_array[1] = 1;
            axis_array[2] = 2;
            axis_array[3] = 3;
            axis_array[4] = 4;
            position_array[0] = Convert.ToDouble(count.Text);
            position_array[1] = 2000;
            position_array[2] = 5000;
            position_array[3] = 1500;
            position_array[4] = 0;
           // position_array[0] = 0;
            low_speed = Convert.ToDouble(str_vel.Text);
            max_speed = Convert.ToDouble(max_vel.Text);
            acc_time = Convert.ToDouble(acc.Text);
            uint L1;
            L1 = (uint)Convert.ToInt32(txtCircleR.Text);
           
            PROSYS.GT_PROSYS_U3_set_continous_mode_on();

            for (UInt16 loop = 0; loop < 100; loop++)
            {
                //position_array[0] = position_array[0] + 1000;
                unsafe
                {
                    fixed (double* position_ref = position_array) fixed (Int16* axis_ref = axis_array) PROSYS.GT_PROSYS_U3_axis_move(rel_abs, Total_axis_to_move, axis_ref, position_ref, low_speed, max_speed, acc_time);
                }
               // PROSYS.GT_PROSYS_U3_set_do(loop);

            }
            //unsafe
            //{
            //    fixed (double* position_ref = position_array) fixed (Int16* axis_ref = axis_array) PROSYS.GT_PROSYS_U3_axis_move(rel_abs, 5, axis_ref, position_ref, low_speed, max_speed, acc_time);
            //}
            for (UInt16 loop = 0; loop <= 100; loop++)
            {

                //    //------------------------------- Square --------------------------------------//

                PROSYS.GT_PROSYS_U3_galvo_move_XY((int)10000, (int)10000, gspeed, XOFFSET, YOFFSET, THETA); //delay_ms(10);
                //while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
                PROSYS.GT_PROSYS_U3_galvo_move_XY((int)10000, (int)L1 + 10000, gspeed, XOFFSET, YOFFSET, THETA); //delay_ms(10);
                // while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
                PROSYS.GT_PROSYS_U3_galvo_move_XY((int)L1 + 10000, (int)L1 + 10000, gspeed, XOFFSET, YOFFSET, THETA);// delay_ms(10);
                // while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
                PROSYS.GT_PROSYS_U3_galvo_move_XY((int)L1 + 10000, (int)0 + 10000, gspeed, XOFFSET, YOFFSET, THETA); //delay_ms(10);
                //while (PROSYS.GT_PROSYS_U3_galvo_run_status() == 1) ;
              //  PROSYS.GT_PROSYS_U3_set_do(loop);
            }
            //for (UInt16 loop = 0; loop < 100; loop++)
            //{
            //    //position_array[0] = position_array[0] + 1000;
            //    unsafe
            //    {
            //        fixed (double* position_ref = position_array) fixed (Int16* axis_ref = axis_array) PROSYS.GT_PROSYS_U3_axis_move(rel_abs, Total_axis_to_move, axis_ref, position_ref, low_speed, max_speed, acc_time);
            //    }
            //    PROSYS.GT_PROSYS_U3_set_do(loop);

            //}



            while (PROSYS.GT_PROSYS_U3_buffer_ready() == 1)
            {

                Application.DoEvents();
            }

           
        }

        private void button30_Click(object sender, EventArgs e)
        {
            Int16[] axis_array = new Int16[5];
            Int16 Motion;
            double[] position_array = new double[5];
            Int16 rel_abs;
            Int16 Total_axis_to_move = 5;
            double low_speed;
            double max_speed;
            double acc_time;

            rel_abs = Convert.ToInt16(relabs.Text);
            axis_array[0] = Convert.ToInt16(axis.Text);
            axis_array[1] = 1;
            axis_array[2] = 2;
            axis_array[3] = 3;
            axis_array[4] = 4;
            position_array[0] = Convert.ToDouble(count.Text);
            position_array[1] = 2000;
            position_array[2] = 5000;
            position_array[3] = 1500;
            position_array[4] = 500;
            low_speed = Convert.ToDouble(str_vel.Text);
            max_speed = Convert.ToDouble(max_vel.Text);
            acc_time = Convert.ToDouble(acc.Text);

            unsafe
            {
                fixed (double* position_ref = position_array) fixed (Int16* axis_ref = axis_array) PROSYS.GT_PROSYS_U3_axis_move(rel_abs, Total_axis_to_move, axis_ref, position_ref, low_speed, max_speed, acc_time);
            }
        }

        private void button31_Click(object sender, EventArgs e)
        {
            Int16 L1;
            
            
            //Int16[] axis_array = new Int16[3];
            //double[] position_array = new double[5];
            //Int16 rel_abs;
            //Int16 Total_axis_to_move = 1;
            //double low_speed;
            //double max_speed;
            //double acc_time;

            //rel_abs = Convert.ToInt16(relabs.Text);
            //axis_array[0] = Convert.ToInt16(axis.Text);
            //position_array[0] = Convert.ToDouble(count.Text);
            //low_speed = Convert.ToDouble(str_vel.Text);
            //max_speed = Convert.ToDouble(max_vel.Text);
            //acc_time = Convert.ToDouble(acc.Text);

            //unsafe
            //{
            //    fixed (double* position_ref = position_array) fixed (Int16* axis_ref = axis_array) PROSYS.GT_PROSYS_U3_axis_move(rel_abs, Total_axis_to_move, axis_ref, position_ref, low_speed, max_speed, acc_time);
            //}
            //L1 = Convert.ToInt16(tbDO.Text);

            PROSYS.GT_PROSYS_U3_set_do_bit(0, 10);

            PROSYS.GT_PROSYS_U3_set_do_bit(0, 17);
        }

        private void button32_Click(object sender, EventArgs e)
        {
            
            uint L1;
            L1 = 1000;
            for (UInt16 loop = 0; loop <= 50; loop++)
            {
                
                PROSYS.GT_PROSYS_U3_galvo_move_XY((int)(XORIGIN - (L1 / 2)), (int)(YORIGIN), gspeed, XOFFSET, YOFFSET, THETA);
                
                PROSYS.GT_PROSYS_U3_galvo_move_XY((int)XORIGIN, (int)(YORIGIN + (L1 / 2)), gspeed, XOFFSET, YOFFSET, THETA);
                
                PROSYS.GT_PROSYS_U3_galvo_move_XY((int)(XORIGIN + (L1 / 2)), (int)(YORIGIN), gspeed, XOFFSET, YOFFSET, THETA);
                
                PROSYS.GT_PROSYS_U3_galvo_move_XY((int)XORIGIN, (int)(YORIGIN - (L1 / 2)), gspeed, XOFFSET, YOFFSET, THETA);
               
              PROSYS.GT_PROSYS_U3_galvo_move_XY((int)(XORIGIN - (L1 / 2)), (int)(YORIGIN), gspeed, XOFFSET, YOFFSET, THETA);

                L1 =L1+1000;
                
            }

            while (PROSYS.GT_PROSYS_U3_buffer_ready() == 1)
            {
                Application.DoEvents();
            }

           
        }

        private void button33_Click(object sender, EventArgs e)
        {
            Int16 Ex_axis;
            Ex_axis = Convert.ToInt16(axis.Text);
            PROSYS.GT_PROSYS_U3_buf_exclude_axis(Ex_axis);
        }

        private void button34_Click(object sender, EventArgs e)
        {
            Int16 In_axis;
            In_axis = Convert.ToInt16(axis.Text);
            PROSYS.GT_PROSYS_U3_buf_include_axis(In_axis);
        }
        



         
      

     

    }
}



namespace MicroLibrary
{
    /// <summary>
    /// MicroStopwatch class
    /// </summary>
    public class MicroStopwatch : System.Diagnostics.Stopwatch
    {
        readonly double _microSecPerTick =
            1000000D / System.Diagnostics.Stopwatch.Frequency;

        public MicroStopwatch()
        {
            if (!System.Diagnostics.Stopwatch.IsHighResolution)
            {
                throw new Exception("On this system the high-resolution " +
                                    "performance counter is not available");
            }
        }

        public long ElapsedMicroseconds
        {
            get
            {
                return (long)(ElapsedTicks * _microSecPerTick);
            }
        }
    }

    /// <summary>
    /// MicroTimer class
    /// </summary>
    public class MicroTimer
    {
        public delegate void MicroTimerElapsedEventHandler(
                             object sender,
                             MicroTimerEventArgs timerEventArgs);
        public event MicroTimerElapsedEventHandler MicroTimerElapsed;

        System.Threading.Thread _threadTimer = null;
        long _ignoreEventIfLateBy = long.MaxValue;
        long _timerIntervalInMicroSec = 0;
        bool _stopTimer = true;

        public MicroTimer()
        {
        }

        public MicroTimer(long timerIntervalInMicroseconds)
        {
            Interval = timerIntervalInMicroseconds;
        }

        public long Interval
        {
            get
            {
                return System.Threading.Interlocked.Read(
                    ref _timerIntervalInMicroSec);
            }
            set
            {
                System.Threading.Interlocked.Exchange(
                    ref _timerIntervalInMicroSec, value);
            }
        }

        public long IgnoreEventIfLateBy
        {
            get
            {
                return System.Threading.Interlocked.Read(
                    ref _ignoreEventIfLateBy);
            }
            set
            {
                System.Threading.Interlocked.Exchange(
                    ref _ignoreEventIfLateBy, value <= 0 ? long.MaxValue : value);
            }
        }

        public bool Enabled
        {
            set
            {
                if (value)
                {
                    Start();
                }
                else
                {
                    Stop();
                }
            }
            get
            {
                return (_threadTimer != null && _threadTimer.IsAlive);
            }
        }

        public void Start()
        {
            if (Enabled || Interval <= 0)
            {
                return;
            }

            _stopTimer = false;

            System.Threading.ThreadStart threadStart = delegate()
            {
                NotificationTimer(ref _timerIntervalInMicroSec,
                                  ref _ignoreEventIfLateBy,
                                  ref _stopTimer);
            };

            _threadTimer = new System.Threading.Thread(threadStart);
            _threadTimer.Priority = System.Threading.ThreadPriority.Highest;
            _threadTimer.Start();
        }

        public void Stop()
        {
            _stopTimer = true;
        }

        public void StopAndWait()
        {
            StopAndWait(System.Threading.Timeout.Infinite);
        }

        public bool StopAndWait(int timeoutInMilliSec)
        {
            _stopTimer = true;

            if (!Enabled || _threadTimer.ManagedThreadId ==
                System.Threading.Thread.CurrentThread.ManagedThreadId)
            {
                return true;
            }

            return _threadTimer.Join(timeoutInMilliSec);
        }

        public void Abort()
        {
            _stopTimer = true;

            if (Enabled)
            {
                _threadTimer.Abort();
            }
        }

        void NotificationTimer(ref long timerIntervalInMicroSec,
                               ref long ignoreEventIfLateBy,
                               ref bool stopTimer)
        {
            int timerCount = 0;
            long nextNotification = 0;

            MicroStopwatch microStopwatch = new MicroStopwatch();
            microStopwatch.Start();

            while (!stopTimer)
            {
                long callbackFunctionExecutionTime =
                    microStopwatch.ElapsedMicroseconds - nextNotification;

                long timerIntervalInMicroSecCurrent =
                    System.Threading.Interlocked.Read(ref timerIntervalInMicroSec);
                long ignoreEventIfLateByCurrent =
                    System.Threading.Interlocked.Read(ref ignoreEventIfLateBy);

                nextNotification += timerIntervalInMicroSecCurrent;
                timerCount++;
                long elapsedMicroseconds = 0;

                while ((elapsedMicroseconds = microStopwatch.ElapsedMicroseconds)
                        < nextNotification)
                {
                    System.Threading.Thread.SpinWait(10);
                }

                long timerLateBy = elapsedMicroseconds - nextNotification;

                if (timerLateBy >= ignoreEventIfLateByCurrent)
                {
                    continue;
                }

                MicroTimerEventArgs microTimerEventArgs =
                     new MicroTimerEventArgs(timerCount,
                                             elapsedMicroseconds,
                                             timerLateBy,
                                             callbackFunctionExecutionTime);
                MicroTimerElapsed(this, microTimerEventArgs);
            }

            microStopwatch.Stop();
        }
    }

    /// <summary>
    /// MicroTimer Event Argument class
    /// </summary>
    public class MicroTimerEventArgs : EventArgs
    {
        // Simple counter, number times timed event (callback function) executed
        public int TimerCount { get; private set; }

        // Time when timed event was called since timer started
        public long ElapsedMicroseconds { get; private set; }

        // How late the timer was compared to when it should have been called
        public long TimerLateBy { get; private set; }

        // Time it took to execute previous call to callback function (OnTimedEvent)
        public long CallbackFunctionExecutionTime { get; private set; }

        public MicroTimerEventArgs(int timerCount,
                                   long elapsedMicroseconds,
                                   long timerLateBy,
                                   long callbackFunctionExecutionTime)
        {
            TimerCount = timerCount;
            ElapsedMicroseconds = elapsedMicroseconds;
            TimerLateBy = timerLateBy;
            CallbackFunctionExecutionTime = callbackFunctionExecutionTime;
        }

    }
}
