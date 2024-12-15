
pub mod merge_operation_vector {
    pub fn run() {
        let mut v1 = vec![1, 2, 4, 5];
        let mut v2 = vec![2, 9, 12, 15];
    
        let c = __merge_operation_vector(v1, v2);
        for i in 0..c.len() {
            print!("{}, ", c[i]);
        }
    }
    
    fn __merge_operation_vector(a: Vec<i32>, b: Vec<i32>) -> Vec<i32>{
        let mut c = Vec::new();
        let (mut ai, mut bi) = (0, 0);
        let (alen, blen) = (a.len(), b.len());
    
        while ((ai < alen) && (bi < blen)) {
            if (a[ai] < b[bi]) {
                c.push(a[ai]);
                ai = ai + 1;
            } else {
                c.push(b[bi]);
                bi = bi + 1;
            }
        }
    
    
        while (ai < alen) {
            c.push(a[ai]);
            ai = ai + 1;
        }
    
        while (bi < blen) {
            c.push(b[bi]);
            bi = bi + 1;
        }
    
        return c;
    }
}




pub mod merge_operation_struct {
    pub fn run() {
        let mut v1 = vec![23, 45, 65, 79, 91];
        let mut v2 = vec![1, 19, 21, 46, 64];
    
        let mut mo = MergeOperation{a: &v1, b: &v2};
        let c = mo.merge();

        for i in 0..c.len() {
            print!("{} ", c[i]);
        }
    }
    

    pub struct MergeOperation<'a> {
        a: &'a Vec<i32>,
        b: &'a Vec<i32>
    }
    impl<'a> MergeOperation<'a> {
        pub fn new(a: &'a mut Vec<i32>, b: &'a mut Vec<i32>) -> Self {
            Self {
                a: a,
                b: b
            }
        }

        pub fn merge(&mut self) -> Vec<i32> {
            let mut c = Vec::new();


            let (mut ai, mut bi) = (0, 0);
            let (alen, blen) = (self.a.len(), self.b.len());
        
            while ((ai < alen) && (bi < blen)) {
                if (self.a[ai] < self.b[bi]) {
                    c.push(self.a[ai]);
                    ai = ai + 1;
                } else {
                    c.push(self.b[bi]);
                    bi = bi + 1;
                }
            }
        
        
            while (ai < alen) {
                c.push(self.a[ai]);
                ai = ai + 1;
            }
        
            while (bi < blen) {
                c.push(self.b[bi]);
                bi = bi + 1;
            }

            return c
        }
    }

}

