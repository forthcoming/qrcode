# -*- coding: utf-8 -*-
from mylibs import data, ECC, structure, matrix, draw


def get_qrcode(words, version, level, save_place):
    # Data Coding
    version, data_codewords = data.encode(version, level, words)

    # Error Correction Coding
    ecc = ECC.encode(version, level, data_codewords)

    # Structure final bits
    final_bits = structure.structure_final_bits(version, level, data_codewords, ecc)

    # Get the QR Matrix
    qr_matrix = matrix.get_qrmatrix(version, level, final_bits)

    # Draw the picture and Save it, then return the real ver and the absolute name
    return version, draw.draw_qrcode(save_place, qr_matrix)
