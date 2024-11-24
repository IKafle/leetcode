

def how_sum(target_sum, arr, path, container):
    
    if (target_sum == 0): return []
    if (target_sum <= 0): return None
    
    for num in arr:
        
        sum  = target_sum - num
        remainder = how_sum(sum, arr, path, container) # returned value from base case/child nodes/ leaf node.
        
        if (remainder  != None):
            path = remainder + [num]
            return path
            
    container.append(path)
    return container




if __name__ == "__main__":
    print("hello world")
    can_sum : list[int] = how_sum(8, [7,3,5], [], [])
    print(f"Final output : {can_sum}")