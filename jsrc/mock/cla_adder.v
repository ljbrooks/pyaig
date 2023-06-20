module cla_adder
        (   input [3:0] A,B,
            input cin,
            output [3:0] S,
            output cout
            );
            
wire [3:0] P,G;
wire [4:0] C;   
    
//first level
assign P = A ^ B;
assign G = A & B;

//second level
cla_block gen_c(P,G,cin,C);

//third level
assign S = P ^ C[3:0];
assign cout = C[4];

endmodule

