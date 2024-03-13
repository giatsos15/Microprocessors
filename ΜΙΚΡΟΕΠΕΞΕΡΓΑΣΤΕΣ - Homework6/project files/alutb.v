module MCPU_Alutb();

parameter CMD_SIZE=2;
parameter WORD_SIZE=2;

reg [CMD_SIZE-1:0] opcode;
reg [WORD_SIZE-1:0] r1;
reg [WORD_SIZE-1:0] r2;
wire [WORD_SIZE*2-1:0] out;
wire OVERFLOW;
reg iscorrect;

MCPU_Alu #(.CMD_SIZE(CMD_SIZE), .WORD_SIZE(WORD_SIZE)) aluinst (opcode, r1, r2, out, OVERFLOW);

// Testbench code goes here
always #2 r1[0] = $random;
always #2 r2[0] = $random;
always #2 r1[1] = $random;
always #2 r2[1] = $random;

always #2 opcode[0] = $random;
always #2 opcode[1] = $random;

always @ (out)
  #3
begin
  if (opcode == 0) begin
    if (out == r1&r2) begin
      iscorrect = 1;
    end else begin
      iscorrect = 0;
    end
  end else if (opcode == 1) begin
    if (out == r1|r2) begin
      iscorrect = 1;
    end else begin
      iscorrect = 0;
    end
  end else if (opcode == 2) begin
    if (out == r1^r2) begin
      iscorrect = 1;
    end else begin
      iscorrect = 0;
    end
  end else if (opcode == 3) begin
    if ({OVERFLOW,out} == r1+r2) begin
      iscorrect = 1;
    end else begin
      iscorrect = 0;
    end
  end
end
  
initial begin
  $display("@%0dns default is selected, opcode %b",$time,opcode);
end


endmodule
