function get_indexes(haystack: string, needle_first_char: string): number[] {
    let _temp: number[] = []
    let chars: string[] = [...haystack];
    let chars_len = chars.length
    for (let i=0; i<chars_len; i++) {
        if (needle_first_char === chars[i]) {
            _temp.push(i)
        }
    }
    return _temp;
}

function strStr1(haystack: string, needle: string): number {
    let needle_first_char: string = needle[0]
    const needle_len: number = needle.length
    let indexes: number[] = get_indexes(haystack, needle_first_char)
    for (let idx=0; idx<indexes.length; idx++) {
        if (haystack.slice(idx, idx + needle_len).startsWith(needle)) {
            return idx
        }
    }
    return -1
};



function strStr2(haystack: string, needle: string): number {
    for (let idx=0; idx<haystack.length; idx++) {
        if (haystack.slice(idx, idx + needle.length).startsWith(needle)) {
            return idx
        }
    }
    return -1
};