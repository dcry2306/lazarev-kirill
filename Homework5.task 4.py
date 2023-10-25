def count_completed():       
        s1 = set(input().split())
        s2 = set(input().split())
        s3 = set(input().split())

        all_tasks = s1 and s2 and s3 

        if all_tasks:  
            print(*sorted(all_tasks), sep=" " ) 
        else:  
            print("Все три задачи никто не решил")  

count_completed()