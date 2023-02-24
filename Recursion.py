# Function that takes two arguments (start, end) and outputs a count
# starting from start til end but excluding end.
def count_up(start, end):
    # Base case: If start equals the end value do nothing and end recursion.
    if start == end:
        return
    else:
        # Print start and do a recursive call and add 1 to (start)
        # if start is still less then end
        print(start)
        count_up(start+1, end)



# Function that outputs a count starting from start, increases or decreases as
# appropriate by 1 at each recursive step, and stops before end.
def count(start, end):
    # Base case: If start equals the end value do nothing and end recursion.
    if start == end:
        return
    else:
        if start > end:
            # Print start and do a recursive call and subtract 1 from (start)
            # if start is still greater than end
            print(start)
            count(start-1, end)

        else:
            # Print start and do a recursive call and add 1 to (start)
            # if start is still less than end
            print(start)
            count(start+1, end)


# Function that outputs a count starting from start, increases or decreases
# as appropriate by inc at each recursive step, and stops when the count reaches or exceeds end.
def count_inc(start, end, inc):
    # Base case: If start equals the end value do nothing and end recursion.
    if start == end:
        return
    else:
        if start > end:
            # Print start and do a recursive call and subtract inc from (start)
            # if start is still greater than end
            print(start)
            new_start = start-inc
            if(new_start < end):
                count_inc(end, end, inc)
            else:
                count_inc(new_start, end, inc)
        else:
            # Print start and do a recursive call and add inc to (start)
            # if start is still less than end
            print(start)
            new_start = start+inc
            if(new_start > end):
                count_inc(end, end, inc)
            else:
                count_inc(new_start, end, inc)


# Function that behaves exactly like count_inc(), but with one modification:
# a Boolean value for is_exclusive determines whether the function is exclusive (True) or inclusive (False).
def count_inc_end(start, end, inc, is_exclusive):
    # Base case: if start equals the end value, handle inclusiveness of end and end recursion.
    if start == end:
        if is_exclusive:
            return
        else:
            print(end)
    else:
        # Recursive case: handle counting up or down based on start and end values.
        if start > end:
            print(start)
            new_start = start - inc
            # If the new start value is less than the end value, handle inclusiveness of end and end recursion.
            if new_start < end:
                if is_exclusive:
                    return
                else:
                    print(end)
            else:
                count_inc_end(new_start, end, inc, is_exclusive)
        else:
            print(start)
            new_start = start + inc
            # If the new start value is greater than the end value, handle inclusiveness of end and end recursion.
            if new_start > end:
                if is_exclusive:
                    return
                else:
                    print(end)
            else:
                count_inc_end(new_start, end, inc, is_exclusive)

print("Testing count_up(start, end):")
print("count_up(3, 8):")
count_up(3, 8)

print("count_up(-2, 4):")
count_up(-2, 4)

print("count_up(5, 5):")
count_up(5, 5)
print()


print("Testing count(start, end):")
print("count(4, 5):")
count(4, 5)

print("count(7, 2):")
count(7, 2)

print("count(5, 5):")
count(5, 5)
print()


print("Testing count_inc(start, end, inc):")
print("count_inc(13, 3, 2):")
count_inc(13, 3, 2)

print("count_inc(7, 18, 4):")
count_inc(7, 18, 4)

print("count_inc(-5, 2, 3):")
count_inc(-5, 2, 3)
print()


print("Testing count_inc_end(start, end, inc, is_exclusive)")
print("count_inc_end(5, 2, 2, True):")
count_inc_end(5, 2, 2, True)

print("count_inc_end(2, 5, 2, False):")
count_inc_end(2, 5, 2, False)

print("count_inc_end(-3, -7, 1, True):")
count_inc_end(-3, -7, 1, True)
