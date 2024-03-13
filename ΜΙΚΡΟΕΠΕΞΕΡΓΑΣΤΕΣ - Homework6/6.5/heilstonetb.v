module MCPU_Heilstonetb();


reg reset, clk;


MCPU cpuinst (clk, reset);


initial begin
  reset=1;
  #10  reset=0;
end

always begin
  #5 clk=0; 
  #5 clk=1; 
end


/********OUR ASSEMBLER*****/

integer file, i;
reg[cpuinst.WORD_SIZE-1:0] memi;
parameter  [cpuinst.OPERAND_SIZE-1:0]  R0  = 0; //4'b0000
parameter  [cpuinst.OPERAND_SIZE-1:0]  R1  = 1; //4'b0001
parameter  [cpuinst.OPERAND_SIZE-1:0]  R2  = 2; //4'b0010
parameter  [cpuinst.OPERAND_SIZE-1:0]  R3  = 3; //4'b0011
parameter  [cpuinst.OPERAND_SIZE-1:0]  R4  = 4; //4'b0100
parameter  [cpuinst.OPERAND_SIZE-1:0]  R5  = 5; //4'b0101
parameter  [cpuinst.OPERAND_SIZE-1:0]  R6  = 6; //4'b0110
parameter  [cpuinst.OPERAND_SIZE-1:0]  R7  = 7; //4'b0111
parameter  [cpuinst.OPERAND_SIZE-1:0]  R8  = 8; //4'b1000
parameter  [cpuinst.OPERAND_SIZE-1:0]  R9  = 9; //4'b1001
parameter  [cpuinst.OPERAND_SIZE-1:0]  R10  = 10; //4'b1010
parameter  [cpuinst.OPERAND_SIZE-1:0]  R11  = 11; //4'b1011
parameter  [cpuinst.OPERAND_SIZE-1:0]  R12  = 12; //4'b1100
parameter  [cpuinst.OPERAND_SIZE-1:0]  R13  = 13; //4'b1101
parameter  [cpuinst.OPERAND_SIZE-1:0]  R14  = 14; //4'b1110
parameter  [cpuinst.OPERAND_SIZE-1:0]  R15  = 15; //4'b1111



initial
begin

    for(i=0;i<256;i=i+1)
    begin
      cpuinst.raminst.mem[i]=0;
    end
    cpuinst.regfileinst.R[0]=0;
    cpuinst.regfileinst.R[1]=0;
    cpuinst.regfileinst.R[2]=0;
    cpuinst.regfileinst.R[3]=0;
    cpuinst.regfileinst.R[4]=0;
    cpuinst.regfileinst.R[5]=0;
    cpuinst.regfileinst.R[6]=0;
    cpuinst.regfileinst.R[7]=0;
    cpuinst.regfileinst.R[8]=0;
    cpuinst.regfileinst.R[9]=0;
    cpuinst.regfileinst.R[10]=0;
    cpuinst.regfileinst.R[11]=0;
    cpuinst.regfileinst.R[12]=0;
    cpuinst.regfileinst.R[13]=0;
    cpuinst.regfileinst.R[14]=0;
    cpuinst.regfileinst.R[15]=0; 
    



                                                                              //memory address: instruction
    i=0;  cpuinst.raminst.mem[0]={cpuinst.OP_SHORT_TO_REG, R0, 8'b00000001};  // 0: n=R0 (R0=1);
    i=i+1;cpuinst.raminst.mem[i]={cpuinst.OP_STORE_TO_MEM, R0, 8'b01100100};  // 1: mem[100]=RO=n;
    i=i+1;cpuinst.raminst.mem[i]={cpuinst.OP_SHORT_TO_REG, R1, 8'b00000001};  // 2: R1=1 (FOR XOR & AND);
    i=i+1;cpuinst.raminst.mem[i]={cpuinst.OP_SHORT_TO_REG, R7, 8'b00000010};  // 3: R7=2 (FOR DIV);
    i=i+1;cpuinst.raminst.mem[i]={cpuinst.OP_SHORT_TO_REG, R8, 8'b00000011};  // 4: R8=3 (FOR MUL);
    i=i+1;cpuinst.raminst.mem[i]={cpuinst.OP_XOR, R3, R0, R1};                // 5: XOR for n!=1;
    i=i+1;cpuinst.raminst.mem[i]={cpuinst.OP_BNZ, R3, 8'b00010100};           // 6: BNZ for n!=1;
    i=i+1;cpuinst.raminst.mem[i]={cpuinst.OP_BNZ, R0, 8'b00010101};           // 7: BNZ IF n=1 (END);
    
    i=i+1;cpuinst.raminst.mem[i]={cpuinst.OP_LOAD_FROM_MEM, R0, 8'b01100100}; // 8: LOAD FROM mem[100] to R0;
    i=i+1;cpuinst.raminst.mem[i]={cpuinst.OP_AND, R4, R0, R1};                // 9: AND FOR ODD/EVEN;            
    i=i+1;cpuinst.raminst.mem[i]={cpuinst.OP_BNZ, R4, 8'b00010000};           // 10: BNZ FOR ODD/EVEN;
     
    i=i+1;cpuinst.raminst.mem[i]={cpuinst.OP_DIV, R6, R0, R7};          	     // 11: ELSE;
    i=i+1;cpuinst.raminst.mem[i]={cpuinst.OP_STORE_TO_MEM, R6, 8'b01100100};  // 12: STORE RESULT;
    i=i+1;cpuinst.raminst.mem[i]={cpuinst.OP_XOR, R5, R6, R1};                // 13: XOR FOR WHILE;            
    i=i+1;cpuinst.raminst.mem[i]={cpuinst.OP_BNZ, R5, 8'b00001000};           // 14: BNZ FOR WHILE;
    i=i+1;cpuinst.raminst.mem[i]={cpuinst.OP_BNZ, R6, 8'b00010101};           // 15: BNZ IF n=1 (END);
    
    i=i+1;cpuinst.raminst.mem[i]={cpuinst.OP_MUL, R4, R0, R8};                // 16: IF:
    i=i+1;cpuinst.raminst.mem[i]={cpuinst.OP_ADD, R6, R4, R1};                // 17: 
    i=i+1;cpuinst.raminst.mem[i]={cpuinst.OP_STORE_TO_MEM, R6, 8'b01100100};  // 18: STORE RESULT;    
    i=i+1;cpuinst.raminst.mem[i]={cpuinst.OP_XOR, R3, R6, R1};                // 19: XOR FOR WHILE;            
    i=i+1;cpuinst.raminst.mem[i]={cpuinst.OP_BNZ, R3, 8'b00001000};           // 20: BNZ FOR WHILE;
    
    
    
    
    
                                                                               //}
    
    
    file = $fopen("program.list","w");
    for(i=0;i<cpuinst.raminst.RAM_SIZE;i=i+1)
    begin
      memi=cpuinst.raminst.mem[i];
      
      $fwrite(file, "%b_%b_%b_%b\n", 
        memi[cpuinst.INSTRUCTION_SIZE-1:cpuinst.INSTRUCTION_SIZE-cpuinst.OPCODE_SIZE],
        memi[cpuinst.OPCODE_SIZE*3-1:2*cpuinst.OPCODE_SIZE],
        memi[cpuinst.OPCODE_SIZE*2-1:cpuinst.OPCODE_SIZE],
        memi[cpuinst.OPCODE_SIZE-1:0]);
    end
    $fclose(file);
end

endmodule

