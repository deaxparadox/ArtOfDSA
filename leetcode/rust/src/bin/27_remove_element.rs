/// Using two pointer technique
struct Solution;

impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let mut k = 0;

        for i in 0..nums.len() {
            if nums[i] != val {
                nums[k] = nums[i];
                k += 1;
            }
        }
        
        k as i32
    }
}

fn main() {
    let mut nums: Vec<i32> = Vec::new();
    nums.push(3);
    nums.push(2);
    nums.push(2);
    nums.push(3);

    let val = 2;

    let result: i32 = Solution::remove_element(&mut nums, val);

    println!("K: {}", result);
    println!("Modified vec: {:#?}", nums);


}




