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
    
        
}
