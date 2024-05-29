def maximum_of_minimum_window_size(arr):
   if arr == None:
      return None
   
   s = []
   n = len(arr)
   left = [-1] * (n+1)
   right = [n] * (n+1)

   for i in range(n):
      while len(s) != 0 and arr[s[0]] >= arr[i]:
         s.pop(0)
      
      if len(s) != 0:
         left[i] = s[0]

      s.insert(0, i)
   
   while len(s) != 0:
      s.pop(0)
   
   for i in range(n-1, -1, -1):
      while len(s) != 0 and arr[s[0]] >= arr[i]:
         s.pop(0)
      
      if len(s) != 0:
         right[i] = s[0]

      s.insert(0, i)

   ans = [0] * (n+1)
   for i in range(n):
      Len = right[i] - left[i] - 1
      ans[Len] = max(ans[Len], arr[i])

   for i in range(n - 1, 0, -1):
        ans[i] = max(ans[i], ans[i + 1])

   return ans[1:n+1]
   

      


if __name__ == '__main__':
  arr = [10, 20, 15, 50, 10, 70, 30]
  result = maximum_of_minimum_window_size(arr)
  print(result)