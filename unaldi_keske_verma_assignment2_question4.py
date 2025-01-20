# Assignment 2 - Umutcan Ünaldı (7025677), Shruti Verma (7022659), Nazlıgül Keske (7025902)
from csv import writer
# Bio and Bio.Align is specifically used for consensus calculations
from Bio import AlignIO as al
from Bio.Align import AlignInfo as alI


# Alignment is called with the format "clustal"
alignment = al.read("clustalo-E20211130-094437-0140-87358764-p2m.clustal_num", "clustal")
# Summary info is assigned
align = alI.SummaryInfo(alignment)


# Question 4
a_counter, r_counter, n_counter,d_counter, c_counter, e_counter, q_counter, g_counter = 0,0,0,0,0,0,0,0
h_counter, i_counter, l_counter, k_counter, m_counter,f_counter, p_counter, t_counter = 0,0,0,0,0,0,0,0
s_counter, w_counter, y_counter, v_counter, x_counter = 0,0,0,0,0

prob_a, prob_r, prob_n, prob_d, prob_c, prob_e, prob_q, prob_g, prob_h, prob_i, prob_l = 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
prob_k, prob_m, prob_f, prob_p, prob_t, prob_s, prob_w, prob_y, prob_v, prob_x = 1, 1, 1, 1, 1, 1, 1, 1, 1, 1



for i in range(0, 386):
    for j in range (0, 10):
        if alignment[j][i] == "A":
            a_counter += 1
            print(a_counter)
            prob_a = prob_a * (a_counter/11)

        if alignment[j][i] == "R":
            r_counter += 1
            print(r_counter)
            prob_r = prob_r * (r_counter / 11)

        if alignment[j][i] == "N":
            n_counter += 1
            prob_n = prob_n * (n_counter / 11)
        if alignment[j][i] == "D":
            d_counter += 1
            prob_d = prob_d * (d_counter / 11)
        if alignment[j][i] == "C":
            c_counter += 1
            prob_c = prob_c * (c_counter / 11)
        if alignment[j][i] == "E":
            e_counter += 1
            prob_e = prob_e * (e_counter / 11)
        if alignment[j][i] == "Q":
            q_counter += 1
            prob_q = prob_q * (q_counter / 11)
        if alignment[j][i] == "G":
            g_counter += 1
            prob_g = prob_g * (g_counter / 11)
        if alignment[j][i] == "H":
            h_counter += 1
            prob_h = prob_h * (h_counter / 11)
        if alignment[j][i] == "I":
            i_counter += 1
            prob_i = prob_i * (i_counter / 11)
        if alignment[j][i] == "L":
            l_counter += 1
            prob_l = prob_l * (l_counter / 11)
        if alignment[j][i] == "K":
            k_counter += 1
            prob_k = prob_k * (k_counter / 11)
        if alignment[j][i] == "M":
            m_counter += 1
            prob_m = prob_m * (m_counter / 11)
        if alignment[j][i] == "F":
            f_counter += 1
            prob_f = prob_f * (f_counter / 11)
        if alignment[j][i] == "P":
            p_counter += 1
            prob_p = prob_p * (p_counter / 11)
        if alignment[j][i] == "T":
            t_counter += 1
            prob_t = prob_t * (t_counter / 11)
        if alignment[j][i] == "S":
            s_counter += 1
            prob_s = prob_s * (s_counter / 11)
        if alignment[j][i] == "W":
            w_counter += 1
            prob_w = prob_w * (w_counter / 11)
        if alignment[j][i] == "Y":
            y_counter += 1
            prob_y = prob_y * (y_counter / 11)
        if alignment[j][i] == "V":
            v_counter += 1
            prob_v = prob_v * (v_counter / 11)
        if alignment[j][i] == "X":
            x_counter += 1
            prob_x = prob_x * (x_counter / 11)

prob_list= (prob_a, prob_r, prob_n, prob_d, prob_c, prob_e, prob_q, prob_g, prob_h, prob_i, prob_l,
            prob_k, prob_m, prob_f, prob_p, prob_t, prob_s, prob_w, prob_y, prob_v, prob_x)


# Written to csv
with open('sequencep.csv', 'a', newline='') as profile:
    writer_object = writer(profile)
    writer_object.writerow(prob_list)