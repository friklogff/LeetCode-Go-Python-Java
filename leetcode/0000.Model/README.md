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
import "sort"

func permuteUnique(nums []int) [][]int {
	if len(nums) == 0 {
		return [][]int{}
	}
	used, p, res := make([]bool, len(nums)), []int{}, [][]int{}
	sort.Ints(nums) // 这里是去重的关键逻辑
	generatePermutation47(nums, 0, p, &res, &used)
	return res
}

func generatePermutation47(nums []int, index int, p []int, res *[][]int, used *[]bool) {
	if index == len(nums) {
		temp := make([]int, len(p))
		copy(temp, p)
		*res = append(*res, temp)
		return
	}
	for i := 0; i < len(nums); i++ {
		if !(*used)[i] {
			if i > 0 && nums[i] == nums[i-1] && !(*used)[i-1] { // 这里是去重的关键逻辑
				continue
			}
			(*used)[i] = true
			p = append(p, nums[i])
			generatePermutation47(nums, index+1, p, res, used)
			p = p[:len(p)-1]
			(*used)[i] = false
		}
	}
	return
}

给出完善后带注释完整代码

给出测试输出语句


你能用同样的思路同样数量的解法用Java实现么，以此为开头，给出带注释完整代码
class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {

    }
}
你能用同样的思路同样数量的解法用Python实现么，以此为开头，给出带注释完整代码
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
你能用同样的思路同样数量的解法用c++实现么，以此为开头，给出带注释完整代码
class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {

    }
};
你能用同样的思路同样数量的解法用go实现么，以此为开头，给出带注释完整代码
func permute(nums []int) [][]int {

}
我们用中文交流，分开介绍每个版本的所需要掌握的详细基础知识

再分别介绍每个版本的解题思路

git add .
git commit -m "Updated"
git push

```


