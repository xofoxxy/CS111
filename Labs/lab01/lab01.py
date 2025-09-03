
def get_inputs():
    """
    Enter an integer divisible by 20 => 100
    Enter a floating point number => 3.1
    Enter a family relationship (mother, grandfather, cousin, etc.) => aunt
    Enter a noun => tricycle
    Enter an adjective => glowing
    """
    integer = int(input())
    if integer % 20 != 0:
        print(f"{integer} is not divisible by 20!")
        return False
    float_num = float(input())
    family_relation = input()
    noun = input()
    adjective = input()

    inputs = [integer, float_num, family_relation, noun, adjective]
    return inputs

def mad_lib(inputs):
    integer, float_num, family_relation, noun, adjective = inputs
    print(f"{int(integer/20)} score and {float_num:.3f} years ago, our fore{family_relation}s brought forth upon this {noun} a {adjective} nation.")

if __name__ == "__main__":
    inputs = get_inputs()
    if inputs:
        mad_lib(inputs)

