use std::io;

pub fn run() -> Result<(), ()> {
    search()?;
    return Ok(());
}

fn search() -> Result<(), ()> {
    let numbers: Vec<i32> = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

    println!("We have the following array of number?");
    print!("Select the target ? ");
    
    let mut target = 4;


    LinearSearch::find_target(&numbers, target)?;
    println!("{:?}", numbers);
    Ok(())
}

struct LinearSearch;
impl LinearSearch {
    pub fn find_target(arr: &Vec<i32>, target: i32) -> Result<(), ()>{
        for i in arr.into_iter() {
            println!("{target}\t{i}");
            if target == *i {
                return Ok(());
            }
        }
        return Err(());
    }
}