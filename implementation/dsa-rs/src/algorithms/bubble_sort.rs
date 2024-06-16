use std::vec;



pub struct BubbleSort {
    pub arr: Vec<i32>
}

impl BubbleSort {
    pub fn show(self) {
        for i in 0..self.arr.len() {
            print!("{}, ", self.arr[i]);
        }
        println!();
    }
    pub fn sort(&mut self) {
        let mut n = self.arr.len();
        let mut swapped = false;
    
        for i in 0..n {
            swapped = false;
    
            for j in 0..n-i-1 {
                if self.arr[j] > self.arr[1+1] {
                    let temp = self.arr[j];
                    self.arr[j] = self.arr[j+1];
                    self.arr[j+1] = self.arr[j];
                    swapped = true;
                }
            }
    
            if !swapped {
                break;
            }
        }
    }

    
    pub fn bubble_sort(v0: &mut Vec<i32>) -> &mut Vec<i32> {
        let mut n = v0.len();
        let mut swapped = false;
    
        for i in 0..n {
            swapped = false;
    
            for j in 0..n-i-1 {
                if v0[j] > v0[j+1] {
                    let _temp = v0[j];
                    v0[j] = v0[j+1];
                    v0[j+1] = _temp;
                    swapped = true;
                }
            }
    
            if !swapped {
                break;
            }
        }
    
        return v0;
    }
        
}
