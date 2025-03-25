for i in range(0, 11):
    i_decimal = i / 5
    for j in range(1, 4):
        j_decimal = j + i_decimal
        if i_decimal == int(i_decimal):
            print(f"I={int(i_decimal)} J={int(j_decimal)}")
        else:
            print(f"I={i_decimal:.1f} J={j_decimal:.1f}")