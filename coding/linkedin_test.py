def repeat_optimize(word, times):
    op_str = ""
    for i in range(int(times / 2)):
        op_str = op_str + word

    return op_str + op_str


d = repeat_optimize("test-", 10)
print(d)
