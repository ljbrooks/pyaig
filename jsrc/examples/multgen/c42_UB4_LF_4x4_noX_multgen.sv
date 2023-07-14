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

module c42_UB4_LF_4x4_noX(
        input logic [3:0] IN1,
        input logic [3:0] IN2,
        output logic [7:0] result);
    
    
// Creating Partial Products 

    wire [4:0] mult = {1'b0, IN1};
    wire [4:0] mcand = {1'b0, IN2};
    wire [5:0] mcand_1x;
    wire [5:0] mcand_2x;
    assign mcand_1x = {{1{mcand[4]}},  mcand};
    assign mcand_2x = {{0{mcand[4]}},  mcand, 1'b0};
    
    // Booth Radix-4 Partial Products. Multiplier selectors: mult[1] mult[0] 1'b0
    wire logic select_0_0, select_e_0, select_2x_0, tcomp0, select_ne_0, select_n2x_0;
    assign select_0_0 =  &{mult[1], mult[0], 1'b0} | ~|{mult[1], mult[0], 1'b0};
    assign select_e_0 = ((~ mult[1]) & (mult[0] ^ 1'b0));
    assign select_ne_0 = mult[1] &  (mult[0] ^ 1'b0);
    assign select_2x_0 = (~ mult[1]) & mult[0] & 1'b0;
    assign select_n2x_0 = mult[1] & (~ mult[0]) & (~ 1'b0);
    reg [5:0] pp_0;
    always @(*) begin
       case (1'b1)
          select_0_0   : pp_0 = 0; 
          select_e_0   : pp_0 = mcand_1x; 
          select_2x_0  : pp_0 = mcand_2x; 
          select_n2x_0 : pp_0 = (~ mcand_2x); 
          select_ne_0  : pp_0 = (~ mcand_1x); 
          default  : pp_0 = 0; 
       endcase 
       pp_0[5] = ~pp_0[5]; // flip the MSB 
    end
    assign tcomp0 =  select_n2x_0 | select_ne_0;
    
    // Booth Radix-4 Partial Products. Multiplier selectors: mult[3] mult[2] mult[1]
    wire logic select_0_1, select_e_1, select_2x_1, tcomp1, select_ne_1, select_n2x_1;
    assign select_0_1 =  &{mult[3], mult[2], mult[1]} | ~|{mult[3], mult[2], mult[1]};
    assign select_e_1 = ((~ mult[3]) & (mult[2] ^ mult[1]));
    assign select_ne_1 = mult[3] &  (mult[2] ^ mult[1]);
    assign select_2x_1 = (~ mult[3]) & mult[2] & mult[1];
    assign select_n2x_1 = mult[3] & (~ mult[2]) & (~ mult[1]);
    reg [5:0] pp_1;
    always @(*) begin
       case (1'b1)
          select_0_1   : pp_1 = 0; 
          select_e_1   : pp_1 = mcand_1x; 
          select_2x_1  : pp_1 = mcand_2x; 
          select_n2x_1 : pp_1 = (~ mcand_2x); 
          select_ne_1  : pp_1 = (~ mcand_1x); 
          default  : pp_1 = 0; 
       endcase 
       pp_1[5] = ~pp_1[5]; // flip the MSB 
    end
    assign tcomp1 =  select_n2x_1 | select_ne_1;
    
    // Booth Radix-4 Partial Products. Multiplier selectors: mult[4] mult[4] mult[3]
    wire logic select_0_2, select_e_2, select_2x_2, tcomp2, select_ne_2, select_n2x_2;
    assign select_0_2 =  &{mult[4], mult[4], mult[3]} | ~|{mult[4], mult[4], mult[3]};
    assign select_e_2 = ((~ mult[4]) & (mult[4] ^ mult[3]));
    assign select_ne_2 = mult[4] &  (mult[4] ^ mult[3]);
    assign select_2x_2 = (~ mult[4]) & mult[4] & mult[3];
    assign select_n2x_2 = mult[4] & (~ mult[4]) & (~ mult[3]);
    reg [5:0] pp_2;
    always @(*) begin
       case (1'b1)
          select_0_2   : pp_2 = 0; 
          select_e_2   : pp_2 = mcand_1x; 
          select_2x_2  : pp_2 = mcand_2x; 
          select_n2x_2 : pp_2 = (~ mcand_2x); 
          select_ne_2  : pp_2 = (~ mcand_1x); 
          default  : pp_2 = 0; 
       endcase 
       pp_2[5] = ~pp_2[5]; // flip the MSB 
    end
    assign tcomp2 =  select_n2x_2 | select_ne_2;
    
    // The values to be summed in the summation tree, from LSB (left) to MSB:
     // pp_0[0] pp_0[1] pp_0[2] pp_0[3] pp_0[4] pp_0[5]   --      --      --      --    
     //   --      --    pp_1[0] pp_1[1] pp_1[2] pp_1[3] pp_1[4] pp_1[5]   --      --    
     //   --      --      --      --    pp_2[0] pp_2[1] pp_2[2] pp_2[3] pp_2[4] pp_2[5] 
     // tcomp0    --    tcomp1    --    tcomp2    --      --      --      --      --    
     //   --      --      --      --      --    1'b1    1'b1      --    1'b1      --    
    
// Creating Summation Tree 

    
    // 4to2 compressor tree Stage 1
    
    wire cout0;
    wire [5:0] sum0;
    wire [5:0] carry0;
    Four2Two #(6) cmp42_0(
            .in1({pp_1[5:4], pp_0[5:2]}),
            .in2({pp_2[3:2], pp_1[3:0]}),
            .in3({1'b0, 1'b1, pp_2[1:0], 1'b0, tcomp1}),
            .in4({2'b0, 1'b1, tcomp2, 2'b0}),
            .cin(1'b0),
            .sum(sum0),
            .carry(carry0),
            .cout(cout0));
    
    logic [8:0] adder_result;
    LF_8 final_adder ({carry0[4], carry0[3], carry0[2], carry0[1], carry0[0], sum0[0], pp_0[1], pp_0[0] }, {sum0[5], sum0[4], sum0[3], sum0[2], sum0[1], 1'b0, 1'b0, tcomp0 }, adder_result );
    assign result[7:0] = adder_result[7:0];
endmodule



module LF_8 ( 
        input logic [7:0] IN1,
        input logic [7:0] IN2,
        output logic [8:0] OUT);
    
    wire logic [7:0] p_0;
    wire logic [7:0] g_0;
    assign g_0 = IN1 & IN2;
    assign p_0 = IN1 ^ IN2;
    
// Ladner-Fischer Adder 

    
    // LF stage 1
    wire logic p_1_1;
    wire logic g_1_1;
    assign p_1_1 = p_0[1] & p_0[0];
    assign g_1_1 = (p_0[1] & g_0[0]) | g_0[1];
    wire logic p_1_3;
    wire logic g_1_3;
    assign p_1_3 = p_0[3] & p_0[2];
    assign g_1_3 = (p_0[3] & g_0[2]) | g_0[3];
    wire logic p_1_5;
    wire logic g_1_5;
    assign p_1_5 = p_0[5] & p_0[4];
    assign g_1_5 = (p_0[5] & g_0[4]) | g_0[5];
    wire logic p_1_7;
    wire logic g_1_7;
    assign p_1_7 = p_0[7] & p_0[6];
    assign g_1_7 = (p_0[7] & g_0[6]) | g_0[7];
    
    // LF stage 2
    wire logic p_2_2;
    wire logic g_2_2;
    assign p_2_2 = p_0[2] & p_1_1;
    assign g_2_2 = (p_0[2] & g_1_1) | g_0[2];
    wire logic p_2_3;
    wire logic g_2_3;
    assign p_2_3 = p_1_3 & p_1_1;
    assign g_2_3 = (p_1_3 & g_1_1) | g_1_3;
    wire logic p_2_6;
    wire logic g_2_6;
    assign p_2_6 = p_0[6] & p_1_5;
    assign g_2_6 = (p_0[6] & g_1_5) | g_0[6];
    wire logic p_2_7;
    wire logic g_2_7;
    assign p_2_7 = p_1_7 & p_1_5;
    assign g_2_7 = (p_1_7 & g_1_5) | g_1_7;
    
    // LF stage 3
    wire logic p_3_4;
    wire logic g_3_4;
    assign p_3_4 = p_0[4] & p_2_3;
    assign g_3_4 = (p_0[4] & g_2_3) | g_0[4];
    wire logic p_3_5;
    wire logic g_3_5;
    assign p_3_5 = p_1_5 & p_2_3;
    assign g_3_5 = (p_1_5 & g_2_3) | g_1_5;
    wire logic p_3_6;
    wire logic g_3_6;
    assign p_3_6 = p_2_6 & p_2_3;
    assign g_3_6 = (p_2_6 & g_2_3) | g_2_6;
    wire logic p_3_7;
    wire logic g_3_7;
    assign p_3_7 = p_2_7 & p_2_3;
    assign g_3_7 = (p_2_7 & g_2_3) | g_2_7;
    
    // LF postprocess 
    assign OUT[0] = p_0[0];
    assign OUT[1] = p_0[1] ^ g_0[0];
    assign OUT[2] = p_0[2] ^ g_1_1;
    assign OUT[3] = p_0[3] ^ g_2_2;
    assign OUT[4] = p_0[4] ^ g_2_3;
    assign OUT[5] = p_0[5] ^ g_3_4;
    assign OUT[6] = p_0[6] ^ g_3_5;
    assign OUT[7] = p_0[7] ^ g_3_6;
    assign OUT[8] = g_3_7;
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




