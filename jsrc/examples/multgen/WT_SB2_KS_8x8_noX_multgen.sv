// Note: The license below is based on the template at:
// http://opensource.org/licenses/BSD-3-Clause
// Copyright (C) 2020 Regents of the University of Texas
//All rights reserved.

// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are
// met:

// o Redistributions of source code must retain the above copyright
//   notice, this list of conditions and the following disclaimer.

// o Redistributions in binary form must reproduce the above copyright
//   notice, this list of conditions and the following disclaimer in the
//   documentation and/or other materials provided with the distribution.

// o Neither the name of the copyright holders nor the names of its
//   contributors may be used to endorse or promote products derived
//   from this software without specific prior written permission.

// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
// "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
// LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
// A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
// HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
// SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
// LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
// DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
// THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
// (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
// OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

// Original Author(s):
// Mertcan Temel         <mert@utexas.edu>

// DO NOT REMOVE:
// This file is generated by Temel's multiplier generator. Download from https://github.com/temelmertcan/multgen.

module WT_SB2_KS_8x8_noX(
        input logic [7:0] IN1,
        input logic [7:0] IN2,
        output logic [15:0] result);
    
    
// Creating Partial Products 

    wire [7:0] mult = IN1;
    wire [7:0] mcand = IN2;
    
    // Booth Radix-2 Partial Products. Multiplier selectors: mult[0] 1'b0
    wire logic select_e_0, tcomp0, select_ne_0;
    assign select_e_0 = ~mult[0] & 1'b0;
    assign select_ne_0 = mult[0] & ~1'b0;
    wire [7:0] pp_0;
    assign pp_0 = (1<<7) ^ // flip the MSB 
                   ((select_e_0 ? mcand : 0) | 
                    (select_ne_0 ? (~ mcand) : 0)); 
    assign tcomp0 = select_ne_0;
    
    // Booth Radix-2 Partial Products. Multiplier selectors: mult[1] mult[0]
    wire logic select_e_1, tcomp1, select_ne_1;
    assign select_e_1 = ~mult[1] & mult[0];
    assign select_ne_1 = mult[1] & ~mult[0];
    wire [7:0] pp_1;
    assign pp_1 = (1<<7) ^ // flip the MSB 
                   ((select_e_1 ? mcand : 0) | 
                    (select_ne_1 ? (~ mcand) : 0)); 
    assign tcomp1 = select_ne_1;
    
    // Booth Radix-2 Partial Products. Multiplier selectors: mult[2] mult[1]
    wire logic select_e_2, tcomp2, select_ne_2;
    assign select_e_2 = ~mult[2] & mult[1];
    assign select_ne_2 = mult[2] & ~mult[1];
    wire [7:0] pp_2;
    assign pp_2 = (1<<7) ^ // flip the MSB 
                   ((select_e_2 ? mcand : 0) | 
                    (select_ne_2 ? (~ mcand) : 0)); 
    assign tcomp2 = select_ne_2;
    
    // Booth Radix-2 Partial Products. Multiplier selectors: mult[3] mult[2]
    wire logic select_e_3, tcomp3, select_ne_3;
    assign select_e_3 = ~mult[3] & mult[2];
    assign select_ne_3 = mult[3] & ~mult[2];
    wire [7:0] pp_3;
    assign pp_3 = (1<<7) ^ // flip the MSB 
                   ((select_e_3 ? mcand : 0) | 
                    (select_ne_3 ? (~ mcand) : 0)); 
    assign tcomp3 = select_ne_3;
    
    // Booth Radix-2 Partial Products. Multiplier selectors: mult[4] mult[3]
    wire logic select_e_4, tcomp4, select_ne_4;
    assign select_e_4 = ~mult[4] & mult[3];
    assign select_ne_4 = mult[4] & ~mult[3];
    wire [7:0] pp_4;
    assign pp_4 = (1<<7) ^ // flip the MSB 
                   ((select_e_4 ? mcand : 0) | 
                    (select_ne_4 ? (~ mcand) : 0)); 
    assign tcomp4 = select_ne_4;
    
    // Booth Radix-2 Partial Products. Multiplier selectors: mult[5] mult[4]
    wire logic select_e_5, tcomp5, select_ne_5;
    assign select_e_5 = ~mult[5] & mult[4];
    assign select_ne_5 = mult[5] & ~mult[4];
    wire [7:0] pp_5;
    assign pp_5 = (1<<7) ^ // flip the MSB 
                   ((select_e_5 ? mcand : 0) | 
                    (select_ne_5 ? (~ mcand) : 0)); 
    assign tcomp5 = select_ne_5;
    
    // Booth Radix-2 Partial Products. Multiplier selectors: mult[6] mult[5]
    wire logic select_e_6, tcomp6, select_ne_6;
    assign select_e_6 = ~mult[6] & mult[5];
    assign select_ne_6 = mult[6] & ~mult[5];
    wire [7:0] pp_6;
    assign pp_6 = (1<<7) ^ // flip the MSB 
                   ((select_e_6 ? mcand : 0) | 
                    (select_ne_6 ? (~ mcand) : 0)); 
    assign tcomp6 = select_ne_6;
    
    // Booth Radix-2 Partial Products. Multiplier selectors: mult[7] mult[6]
    wire logic select_e_7, tcomp7, select_ne_7;
    assign select_e_7 = ~mult[7] & mult[6];
    assign select_ne_7 = mult[7] & ~mult[6];
    wire [7:0] pp_7;
    assign pp_7 = (1<<7) ^ // flip the MSB 
                   ((select_e_7 ? mcand : 0) | 
                    (select_ne_7 ? (~ mcand) : 0)); 
    assign tcomp7 = select_ne_7;
    
    // The values to be summed in the summation tree, from LSB (left) to MSB:
     // pp_0[0] pp_0[1] pp_0[2] pp_0[3] pp_0[4] pp_0[5] pp_0[6] pp_0[7]   --      --      --      --      --      --      --      --    
     //   --    pp_1[0] pp_1[1] pp_1[2] pp_1[3] pp_1[4] pp_1[5] pp_1[6] pp_1[7]   --      --      --      --      --      --      --    
     //   --      --    pp_2[0] pp_2[1] pp_2[2] pp_2[3] pp_2[4] pp_2[5] pp_2[6] pp_2[7]   --      --      --      --      --      --    
     //   --      --      --    pp_3[0] pp_3[1] pp_3[2] pp_3[3] pp_3[4] pp_3[5] pp_3[6] pp_3[7]   --      --      --      --      --    
     //   --      --      --      --    pp_4[0] pp_4[1] pp_4[2] pp_4[3] pp_4[4] pp_4[5] pp_4[6] pp_4[7]   --      --      --      --    
     //   --      --      --      --      --    pp_5[0] pp_5[1] pp_5[2] pp_5[3] pp_5[4] pp_5[5] pp_5[6] pp_5[7]   --      --      --    
     //   --      --      --      --      --      --    pp_6[0] pp_6[1] pp_6[2] pp_6[3] pp_6[4] pp_6[5] pp_6[6] pp_6[7]   --      --    
     //   --      --      --      --      --      --      --    pp_7[0] pp_7[1] pp_7[2] pp_7[3] pp_7[4] pp_7[5] pp_7[6] pp_7[7]   --    
     // tcomp0  tcomp1  tcomp2  tcomp3  tcomp4  tcomp5  tcomp6  tcomp7    --      --      --      --      --      --      --      --    
     //   --      --      --      --      --      --      --    1'b1      --      --      --      --      --      --      --    1'b1    
    
