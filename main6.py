#сортировка слияния 
def merge_sort(nums):#создадим функцию сортировки
    if len(nums) > 1:
        mid = len(nums) // 2 #создадим переменную для половины значений
        left = nums[:mid] #левая часть списка
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                nums[k]=left[i]
                i+=1
            else:
                nums[k]=right[j]
                j+=1
                k+=1
        while i<len(left):
            nums[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            nums[k]=right[j]
            j+=1
            k+=1 
list1=[1,2,9,8,7,6,5] 
merge_sort(list1)
print(list1) 
         
