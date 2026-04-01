from pyuvm import uvm_sequence
from tb.sequences.sequence_item import ALUSeqItem

class ALUSequence(uvm_sequence):
    def __init__(self, name="ALUSequence", num_tests=300):
        super().__init__(name)
        self.num_tests = num_tests

    async def body(self):
        for _ in range(self.num_tests):
            item = ALUSeqItem("item")
            item.randomize()
            await self.start_item(item)
            await self.finish_item(item)