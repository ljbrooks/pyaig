


module adder(input [3:0] a,
             input [3:0]  b,
             input        cin,
             output [3:0] sum,
             output       cout) ;
   wire [4:0]             x = a+b + cin;
   assign sum = x[3:0];

   assign cout = x[4];
   
endmodule
