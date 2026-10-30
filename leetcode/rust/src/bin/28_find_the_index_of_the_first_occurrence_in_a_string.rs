pub struct Solution; 

impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
        let mut status: bool = false;
        for i in 0..haystack.len() {
            status = haystack[i..i+needle.len()].starts_with(&needle);
            if status {
                return i as i32;
            }
        }
        return -1;
        
    }
}

fn main() {
}