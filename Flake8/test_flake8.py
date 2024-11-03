# WUILLERMIN Mainell - Python 3.2 - Functions Helping statisticians Part 1

# Mission 1


def hello_python():
    return "Hello Python de la Fournaise"


hello_python()

# Mission 2


def equal(nb1, bn2):
    if nb1 == bn2:
        return True
    else:
        return False


equal(7, 7)

# Mission 3


def mule_tiples(number):
    my_list = []
    for i in range(1, 11):
        my_list.append(number*i)
    return my_list


mule_tiples(2)

# Mission 4


def keep_vowels(input_string):
    output_string = str()
    vowels = "aeiouyAEIOUY"
    for i in range(len(input_string)):
        if input_string[i] in vowels:
            output_string += input_string[i]
    return output_string


keep_vowels("ABRACADABRA")

# Mission 5


def division_operation(num1, num2):
    if (num2 == 0):
        print("Tu viens de faire quelque chose d'interdit!")
        return
    return num1/num2


division_operation(10, 0)


# Mission 6


def arithm(num1, num2, num3):
    if (num2 == 0):
        print("Divide-by-zero error")
        return
    result = (num1/num2)-num3
    if (result > 0):
        print("Positive result")
    return result


arithm(10, 2, 3)


# Mission 7


def net_salary(gross_salary):
    return gross_salary - gross_salary*21/100


net_salary(1000)


# Mission 8


def swap(A, B):
    C = A
    A = B
    B = C
    print("A="+str(A))
    print("B="+str(B))


swap(2, 4)
