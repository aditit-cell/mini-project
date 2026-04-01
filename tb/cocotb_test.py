import cocotb
from cocotb.triggers import Timer
import random, sys

sys.stdout.reconfigure(line_buffering=True)

OPCODE_NAMES = {
    0: "ADD", 1: "SUB", 2: "AND", 3: "OR",
    4: "XOR", 5: "SLL", 6: "SRL", 7: "SLT"
}

def alu_model(a, b, opcode):
    shamt = b & 0x1F

    if opcode == 0:
        return (a + b) & 0xFFFFFFFF
    elif opcode == 1:
        return (a - b) & 0xFFFFFFFF
    elif opcode == 2:
        return a & b
    elif opcode == 3:
        return a | b
    elif opcode == 4:
        return a ^ b
    elif opcode == 5:
        return (a << shamt) & 0xFFFFFFFF
    elif opcode == 6:
        return (a >> shamt) & 0xFFFFFFFF
    elif opcode == 7:
        a_signed = a if a < (1 << 31) else a - (1 << 32)
        b_signed = b if b < (1 << 31) else b - (1 << 32)
        return 1 if (a_signed < b_signed) else 0
    else:
        return 0

@cocotb.test()
async def test_alu_random(dut):

    for i in range(50):
        opcode = random.randint(0, 7)
        a      = random.randint(0, 0xFFFFFFFF)
        b      = random.randint(0, 0xFFFFFFFF)

        dut.opcode.value = opcode
        dut.a.value      = a
        dut.b.value      = b

        await Timer(1, unit="ns")

        result = int(dut.result.value)
        expected = alu_model(a, b, opcode)

        print(f"[{i+1:02d}] {OPCODE_NAMES[opcode]} | "
              f"A={a:#010x}, B={b:#010x} → "
              f"result={result:#010x}, expected={expected:#010x}")

        assert result == expected, f"Mismatch at test {i+1}"
        assert (result == 0) == (int(dut.zero.value) == 1)

    await Timer(1, unit="ns")