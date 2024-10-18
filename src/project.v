/*
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_htfab_latch_test (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // always 1 when the design is powered, so you can ignore it
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);

// positive latch

wire p_e = ui_in[0];
wire p_d = ui_in[1];
reg p_q;

always_latch begin
    if (p_e) p_q = p_d;
end

// negative latch

wire n_e = ui_in[2];
wire n_d = ui_in[3];
reg n_q;

always_latch begin
    if (~n_e) n_q = n_d;
end

// assign outputs

assign uo_out[0] = p_q;
assign uo_out[1] = n_q;
assign uo_out[7:2] = 0;
assign uio_out = 0;
assign uio_oe = 0;

// ignore unused inputs

wire _unused = &{ena, clk, rst_n, ui_in[7:4], uio_in, 1'b0};

endmodule
