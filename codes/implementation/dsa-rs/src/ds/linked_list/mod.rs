pub fn run() -> Result<(), ()> {
    let n1 = Stack::new(1);
    Stack::print(&n1);

    
    // while let Some(value) = t {
    //     t = value.next;
    // }
    // t = Some(Box::new(Node { value: 3, next: None}));

    // t = n1;

    // while let Some(value) = t {
    //     println!("{}", value.value);
    //     t = value.next;
    // }
    // println!("{}", n1.value);

    Ok(())
}

#[derive(Debug)]
struct Stack {
    next: Option<Box<Stack>>,
    value: i32
}

impl Stack {
    fn new(value: i32) -> Option<Box<Stack>> {
        Some(Box::new(Stack {
            value: value,
            next: None
        }))
    }
    fn print(mut temp: &Option<Box<Stack>>) {
        // while let Some(stack) = temp {
        //     println!("Stack value: {}", temp.as_ref().unwrap().value);
        //     temp = &temp.as_ref().unwrap().next;
        // }
        match temp {
            Some(stack) => {
                println!("Stack value: {}", stack.value);
                temp = &temp.as_ref().unwrap().next;
            },
            None => println!("Stack over")
        }
    }
    fn insert(mut temp: &Option<Box<Stack>>, value: i32) {
        while let Some(stack) = temp {
            if let None = &temp.as_ref().unwrap().next {
                break;
            }
            temp = &temp.as_ref().unwrap().next;
        }
        let n = Stack::new(value);
        // temp.as_mut().unwrap().next = n;
    }
}