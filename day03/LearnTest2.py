"""
需求：
   *
  ***
 *****
*******
"""


def draw_starts(lines):
    for i in range(1, lines):
        print(' ' * (lines - i), ' ' * (lines - i), sep='*' * ((2 * i) - 1))


draw_starts(6)


