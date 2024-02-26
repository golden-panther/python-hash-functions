def fnv1a64(input_str):
    FNV_prime = 1099511628211 	
    FNV_offset_basis = 14695981039346656037 
    hash = FNV_offset_basis
    for byte_of_data in input_str:
        hash = hash ^ byte_of_data
        hash = hash * FNV_prime
    return hex(hash)[-16:]


print(fnv1a64(b'hello'))