module top(in1, in2, out1, out2, out3, out4, out5, out6, out7, out8, out9, out10, out11, out12, out13, out14, out15, out16, out17, out18, out19, out20, out21);
  input [5:0] in1, in2;
  output [6:0] out1;
  output out2, out3, out4, out5, out6, out7, out8, out9, out10, out11, out12, out13, out14, out15, out16, out17, out18, out19, out20, out21;
  wire [5:0] in1, in2;
  wire [6:0] out1;
  wire out2, out3, out4, out5, out6, out7, out8, out9, out10, out11, out12, out13, out14, out15, out16, out17, out18, out19, out20, out21;
  wire gte_28_22_n_0, gte_28_22_n_1, gte_28_22_n_2, gte_28_22_n_3, gte_28_22_n_4, gte_28_22_n_5, gte_28_22_n_6, gte_30_22_n_0;
  wire gte_30_22_n_1, gte_30_22_n_2, gte_30_22_n_3, gte_30_22_n_4, gte_30_22_n_5, gte_30_22_n_6, gte_32_22_n_0, gte_32_22_n_1;
  wire gte_32_22_n_2, gte_32_22_n_3, gte_32_22_n_4, gte_32_22_n_5, gte_32_22_n_6, gte_32_22_n_7, gte_32_22_n_8, gte_32_22_n_9;
  wire gte_32_22_n_10, gte_32_22_n_11, gte_32_22_n_12, gte_32_22_n_13, gte_34_23_n_0, gte_34_23_n_1, gte_34_23_n_2, gte_34_23_n_3;
  wire gte_34_23_n_4, gte_34_23_n_5, gte_34_23_n_6, gte_36_23_n_1, gte_36_23_n_2, gte_36_23_n_3, gte_36_23_n_4, gte_36_23_n_5;
  wire gte_36_23_n_6, gte_36_23_n_7, gte_36_23_n_8, gte_36_23_n_9, gte_36_23_n_10, gte_38_23_n_1, gte_38_23_n_2, gte_38_23_n_3;
  wire gte_38_23_n_4, gte_38_23_n_5, gte_40_23_n_0, gte_40_23_n_1, gte_40_23_n_2, gte_40_23_n_3, gte_40_23_n_4, gte_42_23_n_0;
  wire gte_42_23_n_1, gte_42_23_n_2, gte_42_23_n_3, gte_44_23_n_1, gte_44_23_n_2, gte_44_23_n_3, gte_44_23_n_4, gte_44_23_n_5;
  wire gte_44_23_n_6, gte_44_23_n_7, gte_44_23_n_8, gte_44_23_n_9, gte_44_23_n_10, gte_44_23_n_11, gte_44_23_n_12, lte_27_22_n_0;
  wire lte_27_22_n_1, lte_27_22_n_2, lte_27_22_n_3, lte_27_22_n_4, lte_27_22_n_5, lte_27_22_n_6, lte_27_22_n_7, lte_27_22_n_8;
  wire lte_29_22_n_1, lte_29_22_n_2, lte_29_22_n_3, lte_29_22_n_4, lte_29_22_n_5, lte_29_22_n_6, lte_29_22_n_7, lte_29_22_n_8;
  wire lte_29_22_n_9, lte_31_22_n_1, lte_31_22_n_2, lte_31_22_n_3, lte_31_22_n_4, lte_31_22_n_5, lte_31_22_n_6, lte_31_22_n_7;
  wire lte_31_22_n_8, lte_31_22_n_9, lte_31_22_n_10, lte_31_22_n_11, lte_31_22_n_12, lte_31_22_n_13, lte_31_22_n_14, lte_33_22_n_0;
  wire lte_33_22_n_1, lte_33_22_n_2, lte_33_22_n_3, lte_33_22_n_4, lte_33_22_n_5, lte_33_22_n_6, lte_33_22_n_7, lte_35_23_n_0;
  wire lte_35_23_n_1, lte_35_23_n_2, lte_35_23_n_3, lte_35_23_n_4, lte_35_23_n_5, lte_35_23_n_6, lte_35_23_n_7, lte_35_23_n_8;
  wire lte_35_23_n_9, lte_37_23_n_0, lte_37_23_n_1, lte_37_23_n_2, lte_39_23_n_0, lte_39_23_n_1, lte_39_23_n_2, lte_39_23_n_3;
  wire lte_39_23_n_4, lte_39_23_n_5, lte_41_23_n_0, lte_41_23_n_1, lte_41_23_n_2, lte_41_23_n_3, lte_41_23_n_4, lte_43_23_n_0;
  wire lte_43_23_n_1, lte_43_23_n_2, lte_43_23_n_3, lte_43_23_n_4, lte_43_23_n_5, lte_43_23_n_6, lte_43_23_n_7, lte_43_23_n_8;
  wire lte_43_23_n_9, lte_43_23_n_10, sub_25_21_n_7, sub_25_21_n_8, sub_25_21_n_9, sub_25_21_n_10, sub_25_21_n_11, sub_25_21_n_12;
  wire sub_25_21_n_13, sub_25_21_n_14, sub_25_21_n_15, sub_25_21_n_16, sub_25_21_n_17, sub_25_21_n_18, sub_25_21_n_19, sub_25_21_n_20;
  wire sub_25_21_n_21, sub_25_21_n_22, sub_25_21_n_23, sub_25_21_n_24, sub_25_21_n_25, sub_25_21_n_26, sub_25_21_n_27, sub_25_21_n_28;
  wire sub_25_21_n_29, sub_25_21_n_30, sub_25_21_n_31, sub_25_21_n_32, sub_25_21_n_33, sub_25_21_n_34, sub_25_21_n_35, sub_25_21_n_36;
  wire sub_25_21_n_37, sub_25_21_n_38, sub_25_21_n_39, sub_25_21_n_40, sub_25_21_n_41, sub_25_21_n_42, sub_25_21_n_43, sub_25_21_n_44;
  wire sub_25_21_n_45, sub_25_21_n_46, sub_25_21_n_47, sub_25_21_n_48;
  buf constbuf_n1(out21, 1'b1);
  buf constbuf_n2(out2, 1'b1);
  or gte_28_22_g82__2398(out4 ,gte_28_22_n_1 ,gte_28_22_n_6);
  or gte_28_22_g83__5107(gte_28_22_n_6 ,gte_28_22_n_3 ,gte_28_22_n_5);
  or gte_28_22_g84__6260(gte_28_22_n_5 ,out1[3] ,gte_28_22_n_4);
  and gte_28_22_g85__4319(gte_28_22_n_4 ,out1[2] ,gte_28_22_n_2);
  or gte_28_22_g86__8428(gte_28_22_n_3 ,out1[5] ,out1[4]);
  or gte_28_22_g87__5526(gte_28_22_n_2 ,out1[1] ,out1[0]);
  not gte_28_22_g88(gte_28_22_n_1 ,gte_28_22_n_0);
  buf gte_28_22_drc_bufs(gte_28_22_n_0 ,out1[6]);
  or gte_30_22_g83__6783(out6 ,gte_30_22_n_1 ,gte_30_22_n_6);
  or gte_30_22_g84__3680(gte_30_22_n_6 ,out1[5] ,gte_30_22_n_5);
  and gte_30_22_g85__1617(gte_30_22_n_5 ,out1[4] ,gte_30_22_n_4);
  or gte_30_22_g86__2802(gte_30_22_n_4 ,gte_30_22_n_3 ,gte_30_22_n_2);
  or gte_30_22_g87__1705(gte_30_22_n_3 ,out1[3] ,out1[2]);
  or gte_30_22_g88__5122(gte_30_22_n_2 ,out1[1] ,out1[0]);
  not gte_30_22_g89(gte_30_22_n_1 ,gte_30_22_n_0);
  buf gte_30_22_drc_bufs(gte_30_22_n_0 ,out1[6]);
  or gte_32_22_g78__8246(out8 ,gte_32_22_n_5 ,gte_32_22_n_13);
  or gte_32_22_g79__7098(gte_32_22_n_13 ,out1[5] ,gte_32_22_n_12);
  nor gte_32_22_g80__6131(gte_32_22_n_12 ,gte_32_22_n_9 ,gte_32_22_n_11);
  or gte_32_22_g81__1881(gte_32_22_n_11 ,gte_32_22_n_6 ,gte_32_22_n_10);
  nor gte_32_22_g82__5115(gte_32_22_n_10 ,out1[1] ,gte_32_22_n_0);
  or gte_32_22_g83__7482(gte_32_22_n_9 ,gte_32_22_n_7 ,gte_32_22_n_8);
  not gte_32_22_g84(gte_32_22_n_8 ,gte_32_22_n_1);
  not gte_32_22_g85(gte_32_22_n_7 ,gte_32_22_n_2);
  not gte_32_22_g86(gte_32_22_n_6 ,gte_32_22_n_3);
  not gte_32_22_g87(gte_32_22_n_5 ,gte_32_22_n_4);
  buf gte_32_22_drc_bufs(gte_32_22_n_4 ,out1[6]);
  buf gte_32_22_drc_bufs88(gte_32_22_n_3 ,out1[4]);
  buf gte_32_22_drc_bufs89(gte_32_22_n_2 ,out1[3]);
  buf gte_32_22_drc_bufs90(gte_32_22_n_1 ,out1[2]);
  buf gte_32_22_drc_bufs92(gte_32_22_n_0 ,out1[0]);
  or gte_34_23_g79__4733(out10 ,gte_34_23_n_1 ,gte_34_23_n_6);
  and gte_34_23_g80__6161(gte_34_23_n_6 ,out1[5] ,gte_34_23_n_5);
  or gte_34_23_g81__9315(gte_34_23_n_5 ,out1[4] ,gte_34_23_n_4);
  and gte_34_23_g82__9945(gte_34_23_n_4 ,out1[3] ,gte_34_23_n_3);
  or gte_34_23_g83__2883(gte_34_23_n_3 ,out1[0] ,gte_34_23_n_2);
  or gte_34_23_g84__2346(gte_34_23_n_2 ,out1[2] ,out1[1]);
  not gte_34_23_g85(gte_34_23_n_1 ,gte_34_23_n_0);
  buf gte_34_23_drc_bufs(gte_34_23_n_0 ,out1[6]);
  nor gte_36_23_g78__1666(gte_36_23_n_10 ,gte_36_23_n_9 ,gte_36_23_n_4);
  and gte_36_23_g79__7410(gte_36_23_n_9 ,gte_36_23_n_8 ,gte_36_23_n_7);
  or gte_36_23_g80__6417(gte_36_23_n_8 ,gte_36_23_n_5 ,gte_36_23_n_6);
  nor gte_36_23_g81__5477(gte_36_23_n_7 ,out1[5] ,gte_36_23_n_3);
  not gte_36_23_g82(gte_36_23_n_6 ,gte_36_23_n_1);
  not gte_36_23_g83(gte_36_23_n_5 ,gte_36_23_n_2);
  buf gte_36_23_drc_bufs(gte_36_23_n_4 ,out1[6]);
  buf gte_36_23_drc_bufs84(gte_36_23_n_3 ,out1[4]);
  buf gte_36_23_drc_bufs85(gte_36_23_n_2 ,out1[3]);
  buf gte_36_23_drc_bufs86(gte_36_23_n_1 ,out1[2]);
  buf gte_36_23_drc_bufs88(out12 ,gte_36_23_n_10);
  nor gte_38_23_g74__2398(gte_38_23_n_5 ,gte_38_23_n_4 ,gte_38_23_n_1);
  nor gte_38_23_g75__5107(gte_38_23_n_4 ,gte_38_23_n_2 ,gte_38_23_n_3);
  and gte_38_23_g76__6260(gte_38_23_n_3 ,out1[4] ,out1[3]);
  buf gte_38_23_drc_bufs(gte_38_23_n_2 ,out1[5]);
  buf gte_38_23_drc_bufs77(gte_38_23_n_1 ,out1[6]);
  buf gte_38_23_drc_bufs80(out14 ,gte_38_23_n_5);
  and gte_40_23_g76__4319(out16 ,out1[5] ,gte_40_23_n_4);
  nor gte_40_23_g77__8428(gte_40_23_n_4 ,gte_40_23_n_1 ,gte_40_23_n_3);
  nor gte_40_23_g78__5526(gte_40_23_n_3 ,gte_40_23_n_0 ,gte_40_23_n_2);
  or gte_40_23_g79__6783(gte_40_23_n_2 ,out1[4] ,out1[3]);
  buf gte_40_23_drc_bufs(gte_40_23_n_1 ,out1[6]);
  buf gte_40_23_drc_bufs82(gte_40_23_n_0 ,out1[2]);
  and gte_42_23_g66__3680(out18 ,out1[4] ,gte_42_23_n_3);
  nor gte_42_23_g67__1617(gte_42_23_n_3 ,gte_42_23_n_2 ,gte_42_23_n_0);
  not gte_42_23_g68(gte_42_23_n_2 ,gte_42_23_n_1);
  buf gte_42_23_drc_bufs(gte_42_23_n_1 ,out1[5]);
  buf gte_42_23_drc_bufs69(gte_42_23_n_0 ,out1[6]);
  nor gte_44_23_g70__2802(gte_44_23_n_12 ,gte_44_23_n_9 ,gte_44_23_n_11);
  or gte_44_23_g71__1705(gte_44_23_n_11 ,gte_44_23_n_7 ,gte_44_23_n_10);
  or gte_44_23_g72__5122(gte_44_23_n_10 ,gte_44_23_n_5 ,out1[6]);
  or gte_44_23_g73__8246(gte_44_23_n_9 ,gte_44_23_n_8 ,gte_44_23_n_6);
  not gte_44_23_g74(gte_44_23_n_8 ,gte_44_23_n_3);
  not gte_44_23_g75(gte_44_23_n_7 ,gte_44_23_n_1);
  not gte_44_23_g76(gte_44_23_n_6 ,gte_44_23_n_2);
  not gte_44_23_g77(gte_44_23_n_5 ,gte_44_23_n_4);
  buf gte_44_23_drc_bufs(gte_44_23_n_4 ,out1[5]);
  buf gte_44_23_drc_bufs79(gte_44_23_n_3 ,out1[4]);
  buf gte_44_23_drc_bufs80(gte_44_23_n_2 ,out1[3]);
  buf gte_44_23_drc_bufs81(gte_44_23_n_1 ,out1[2]);
  buf gte_44_23_drc_bufs82(out20 ,gte_44_23_n_12);
  and lte_27_22_g77__7098(out3 ,lte_27_22_n_5 ,lte_27_22_n_8);
  nor lte_27_22_g78__6131(lte_27_22_n_8 ,lte_27_22_n_0 ,lte_27_22_n_7);
  or lte_27_22_g79__1881(lte_27_22_n_7 ,lte_27_22_n_3 ,lte_27_22_n_6);
  and lte_27_22_g80__5115(lte_27_22_n_6 ,out1[2] ,lte_27_22_n_4);
  nor lte_27_22_g81__7482(lte_27_22_n_5 ,out1[5] ,lte_27_22_n_1);
  or lte_27_22_g82__4733(lte_27_22_n_4 ,out1[1] ,out1[0]);
  not lte_27_22_g83(lte_27_22_n_3 ,lte_27_22_n_2);
  buf lte_27_22_drc_bufs(lte_27_22_n_2 ,out1[6]);
  buf lte_27_22_drc_bufs84(lte_27_22_n_1 ,out1[4]);
  buf lte_27_22_drc_bufs85(lte_27_22_n_0 ,out1[3]);
  nor lte_29_22_g78__6161(lte_29_22_n_9 ,lte_29_22_n_8 ,lte_29_22_n_2);
  or lte_29_22_g79__9315(lte_29_22_n_8 ,lte_29_22_n_3 ,lte_29_22_n_7);
  and lte_29_22_g80__9945(lte_29_22_n_7 ,out1[4] ,lte_29_22_n_6);
  or lte_29_22_g81__2883(lte_29_22_n_6 ,lte_29_22_n_5 ,lte_29_22_n_4);
  or lte_29_22_g82__2346(lte_29_22_n_5 ,out1[3] ,out1[2]);
  or lte_29_22_g83__1666(lte_29_22_n_4 ,out1[1] ,out1[0]);
  not lte_29_22_g84(lte_29_22_n_3 ,lte_29_22_n_1);
  buf lte_29_22_drc_bufs(lte_29_22_n_2 ,out1[5]);
  buf lte_29_22_drc_bufs85(lte_29_22_n_1 ,out1[6]);
  buf lte_29_22_drc_bufs91(out5 ,lte_29_22_n_9);
  nor lte_31_22_g83__7410(lte_31_22_n_14 ,lte_31_22_n_13 ,lte_31_22_n_5);
  or lte_31_22_g84__6417(lte_31_22_n_13 ,lte_31_22_n_7 ,lte_31_22_n_12);
  and lte_31_22_g85__5477(lte_31_22_n_12 ,out1[4] ,lte_31_22_n_11);
  nor lte_31_22_g86__2398(lte_31_22_n_11 ,lte_31_22_n_10 ,lte_31_22_n_9);
  or lte_31_22_g87__5107(lte_31_22_n_10 ,lte_31_22_n_8 ,lte_31_22_n_6);
  nor lte_31_22_g88__6260(lte_31_22_n_9 ,out1[1] ,lte_31_22_n_1);
  not lte_31_22_g89(lte_31_22_n_8 ,lte_31_22_n_3);
  not lte_31_22_g90(lte_31_22_n_7 ,lte_31_22_n_4);
  not lte_31_22_g91(lte_31_22_n_6 ,lte_31_22_n_2);
  buf lte_31_22_drc_bufs(lte_31_22_n_5 ,out1[5]);
  buf lte_31_22_drc_bufs92(lte_31_22_n_4 ,out1[6]);
  buf lte_31_22_drc_bufs94(lte_31_22_n_3 ,out1[3]);
  buf lte_31_22_drc_bufs95(lte_31_22_n_2 ,out1[2]);
  buf lte_31_22_drc_bufs97(lte_31_22_n_1 ,out1[0]);
  buf lte_31_22_drc_bufs98(out7 ,lte_31_22_n_14);
  and lte_33_22_g81__4319(out9 ,out1[6] ,lte_33_22_n_7);
  or lte_33_22_g82__8428(lte_33_22_n_7 ,lte_33_22_n_2 ,lte_33_22_n_6);
  nor lte_33_22_g83__5526(lte_33_22_n_6 ,lte_33_22_n_0 ,lte_33_22_n_5);
  and lte_33_22_g84__6783(lte_33_22_n_5 ,out1[3] ,lte_33_22_n_4);
  or lte_33_22_g85__3680(lte_33_22_n_4 ,out1[0] ,lte_33_22_n_3);
  or lte_33_22_g86__1617(lte_33_22_n_3 ,out1[2] ,out1[1]);
  not lte_33_22_g87(lte_33_22_n_2 ,lte_33_22_n_1);
  buf lte_33_22_drc_bufs(lte_33_22_n_1 ,out1[5]);
  buf lte_33_22_drc_bufs89(lte_33_22_n_0 ,out1[4]);
  and lte_35_23_g84__2802(out11 ,out1[6] ,lte_35_23_n_9);
  or lte_35_23_g85__1705(lte_35_23_n_9 ,lte_35_23_n_4 ,lte_35_23_n_8);
  or lte_35_23_g86__5122(lte_35_23_n_8 ,lte_35_23_n_3 ,lte_35_23_n_7);
  nor lte_35_23_g87__8246(lte_35_23_n_7 ,lte_35_23_n_0 ,lte_35_23_n_6);
  and lte_35_23_g88__7098(lte_35_23_n_6 ,out1[2] ,lte_35_23_n_5);
  or lte_35_23_g89__6131(lte_35_23_n_5 ,out1[1] ,out1[0]);
  not lte_35_23_g90(lte_35_23_n_4 ,lte_35_23_n_2);
  not lte_35_23_g91(lte_35_23_n_3 ,lte_35_23_n_1);
  buf lte_35_23_drc_bufs(lte_35_23_n_2 ,out1[5]);
  buf lte_35_23_drc_bufs93(lte_35_23_n_1 ,out1[4]);
  buf lte_35_23_drc_bufs94(lte_35_23_n_0 ,out1[3]);
  or lte_37_23_g71__1881(out13 ,out1[6] ,lte_37_23_n_2);
  nor lte_37_23_g72__5115(lte_37_23_n_2 ,lte_37_23_n_0 ,lte_37_23_n_1);
  and lte_37_23_g73__7482(lte_37_23_n_1 ,out1[4] ,out1[3]);
  buf lte_37_23_drc_bufs(lte_37_23_n_0 ,out1[5]);
  or lte_39_23_g71__4733(out15 ,lte_39_23_n_4 ,lte_39_23_n_5);
  nor lte_39_23_g72__6161(lte_39_23_n_5 ,lte_39_23_n_0 ,lte_39_23_n_3);
  or lte_39_23_g73__9315(lte_39_23_n_4 ,lte_39_23_n_2 ,out1[6]);
  or lte_39_23_g74__9945(lte_39_23_n_3 ,out1[4] ,out1[3]);
  not lte_39_23_g75(lte_39_23_n_2 ,lte_39_23_n_1);
  buf lte_39_23_drc_bufs(lte_39_23_n_1 ,out1[5]);
  buf lte_39_23_drc_bufs79(lte_39_23_n_0 ,out1[2]);
  or lte_41_23_g66__2883(out17 ,lte_41_23_n_2 ,lte_41_23_n_4);
  or lte_41_23_g67__2346(lte_41_23_n_4 ,lte_41_23_n_3 ,out1[6]);
  not lte_41_23_g68(lte_41_23_n_3 ,lte_41_23_n_1);
  not lte_41_23_g69(lte_41_23_n_2 ,lte_41_23_n_0);
  buf lte_41_23_drc_bufs(lte_41_23_n_1 ,out1[5]);
  buf lte_41_23_drc_bufs71(lte_41_23_n_0 ,out1[4]);
  or lte_43_23_g74__1666(out19 ,lte_43_23_n_8 ,lte_43_23_n_10);
  or lte_43_23_g75__7410(lte_43_23_n_10 ,lte_43_23_n_6 ,lte_43_23_n_9);
  or lte_43_23_g76__6417(lte_43_23_n_9 ,lte_43_23_n_4 ,out1[6]);
  or lte_43_23_g77__5477(lte_43_23_n_8 ,lte_43_23_n_7 ,lte_43_23_n_5);
  not lte_43_23_g78(lte_43_23_n_7 ,lte_43_23_n_2);
  not lte_43_23_g79(lte_43_23_n_6 ,lte_43_23_n_0);
  not lte_43_23_g80(lte_43_23_n_5 ,lte_43_23_n_1);
  not lte_43_23_g81(lte_43_23_n_4 ,lte_43_23_n_3);
  buf lte_43_23_drc_bufs(lte_43_23_n_3 ,out1[5]);
  buf lte_43_23_drc_bufs83(lte_43_23_n_2 ,out1[4]);
  buf lte_43_23_drc_bufs84(lte_43_23_n_1 ,out1[3]);
  buf lte_43_23_drc_bufs85(lte_43_23_n_0 ,out1[2]);
  or sub_25_21_g147__2398(sub_25_21_n_48 ,sub_25_21_n_21 ,sub_25_21_n_46);
  xnor sub_25_21_g148__5107(sub_25_21_n_47 ,sub_25_21_n_45 ,sub_25_21_n_32);
  and sub_25_21_g149__6260(sub_25_21_n_46 ,sub_25_21_n_18 ,sub_25_21_n_45);
  and sub_25_21_g150__4319(sub_25_21_n_45 ,sub_25_21_n_25 ,sub_25_21_n_43);
  xnor sub_25_21_g151__8428(sub_25_21_n_44 ,sub_25_21_n_42 ,sub_25_21_n_31);
  or sub_25_21_g152__5526(sub_25_21_n_43 ,sub_25_21_n_24 ,sub_25_21_n_42);
  and sub_25_21_g153__6783(sub_25_21_n_42 ,sub_25_21_n_22 ,sub_25_21_n_40);
  xnor sub_25_21_g154__3680(sub_25_21_n_41 ,sub_25_21_n_39 ,sub_25_21_n_30);
  or sub_25_21_g155__1617(sub_25_21_n_40 ,sub_25_21_n_26 ,sub_25_21_n_39);
  and sub_25_21_g156__2802(sub_25_21_n_39 ,sub_25_21_n_23 ,sub_25_21_n_37);
  xnor sub_25_21_g157__1705(sub_25_21_n_38 ,sub_25_21_n_35 ,sub_25_21_n_29);
  or sub_25_21_g158__5122(sub_25_21_n_37 ,sub_25_21_n_20 ,sub_25_21_n_35);
  xnor sub_25_21_g159__8246(sub_25_21_n_36 ,sub_25_21_n_27 ,sub_25_21_n_28);
  and sub_25_21_g160__7098(sub_25_21_n_35 ,sub_25_21_n_19 ,sub_25_21_n_34);
  or sub_25_21_g161__6131(sub_25_21_n_34 ,sub_25_21_n_17 ,sub_25_21_n_27);
  xor sub_25_21_g162__1881(sub_25_21_n_33 ,in1[0] ,in2[0]);
  xnor sub_25_21_g163__5115(sub_25_21_n_32 ,in1[5] ,in2[5]);
  xnor sub_25_21_g164__7482(sub_25_21_n_31 ,in1[4] ,in2[4]);
  xnor sub_25_21_g165__4733(sub_25_21_n_30 ,in1[3] ,in2[3]);
  xnor sub_25_21_g166__6161(sub_25_21_n_29 ,in1[2] ,in2[2]);
  xnor sub_25_21_g167__9315(sub_25_21_n_28 ,in1[1] ,in2[1]);
  nor sub_25_21_g168__9945(sub_25_21_n_26 ,sub_25_21_n_15 ,in1[3]);
  or sub_25_21_g169__2883(sub_25_21_n_25 ,sub_25_21_n_12 ,in2[4]);
  nor sub_25_21_g170__2346(sub_25_21_n_24 ,sub_25_21_n_11 ,in1[4]);
  or sub_25_21_g171__1666(sub_25_21_n_23 ,sub_25_21_n_9 ,in2[2]);
  and sub_25_21_g172__7410(sub_25_21_n_27 ,in2[0] ,sub_25_21_n_16);
  or sub_25_21_g173__6417(sub_25_21_n_22 ,sub_25_21_n_14 ,in2[3]);
  nor sub_25_21_g174__5477(sub_25_21_n_21 ,sub_25_21_n_10 ,in1[5]);
  and sub_25_21_g175__2398(sub_25_21_n_20 ,in2[2] ,sub_25_21_n_9);
  or sub_25_21_g176__5107(sub_25_21_n_19 ,sub_25_21_n_8 ,in2[1]);
  or sub_25_21_g177__6260(sub_25_21_n_18 ,sub_25_21_n_7 ,in2[5]);
  nor sub_25_21_g178__4319(sub_25_21_n_17 ,sub_25_21_n_13 ,in1[1]);
  not sub_25_21_g179(sub_25_21_n_16 ,in1[0]);
  not sub_25_21_g180(sub_25_21_n_15 ,in2[3]);
  not sub_25_21_g181(sub_25_21_n_14 ,in1[3]);
  not sub_25_21_g182(sub_25_21_n_13 ,in2[1]);
  not sub_25_21_g183(sub_25_21_n_12 ,in1[4]);
  not sub_25_21_g184(sub_25_21_n_11 ,in2[4]);
  not sub_25_21_g185(sub_25_21_n_10 ,in2[5]);
  not sub_25_21_g186(sub_25_21_n_9 ,in1[2]);
  not sub_25_21_g187(sub_25_21_n_8 ,in1[1]);
  not sub_25_21_g188(sub_25_21_n_7 ,in1[5]);
  buf sub_25_21_drc_bufs(out1[6] ,sub_25_21_n_48);
  buf sub_25_21_drc_bufs189(out1[5] ,sub_25_21_n_47);
  buf sub_25_21_drc_bufs190(out1[4] ,sub_25_21_n_44);
  buf sub_25_21_drc_bufs191(out1[3] ,sub_25_21_n_41);
  buf sub_25_21_drc_bufs192(out1[2] ,sub_25_21_n_38);
  buf sub_25_21_drc_bufs193(out1[0] ,sub_25_21_n_33);
  buf sub_25_21_drc_bufs194(out1[1] ,sub_25_21_n_36);
endmodule