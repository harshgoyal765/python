def fibonacci_pattern(n):
    # Generate fibonacci series
    fib = [1, 1]
    sum2=[1,1]
   
    for i in range(2, n):
        sum1=sum(fib)
        sum2.append(sum1)
        #print(sum2)
        fib.append(fib[-1] + fib[-2])
    total_sum=sum(fib)+1

   
    # Print pattern
    for i in range(n):
        #print("here is sum2",sum2,(total_sum-sum2[i]-i))
        #print(total_sum)
        # Left spacing
        print(" " * (total_sum-sum2[i]-i), end="")

        # Left stars
        print("*" * fib[i], end="")

        # Middle spacing
        print(" " * (2 * sum2[i]), end="")

        # Right stars (skip for topmost as it's common)
        if i != 0:
            print("*" * fib[i])
        else:
            print("")


# Example run
fibonacci_pattern(4)
