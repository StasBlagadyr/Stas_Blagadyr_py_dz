
def get_even_rand(max_value):
      n = 1
      while n <= max_value:
            yield n
            n += 2
to_15 = get_even_rand(15)
print(get_even_rand(1))


