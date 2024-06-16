

pub mod bubble {
    use crate::SortError;
    use std::vec;

    /// This function directly accept the `&mut Vec<i32>`
    /// and sorting them in ascending order using `bubble sort` technique
    /// 
    pub fn sort(v0: &mut Vec<i32>) -> &mut Vec<i32> {
        let mut n = v0.len();
        let mut swapped = false;

        for i in 0..n {
            swapped = false;

            for j in 0..n - i - 1 {
                if v0[j] > v0[j + 1] {
                    let _temp = v0[j];
                    v0[j] = v0[j + 1];
                    v0[j + 1] = _temp;
                    swapped = true;
                }
            }

            if !swapped {
                break;
            }
        }

        return v0;
    }



    pub fn __print_vector(v0: &mut Vec<i32>, message: &'static str) -> Result<(), SortError> {
        let n = v0.len();

        if n == 0 {
            return Err(SortError::EmptyVector);
        }

        print!("{}: ", message);
        for i in 0..n {
            if i == n-1 {
                print!("{}", v0[i]);    
            } else {
                print!("{}, ", v0[i]);
            }
        }
        println!();
        Ok(())
    }


    /// It is the caller for `sort()` function;
    pub fn run()  -> Result<(), SortError>{
        let mut v0 = vec![12, 43, 32, 99, 3, 87];
        __print_vector(&mut v0, "Original vector")?;
        sort(&mut v0);
        __print_vector(&mut v0, "Sorted vector: ")?;

        Ok(())
    }

    pub struct BubbleSort {
        pub arr: Vec<i32>,
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

                for j in 0..n - i - 1 {
                    if self.arr[j] > self.arr[1 + 1] {
                        let temp = self.arr[j];
                        self.arr[j] = self.arr[j + 1];
                        self.arr[j + 1] = self.arr[j];
                        swapped = true;
                    }
                }

                if !swapped {
                    break;
                }
            }
        }

        
    }
}
