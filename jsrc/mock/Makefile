run:
	yosys -p 'read_verilog carry_lookahead.v ;  aigmap; write_aiger c.aig;'
	yosys -p 'read_verilog ripple_adder.v full_adder.v ; flatten; synth -top ripple_adder; aigmap; write_aiger b.aig;'
	yosys -p 'read_verilog cla_adder.v cla_block.v ; flatten; synth -top cla_adder; aigmap; write_aiger d.aig;'
	abc -c 'read c.aig; write c.aig'
	abc -c 'read b.aig; write b.aig'
	abc -c 'read d.aig; write d.aig'
	~/uu/aiger/aigtodot c.aig c.dot
	~/uu/aiger/aigtodot b.aig b.dot
	~/uu/aiger/aigtodot d.aig d.dot
