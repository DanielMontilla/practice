use std::collections::HashMap;

fn length_of_longest_substring(s: String) -> i32 {
    let mut max_count: i32 = 0;
    let mut start: i32 = -1;
    let mut record: HashMap<char, i32> = HashMap::new();

    for (i, c) in s.chars().enumerate() {
        let i = i as i32;
        match record.get(&c) {
            Some(position) => {
                // if there is  an entry in the map for this letter
                if position > &start {
                    // if the current letter position is more than the current start
                    start = *position;
                }

                // if the current letter's position less than the start (just update)
                record.insert(c, i);
            },
            None => { 
                // if letter doesn't exist in hashmap
                record.insert(c, i);
            }
        }

        // computing iteration count
        let count: i32 = i - start;

        if count > max_count { max_count = count };
    }

    return max_count;
}

fn main() {
    // Inputs:
    let _s_1 = String::from("abcabcbb"); // 3
    let _s_2 = String::from("abcbrascba"); // 5
    let _s_3 = String::from("bbbbb"); // 1
    let _s_4 = String::from("pwwkew"); // 3
    let _s_5 = String::from("a"); // 1
    let _s_6 = String::from(""); // 0
    
    let res_1 = length_of_longest_substring(_s_1);
    let res_2 = length_of_longest_substring(_s_2);
    let res_3 = length_of_longest_substring(_s_3);
    let res_4 = length_of_longest_substring(_s_4);
    let res_5 = length_of_longest_substring(_s_5);
    let res_6 = length_of_longest_substring(_s_6);

    println!("{res_1}, {res_2}, {res_3}, {res_4}, {res_5}, {res_6}");
}


// Runtime: 7 ms, faster than 54.81% of Rust online submissions for Longest Substring Without Repeating Characters.
// Memory Usage: 2.1 MB, less than 76.62% of Rust online submissions for Longest Substring Without Repeating Characters.