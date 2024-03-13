module MCPU_Alu(cmd,in1,in2,out,CF);
parameter CMD_SIZE=3;
parameter WORD_SIZE=16;

parameter  [CMD_SIZE-1:0]  CMD_AND  = 0; //3'b000
parameter  [CMD_SIZE-1:0]  CMD_OR   = 1; //3'b001
parameter  [CMD_SIZE-1:0]  CMD_XOR  = 2; //3'b010
parameter  [CMD_SIZE-1:0]  CMD_ADD  = 3; //3'b011
parameter  [CMD_SIZE-1:0]  CMD_LSL  = 4; //3'b100
parameter  [CMD_SIZE-1:0]  CMD_LSR  = 5; //3'b101
parameter  [CMD_SIZE-1:0]  CMD_MUL  = 6; //3'b110
parameter  [CMD_SIZE-1:0]  CMD_DIV  = 7; //3'b111

input [CMD_SIZE-1:0] cmd;
input [WORD_SIZE-1:0] in1;
input [WORD_SIZE-1:0] in2;
output[WORD_SIZE*2-1:0] out;
//carry flag
output CF;

wire [CMD_SIZE-1:0] cmd;
wire [WORD_SIZE-1:0] in1;
wire [WORD_SIZE-1:0] in2;
reg  [WORD_SIZE*2-1:0] out;
//carry flag
reg  CF;

always @ (cmd, in1, in2)
  #2
case(cmd)
  CMD_AND : begin
               out = in1&in2; 
            end
  CMD_OR : begin
              out = in1|in2;
            end
  CMD_XOR : begin
              out = in1^in2;
            end
  CMD_LSL : begin
              {CF,out} = in1*(2**(in2));
            end
  CMD_LSR : begin
              {CF,out} = in1/(2**(in2));
            end
  CMD_MUL : begin
              {CF,out} = in1*in2;
            end
  CMD_DIV : begin
              {CF,out} = in1/in2;
            end
  default : begin
              {CF,out} = in1+in2;
            end
 endcase

endmodule