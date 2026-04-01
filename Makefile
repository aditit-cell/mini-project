SIM             = icarus
TOPLEVEL_LANG   = verilog
VERILOG_SOURCES = $(PWD)/rtl/alu.sv
TOPLEVEL        = alu
MODULE          = tb.tests.alu_test

export COCOTB_LOG_LEVEL = WARNING
export COCOTB_RESULTS_FILE = logs/results.xml

include $(shell cocotb-config --makefiles)/Makefile.sim
