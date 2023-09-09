## 代码

## Go

```Go

```

## Python

```Python

```

## Java

```Java

```

## Cpp

```Cpp

```

## Prompt

```Prompt
我们用中文交流，你能理解这段代码么，逐行加上注释
func searchRange(nums []int, target int) []int {
    n := len(nums)
    l_prt := 0
    r_prt := n - 1
    
    ans := []int{-1, -1}  
    for l_prt <= r_prt{
        mid := ((r_prt - l_prt)>>1) + l_prt
        if nums[mid]==target{
            ans[0] = mid
            ans[1] = mid
            for ans[0] > 0 && nums[ans[0]-1] == target{
                ans[0]--
            }
            for ans[1] < n - 1 && nums[ans[1] + 1] ==target{
                ans[1]++
            }
            break
        }else if nums[mid] > target{
            r_prt = mid - 1
        }else{
            l_prt = mid + 1
        }
    }
    return ans
}

给出完善后带注释完整代码

给出测试输出语句

你能用同样的思路同样数量的解法用Python实现么，以此为开头，给出带注释完整代码
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
你能用同样的思路同样数量的解法用Java实现么，以此为开头，给出带注释完整代码
class Solution {
    public int[] searchRange(int[] nums, int target) {

    }
}
你能用同样的思路同样数量的解法用c++实现么，以此为开头，给出带注释完整代码
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {

    }
};
我们用中文交流，分开介绍每个版本的所需要掌握的详细基础知识

再分别介绍每个版本的解题思路

git add .
git commit -m "Updated"
git push

```


