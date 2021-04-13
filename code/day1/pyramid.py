"""
Fun script to generate the following pattern

                                    1
                                  1   2
                                1   2   3
                              1   2   3   4
                            1   2   3   4   5
                          1   2   3   4   5   6
                        1   2   3   4   5   6   7
                      1   2   3   4   5   6   7   8
                    1   2   3   4   5   6   7   8   9
                  1   2   3   4   5   6   7   8   9   10
                1   2   3   4   5   6   7   8   9   10  11
              1   2   3   4   5   6   7   8   9   10  11  12
            1   2   3   4   5   6   7   8   9   10  11  12  13
          1   2   3   4   5   6   7   8   9   10  11  12  13  14
        1   2   3   4   5   6   7   8   9   10  11  12  13  14  15
      1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16
    1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17
  1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18
1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19
"""
num_rows = 20
rows = (list(range(1, row_end)) for row_end in range(1, num_rows + 2))

spacer = 4
FMT = num_rows * spacer

# loop through non-empty rows
for row in iter(rows):
    line = "".join(str(item).ljust(spacer, ' ') for item in row)
    print(f"{line: ^{FMT}}")