// Creating Summation Tree 

    
    // Wallace Summation Stage 1
    logic s0 ,c0;
    ha ha0 (pp_0[0], tcomp0, s0, c0);
    logic s1 ,c1; 
    fa fa1 (pp_0[1], pp_1[0], tcomp1, s1, c1);
    logic s2 ,c2; 
    fa fa2 (pp_0[2], pp_1[1], pp_2[0], s2, c2);
    logic s3 ,c3; 
    fa fa3 (pp_0[3], pp_1[2], pp_2[1], s3, c3);
    logic s4 ,c4;
    ha ha4 (pp_3[0], tcomp3, s4, c4);
    logic s5 ,c5; 
    fa fa5 (pp_0[4], pp_1[3], pp_2[2], s5, c5);
    logic s6 ,c6; 
    fa fa6 (pp_3[1], pp_4[0], tcomp4, s6, c6);
    logic s7 ,c7; 
    fa fa7 (pp_0[5], pp_1[4], pp_2[3], s7, c7);
    logic s8 ,c8; 
    fa fa8 (pp_3[2], pp_4[1], pp_5[0], s8, c8);
    logic s9 ,c9; 
    fa fa9 (pp_0[6], pp_1[5], pp_2[4], s9, c9);
    logic s10 ,c10; 
    fa fa10 (pp_3[3], pp_4[2], pp_5[1], s10, c10);
    logic s11 ,c11;
    ha ha11 (pp_6[0], tcomp6, s11, c11);
    logic s12 ,c12; 
    fa fa12 (pp_0[7], pp_1[6], pp_2[5], s12, c12);
    logic s13 ,c13; 
    fa fa13 (pp_3[4], pp_4[3], pp_5[2], s13, c13);
    logic s14 ,c14; 
    fa fa14 (pp_6[1], pp_7[0], tcomp7, s14, c14);
    logic s15 ,c15; 
    fa fa15 (pp_1[7], pp_2[6], pp_3[5], s15, c15);
    logic s16 ,c16; 
    fa fa16 (pp_4[4], pp_5[3], pp_6[2], s16, c16);
    logic s17 ,c17; 
    fa fa17 (pp_2[7], pp_3[6], pp_4[5], s17, c17);
    logic s18 ,c18; 
    fa fa18 (pp_5[4], pp_6[3], pp_7[2], s18, c18);
    logic s19 ,c19; 
    fa fa19 (pp_3[7], pp_4[6], pp_5[5], s19, c19);
    logic s20 ,c20;
    ha ha20 (pp_6[4], pp_7[3], s20, c20);
    logic s21 ,c21; 
    fa fa21 (pp_4[7], pp_5[6], pp_6[5], s21, c21);
    logic s22 ,c22; 
    fa fa22 (pp_5[7], pp_6[6], pp_7[5], s22, c22);
    logic s23 ,c23;
    ha ha23 (pp_6[7], pp_7[6], s23, c23);
    
    // Wallace Summation Stage 2
    logic s24 ,c24;
    ha ha24 (c0, s1, s24, c24);
    logic s25 ,c25; 
    fa fa25 (tcomp2, c1, s2, s25, c25);
    logic s26 ,c26; 
    fa fa26 (c2, s3, s4, s26, c26);
    logic s27 ,c27; 
    fa fa27 (c3, c4, s5, s27, c27);
    logic s28 ,c28; 
    fa fa28 (tcomp5, c5, c6, s28, c28);
    logic s29 ,c29;
    ha ha29 (s7, s8, s29, c29);
    logic s30 ,c30; 
    fa fa30 (c7, c8, s9, s30, c30);
    logic s31 ,c31;
    ha ha31 (s10, s11, s31, c31);
    logic s32 ,c32; 
    fa fa32 (1'b1, c9, c10, s32, c32);
    logic s33 ,c33; 
    fa fa33 (c11, s12, s13, s33, c33);
    logic s34 ,c34; 
    fa fa34 (pp_7[1], c12, c13, s34, c34);
    logic s35 ,c35; 
    fa fa35 (c14, s15, s16, s35, c35);
    logic s36 ,c36; 
    fa fa36 (c15, c16, s17, s36, c36);
    logic s37 ,c37; 
    fa fa37 (c17, c18, s19, s37, c37);
    logic s38 ,c38; 
    fa fa38 (pp_7[4], c19, c20, s38, c38);
    logic s39 ,c39;
    ha ha39 (c21, s22, s39, c39);
    logic s40 ,c40;
    ha ha40 (c22, s23, s40, c40);
    logic s41 ,c41;
    ha ha41 (pp_7[7], c23, s41, c41);
    
    // Wallace Summation Stage 3
    logic s42 ,c42;
    ha ha42 (c24, s25, s42, c42);
    logic s43 ,c43;
    ha ha43 (c25, s26, s43, c43);
    logic s44 ,c44; 
    fa fa44 (s6, c26, s27, s44, c44);
    logic s45 ,c45; 
    fa fa45 (c27, s28, s29, s45, c45);
    logic s46 ,c46; 
    fa fa46 (c28, c29, s30, s46, c46);
    logic s47 ,c47; 
    fa fa47 (s14, c30, c31, s47, c47);
    logic s48 ,c48;
    ha ha48 (s32, s33, s48, c48);
    logic s49 ,c49; 
    fa fa49 (c32, c33, s34, s49, c49);
    logic s50 ,c50; 
    fa fa50 (s18, c34, c35, s50, c50);
    logic s51 ,c51; 
    fa fa51 (s20, c36, s37, s51, c51);
    logic s52 ,c52; 
    fa fa52 (s21, c37, s38, s52, c52);
    logic s53 ,c53;
    ha ha53 (c38, s39, s53, c53);
    logic s54 ,c54;
    ha ha54 (c39, s40, s54, c54);
    logic s55 ,c55;
    ha ha55 (c40, s41, s55, c55);
    logic s56 ,c56;
    ha ha56 (1'b1, c41, s56, c56);
    
    // Wallace Summation Stage 4
    logic s57 ,c57;
    ha ha57 (c42, s43, s57, c57);
    logic s58 ,c58;
    ha ha58 (c43, s44, s58, c58);
    logic s59 ,c59;
    ha ha59 (c44, s45, s59, c59);
    logic s60 ,c60; 
    fa fa60 (s31, c45, s46, s60, c60);
    logic s61 ,c61; 
    fa fa61 (c46, s47, s48, s61, c61);
    logic s62 ,c62; 
    fa fa62 (s35, c47, c48, s62, c62);
    logic s63 ,c63; 
    fa fa63 (s36, c49, s50, s63, c63);
    logic s64 ,c64;
    ha ha64 (c50, s51, s64, c64);
    logic s65 ,c65;
    ha ha65 (c51, s52, s65, c65);
    logic s66 ,c66;
    ha ha66 (c52, s53, s66, c66);
    logic s67 ,c67;
    ha ha67 (c53, s54, s67, c67);
    logic s68 ,c68;
    ha ha68 (c54, s55, s68, c68);
    logic s69 ,c69;
    ha ha69 (c55, s56, s69, c69);
    
    // Wallace Summation Stage 5
    logic s70 ,c70;
    ha ha70 (c57, s58, s70, c70);
    logic s71 ,c71;
    ha ha71 (c58, s59, s71, c71);
    logic s72 ,c72;
    ha ha72 (c59, s60, s72, c72);
    logic s73 ,c73;
    ha ha73 (c60, s61, s73, c73);
    logic s74 ,c74; 
    fa fa74 (s49, c61, s62, s74, c74);
    logic s75 ,c75;
    ha ha75 (c62, s63, s75, c75);
    logic s76 ,c76;
    ha ha76 (c63, s64, s76, c76);
    logic s77 ,c77;
    ha ha77 (c64, s65, s77, c77);
    logic s78 ,c78;
    ha ha78 (c65, s66, s78, c78);
    logic s79 ,c79;
    ha ha79 (c66, s67, s79, c79);
    logic s80 ,c80;
    ha ha80 (c67, s68, s80, c80);
    logic s81 ,c81;
    ha ha81 (c68, s69, s81, c81);
    
    assign result[0] = s0;
    assign result[1] = s24;
    assign result[2] = s42;
    assign result[3] = s57;
    assign result[4] = s70;
    logic [11:0] adder_result;
    KS_11 final_adder ({c80, c79, c78, c77, c76, c75, c74, c73, c72, c71, c70 }, {s81, s80, s79, s78, s77, s76, s75, s74, s73, s72, s71 }, adder_result );
    assign result[15:5] = adder_result[10:0];
endmodule



module KS_11 ( 
        input logic [10:0] IN1,
        input logic [10:0] IN2,
        output logic [11:0] OUT);
    
    wire logic [10:0] p_0;
    wire logic [10:0] g_0;
    assign g_0 = IN1 & IN2;
    assign p_0 = IN1 ^ IN2;
    
// Kogge-Stone Adder 

    
    // KS stage 1
    wire logic p_1_1;
    wire logic g_1_1;
    assign p_1_1 = p_0[1] & p_0[0];
    assign g_1_1 = (p_0[1] & g_0[0]) | g_0[1];
    wire logic p_1_2;
    wire logic g_1_2;
    assign p_1_2 = p_0[2] & p_0[1];
    assign g_1_2 = (p_0[2] & g_0[1]) | g_0[2];
    wire logic p_1_3;
    wire logic g_1_3;
    assign p_1_3 = p_0[3] & p_0[2];
    assign g_1_3 = (p_0[3] & g_0[2]) | g_0[3];
    wire logic p_1_4;
    wire logic g_1_4;
    assign p_1_4 = p_0[4] & p_0[3];
    assign g_1_4 = (p_0[4] & g_0[3]) | g_0[4];
    wire logic p_1_5;
    wire logic g_1_5;
    assign p_1_5 = p_0[5] & p_0[4];
    assign g_1_5 = (p_0[5] & g_0[4]) | g_0[5];
    wire logic p_1_6;
    wire logic g_1_6;
    assign p_1_6 = p_0[6] & p_0[5];
    assign g_1_6 = (p_0[6] & g_0[5]) | g_0[6];
    wire logic p_1_7;
    wire logic g_1_7;
    assign p_1_7 = p_0[7] & p_0[6];
    assign g_1_7 = (p_0[7] & g_0[6]) | g_0[7];
    wire logic p_1_8;
    wire logic g_1_8;
    assign p_1_8 = p_0[8] & p_0[7];
    assign g_1_8 = (p_0[8] & g_0[7]) | g_0[8];
    wire logic p_1_9;
    wire logic g_1_9;
    assign p_1_9 = p_0[9] & p_0[8];
    assign g_1_9 = (p_0[9] & g_0[8]) | g_0[9];
    wire logic p_1_10;
    wire logic g_1_10;
    assign p_1_10 = p_0[10] & p_0[9];
    assign g_1_10 = (p_0[10] & g_0[9]) | g_0[10];
    
    // KS stage 2
    wire logic p_2_2;
    wire logic g_2_2;
    assign p_2_2 = p_1_2 & p_0[0];
    assign g_2_2 = (p_1_2 & g_0[0]) | g_1_2;
    wire logic p_2_3;
    wire logic g_2_3;
    assign p_2_3 = p_1_3 & p_1_1;
    assign g_2_3 = (p_1_3 & g_1_1) | g_1_3;
    wire logic p_2_4;
    wire logic g_2_4;
    assign p_2_4 = p_1_4 & p_1_2;
    assign g_2_4 = (p_1_4 & g_1_2) | g_1_4;
    wire logic p_2_5;
    wire logic g_2_5;
    assign p_2_5 = p_1_5 & p_1_3;
    assign g_2_5 = (p_1_5 & g_1_3) | g_1_5;
    wire logic p_2_6;
    wire logic g_2_6;
    assign p_2_6 = p_1_6 & p_1_4;
    assign g_2_6 = (p_1_6 & g_1_4) | g_1_6;
    wire logic p_2_7;
    wire logic g_2_7;
    assign p_2_7 = p_1_7 & p_1_5;
    assign g_2_7 = (p_1_7 & g_1_5) | g_1_7;
    wire logic p_2_8;
    wire logic g_2_8;
    assign p_2_8 = p_1_8 & p_1_6;
    assign g_2_8 = (p_1_8 & g_1_6) | g_1_8;
    wire logic p_2_9;
    wire logic g_2_9;
    assign p_2_9 = p_1_9 & p_1_7;
    assign g_2_9 = (p_1_9 & g_1_7) | g_1_9;
    wire logic p_2_10;
    wire logic g_2_10;
    assign p_2_10 = p_1_10 & p_1_8;
    assign g_2_10 = (p_1_10 & g_1_8) | g_1_10;
    
    // KS stage 3
    wire logic p_3_4;
    wire logic g_3_4;
    assign p_3_4 = p_2_4 & p_0[0];
    assign g_3_4 = (p_2_4 & g_0[0]) | g_2_4;
    wire logic p_3_5;
    wire logic g_3_5;
    assign p_3_5 = p_2_5 & p_1_1;
    assign g_3_5 = (p_2_5 & g_1_1) | g_2_5;
    wire logic p_3_6;
    wire logic g_3_6;
    assign p_3_6 = p_2_6 & p_2_2;
    assign g_3_6 = (p_2_6 & g_2_2) | g_2_6;
    wire logic p_3_7;
    wire logic g_3_7;
    assign p_3_7 = p_2_7 & p_2_3;
    assign g_3_7 = (p_2_7 & g_2_3) | g_2_7;
    wire logic p_3_8;
    wire logic g_3_8;
    assign p_3_8 = p_2_8 & p_2_4;
    assign g_3_8 = (p_2_8 & g_2_4) | g_2_8;
    wire logic p_3_9;
    wire logic g_3_9;
    assign p_3_9 = p_2_9 & p_2_5;
    assign g_3_9 = (p_2_9 & g_2_5) | g_2_9;
    wire logic p_3_10;
    wire logic g_3_10;
    assign p_3_10 = p_2_10 & p_2_6;
    assign g_3_10 = (p_2_10 & g_2_6) | g_2_10;
    
    // KS stage 4
    wire logic p_4_8;
    wire logic g_4_8;
    assign p_4_8 = p_3_8 & p_0[0];
    assign g_4_8 = (p_3_8 & g_0[0]) | g_3_8;
    wire logic p_4_9;
    wire logic g_4_9;
    assign p_4_9 = p_3_9 & p_1_1;
    assign g_4_9 = (p_3_9 & g_1_1) | g_3_9;
    wire logic p_4_10;
    wire logic g_4_10;
    assign p_4_10 = p_3_10 & p_2_2;
    assign g_4_10 = (p_3_10 & g_2_2) | g_3_10;
    
    // KS postprocess 
    assign OUT[0] = p_0[0];
    assign OUT[1] = p_0[1] ^ g_0[0];
    assign OUT[2] = p_0[2] ^ g_1_1;
    assign OUT[3] = p_0[3] ^ g_2_2;
    assign OUT[4] = p_0[4] ^ g_2_3;
    assign OUT[5] = p_0[5] ^ g_3_4;
    assign OUT[6] = p_0[6] ^ g_3_5;
    assign OUT[7] = p_0[7] ^ g_3_6;
    assign OUT[8] = p_0[8] ^ g_3_7;
    assign OUT[9] = p_0[9] ^ g_4_8;
    assign OUT[10] = p_0[10] ^ g_4_9;
    assign OUT[11] = g_4_10;
endmodule

module ha (
        input logic a,
        input logic b,
        output logic s,
        output logic c);
    
    assign s = a ^ b;
    assign c = a & b;
endmodule



module fa (
        input logic x,
        input logic y,
        input logic z,
        output logic s,
        output logic c);
    
    assign s = x ^ y ^ z;
    assign c = (x & y) | (x & z) | (y & z);
endmodule

module Four2Two 
        #(parameter WIDTH=1) (
        input logic [WIDTH-1:0] in1,
        input logic [WIDTH-1:0] in2,
        input logic [WIDTH-1:0] in3,
        input logic [WIDTH-1:0] in4,
        input logic cin,
        output logic [WIDTH-1:0] sum,
        output logic [WIDTH-1:0] carry,
        output logic cout);
    
    wire logic [WIDTH:0] temp1;
    assign temp1 = {((in1 ^ in2)&in3 | in1 & ~(in1^in2)),cin};
    assign sum = ((in1 ^ in2) ^ in3 ^ in4) ^ temp1[WIDTH-1:0];
    assign carry = ((in1 ^ in2) ^ in3 ^ in4) & temp1[WIDTH-1:0] | in4 & ~((in1 ^ in2) ^ in3 ^ in4);
    assign cout = temp1[WIDTH];
endmodule




