module alu_tb;

    reg [31:0] a, b;
    reg [3:0] opcode;
    wire [31:0] result;
    wire zero;

    // Instantiate DUT
    alu uut (
        .a(a),
        .b(b),
        .opcode(opcode),
        .result(result),
        .zero(zero)
    );

    initial begin
        $display("Starting ALU test...");

        // ADD
        a = 10; b = 5; opcode = 4'b0000;
        #10;
        $display("ADD result = %d", result);

        // SUB
        opcode = 4'b0001;
        #10;
        $display("SUB result = %d", result);

        // AND
        opcode = 4'b0010;
        #10;
        $display("AND result = %d", result);

        // OR
        opcode = 4'b0011;
        #10;
        $display("OR result = %d", result);

        // XOR
        opcode = 4'b0100;
        #10;
        $display("XOR result = %d", result);

        // SHIFT LEFT
        b = 2;
        opcode = 4'b0101;
        #10;
        $display("SLL result = %d", result);

        // SHIFT RIGHT
        b = 2;
        opcode = 4'b0110;
        #10;
        $display("SRL result = %d", result);

        // SLT TEST
        a = 5; b = 10;
        opcode = 4'b0111;
        #10;
        $display("SLT (5 < 10) result = %d", result);

        a = 20; b = 10;
        #10;
        $display("SLT (20 < 10) result = %d", result);

        $finish;
    end

endmodule
