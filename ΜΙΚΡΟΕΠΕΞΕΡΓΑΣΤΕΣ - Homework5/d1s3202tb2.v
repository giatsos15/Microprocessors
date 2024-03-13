module d1s3202tb2();
  
reg tb_a;
reg tb_b;
reg tb_c;
reg d_correct;
  
wire [2:0] tb_dut_inputs;
  
wire tb_d;
  
d1s3202 dut(tb_a, tb_b, tb_c, tb_d);
  
assign tb_dut_inputs={tb_a, tb_b, tb_c};

always @(tb_d or 1 or 0)
begin 
  if (tb_d == 1)
    d_correct = #2 1;
  else
    d_correct = #2 0;
end  

initial begin
  {tb_a, tb_b, tb_c}=3'b000;
  d_correct = 1'b0;
  forever #5 {tb_a, tb_b, tb_c}=tb_dut_inputs + 1;
end

endmodule
