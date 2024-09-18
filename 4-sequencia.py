def completar_sequencia():

    seq_a = [1, 3, 5, 7]
    proximo_a = seq_a[-1] + 2
    print(f"a) Próximo número: {proximo_a}")
    
    seq_b = [2, 4, 8, 16, 32, 64]
    proximo_b = seq_b[-1] * 2
    print(f"b) Próximo número: {proximo_b}")
    
    seq_c = [0, 1, 4, 9, 16, 25, 36]
    proximo_c = (len(seq_c))**2
    print(f"c) Próximo número: {proximo_c}")

    seq_d = [4, 16, 36, 64]
    proximo_d = (len(seq_d) + 2)**2
    print(f"d) Próximo número: {proximo_d}")
    
    seq_e = [1, 1, 2, 3, 5, 8]
    proximo_e = seq_e[-1] + seq_e[-2]
    print(f"e) Próximo número: {proximo_e}")
    
    seq_f = [2, 10, 12, 16, 17, 18, 19]
    proximo_f = seq_f[-1] + 1
    print(f"f) Próximo número: {proximo_f}")

completar_sequencia()