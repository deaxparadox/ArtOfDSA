use std::slice::SliceIndex;

// pub fn sort_arr<T>(arr: &Vec<T>) -> &Vec<T> {
//     let mut t: i32 = 0;
//     for i in 0..arr.len() {
//         if t > arr[i as i32] {}
//     }
//     return arr;
// }

trait Sort<T> {

}

impl<T, I> Sort<I> for Vec<T> where I: SliceIndex<[T]> {}
