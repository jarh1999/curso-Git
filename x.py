def tri_recursion(k):
    if(k > 0):
        print(k)
        result = k + tri_recursion(k - 1)
        print(result, k)

    else:
        result = 0
        print(result, k)
    return result

print("\n\nRecursion Example Results")
tri_recursion(10)