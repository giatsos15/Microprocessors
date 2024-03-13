module MCPU_RAMControllertbam();
parameter WORD_SIZE=12;
parameter ADDR_WIDTH=8;
parameter RAM_SIZE=1<<ADDR_WIDTH;

reg we, re;
integer i;

reg [WORD_SIZE-1:0] datawr;
reg [ADDR_WIDTH-1:0] addr;
reg [ADDR_WIDTH-1:0] instraddr;
wire [WORD_SIZE-1:0] datard;
wire [WORD_SIZE-1:0] instrrd;
reg [WORD_SIZE-1:0] mem1[RAM_SIZE-1:0];
reg memiscorrect;

MCPU_RAMController#(.WORD_SIZE(WORD_SIZE), .ADDR_WIDTH(ADDR_WIDTH), .RAM_SIZE(RAM_SIZE)) ramcontrollerinst(we, datawr, re, addr, datard, instraddr, instrrd);
 
initial begin
  for(i=0; i<RAM_SIZE; i= i + 1) begin
    mem1[i] = 3202;
    ramcontrollerinst.mem[i] = mem1[i];
  end
  for(i=0; i<RAM_SIZE; i= i + 1) begin
    if(mem1[i] == ramcontrollerinst.mem[i]) begin
      memiscorrect = 1;
    end else begin
      memiscorrect = 0;
    end
  end    
end

endmodule 



