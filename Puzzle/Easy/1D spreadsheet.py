n = int(input())
results_list = [None for _ in range(n)]
liste_op = []

for i in range(n):
    operation, arg_1, arg_2 = input().split()
    liste_op.append((operation, arg_1, arg_2))


def ope(type_op, arg1, arg2):
    if type_op == "ADD":
        return arg1 + arg2
    elif type_op == "SUB":
        return arg1 - arg2
    else:
        return arg1 * arg2


while None in results_list:
    for i in range(n):
        if results_list[i] is None:
            operation, arg_1, arg_2 = liste_op[i]
            if operation == "VALUE":
                if arg_1 != "_":
                    if arg_1[0] == "$":
                        case = int(arg_1[1:])
                        arg_1 = results_list[case]
                        if arg_1 is not None:
                            results_list[i] = int(arg_1)
                    else:
                        results_list[i] = int(arg_1)
                else:
                    if arg_2[0] == "$":
                        case = int(arg_2[1:])
                        arg_2 = results_list[case]
                        if arg_2 is not None:
                            results_list[i] = int(arg_2)
                    else:
                        results_list[i] = int(arg_2)
            else:
                if arg_1[0] == "$":
                    case = int(arg_1[1:])
                    arg_1 = results_list[case]
                else:
                    arg_1 = int(arg_1)

                if arg_2[0] == "$":
                    case = int(arg_2[1:])
                    arg_2 = results_list[case]
                else:
                    arg_2 = int(arg_2)

                if arg_1 is not None and arg_2 is not None:
                    results_list[i] = ope(operation, int(arg_1), int(arg_2))

for val in results_list:
    print(val)
