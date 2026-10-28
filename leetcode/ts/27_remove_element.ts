
function removeElement(nums: number[], val: number): number {
    let idx: number = 0
    let removed: boolean = false  
    let pop: number = 0

    while (idx < nums.length) {
        removed = false;
        if (val == nums[idx]) {
            nums.splice(idx, 1)
            removed = true
        }

        if (!removed) {
            idx += 1
        }
    }

    return nums.length
};



function removeElement2(nums: number[], val: number): number {
    /**
     * Using two pointer technique.
     */
    let idx: number = 0
    let removed: boolean = false  
    let pop: number = 0

    while (idx < nums.length) {
        removed = false;
        if (val == nums[idx]) {
            nums.splice(idx, 1)
            removed = true
        }

        if (!removed) {
            idx += 1
        }
    }

    return nums.length
};




function main() {
    let nums: number[] = [3,2,2,3]
    const val: number = 2;
    const nums_length: number = removeElement(nums, val);
    console.log("Result:", nums, nums_length)

}

main()