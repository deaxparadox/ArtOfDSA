use crate::SortError;
    use std::vec;

    /// This function directly accept the `&mut Vec<i32>`
    /// and sorting them in ascending order using `bubble sort` technique
    /// 
    #[allow(unused)]
    pub fn sort(v0: &mut Vec<i32>) -> Result<(), SortError>{

        #[allow(unused)]
        let mut n = v0.len();

        if n == 0 {
            return Err(SortError::EmptyVector);
        }

        let mut swapped: bool;

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
        Ok(())
    }



    pub fn __print_vector<'a>(v0: &mut Vec<i32>, message: &'a str) -> Result<(), SortError> {
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
    #[allow(unused)]
    pub fn run()  -> Result<(), SortError>{
        let mut v0 = vec![12, 43, 32, 99, 3, 87];
        __print_vector(&mut v0, "Original vector")?;
        sort(&mut v0)?;
        __print_vector(&mut v0, "Sorted vector: ")?;

        Ok(())
    }

    pub struct BubbleSort<'a> {
        pub arr: &'a mut Vec<i32>,
    }

    impl<'a> BubbleSort<'a> {
        /// Builder for `BubbleSort`
        pub fn build(v0: &'a mut Vec<i32>) -> Self {
            Self {
                arr: v0
            }
        }

        /// print the vector, with provide message
        pub fn show(&mut self, message: &'static str) -> Result<(), SortError> {
            let n = self.arr.len();
            if n == 0 {
                return Err(SortError::EmptyVector);
            }
            print!("{}", message);
            for i in 0..n {
                if i == n-1 {
                    print!("{}", self.arr[i]);
                } else {
                    print!("{}, ", self.arr[i]);
                }
            }
            println!();
            Ok(())
        }

        /// Sort the vector;
        pub fn sort(&mut self) -> Result<(), SortError> {
            let n = self.arr.len();

            if n == 0 {
                return Err(SortError::EmptyVector);
            }

            let mut swapped: bool;

            for i in 0..n {
                swapped = false;

                for j in 0..n - i - 1 {
                    if self.arr[j] > self.arr[j + 1] {
                        let temp = self.arr[j];
                        self.arr[j] = self.arr[j + 1];
                        self.arr[j + 1] = temp;
                        swapped = true;
                    }
                }

                if !swapped {
                    break;
                }
            }
            Ok(())
        }
    }

    /// driver function for struct `BubbleSort`
    /// 
    /// Run `BubbleSort` struct implementation
    /// 
    pub fn run2() -> Result<(), SortError>{
        let mut v0 = vec![34, 12, 5, 99, 102, 32, 35];
        let mut b = BubbleSort::build(&mut v0);
        b.show("Original array: ")?;
        let _ = b.sort();
        b.show("Sorted vector: ")?;

        Ok(())
    }