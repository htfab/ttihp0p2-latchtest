# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Test project behavior")

    dut.uio_in.value = 0

    dut.ui_in.value = 0b00000011
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0b00000001

    dut.ui_in.value = 0b00000110
    await ClockCycles(dut.clk, 1)
    dut.ui_in.value = 0b00001100
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0b00000001

    dut.ui_in.value = 0b00001001
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0b00000010

    dut.ui_in.value = 0b00001100
    await ClockCycles(dut.clk, 1)
    dut.ui_in.value = 0b00000110
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0b00000010

