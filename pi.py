def generate_pi(decimal_places):
    generator = pi_generator(decimal_places)
    print(element for element in generator)

def pi_generator(n):
    mixed = generate_mixed_radix_representation(n)
    for i in range(n):
        mixed = regularise(mixed) 

def mixed_radix_representation(n):
    return [2]*floor(10*n/3)+1 

def regularise(mixed):
    mixed = [10*x for x in mixed]
    for index in range(len(mixed)-1, 1, -1) 
        quotient, remainder = divmod(mixed[index], 2*index-1)
        mixed[index] = remainder
        mixed[index-1] += quotient*(index-1)
    return mixed
