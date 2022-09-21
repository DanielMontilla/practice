fn best_time_to_buy_and_sell_stock(prices: Vec<i32>) -> i32 {
    let mut max_profit = 0;
    let last_day = prices.len() as i32 - 1;

    if last_day >= 1 {
        let mut buy_day = 0;
        let mut sell_day = 1;
        let mut move_sell = true;

        'main: loop {
            
            let profit = prices[sell_day] - prices[buy_day];

            if profit > max_profit { max_profit = profit };

            if move_sell {

                if sell_day >= last_day as usize { break 'main } // exit condition

                let sell_price = prices[sell_day];
                let mut best_sell_day = sell_day + 1;

                while sell_price >= prices[sell_day] { // shift pointer until we find higher sell price
                    sell_day += 1;

                    if prices[sell_day] >= prices[best_sell_day] { best_sell_day = sell_day }

                    if sell_day >= last_day as usize {
                        sell_day = best_sell_day;
                        break;
                    };
                }

                move_sell = false;

            } else {
                
                let buy_price = prices[buy_day];
                let best_buy_day = buy_day;

                while buy_price <= prices[buy_day] { // shift pointer until we find lower sell price
                    buy_day += 1;
                    if buy_day == sell_day { // when we reach a point where pointers are touching we revert back to the best buy day and flip move_sell flag
                        buy_day = best_buy_day;
                        move_sell = true;
                        break;
                    }
                }
            }
        }
    }

    return max_profit;
}

fn main() {
    // Inputs:
    let _prices_1 = vec![7,6,4,3,1];
    let _prices_2 = vec![7,1,5,3,6,4];
    let _prices_3 = vec![1,2];
    let _prices_4 = vec![3,3,5,0,0,3,1,4];
    let _prices_5 = vec![2,4,1];
    let _prices_6 = vec![11,7,2,4,1];

    let res_1 = best_time_to_buy_and_sell_stock(_prices_1); // 0
    let res_2 = best_time_to_buy_and_sell_stock(_prices_2); // 5 
    let res_3 = best_time_to_buy_and_sell_stock(_prices_3); // 1
    let res_4 = best_time_to_buy_and_sell_stock(_prices_4); // 4
    let res_5 = best_time_to_buy_and_sell_stock(_prices_5); // 2
    let res_6 = best_time_to_buy_and_sell_stock(_prices_6); // 2
    
    println!("{res_1}, {res_2}, {res_3}, {res_4}, {res_5}, {res_6}");
}

// Runtime: 502 ms, faster than 5.95% of Rust online submissions for Best Time to Buy and Sell Stock.
// Memory Usage: 3.1 MB, less than 27.50% of Rust online submissions for Best Time to Buy and Sell Stock.

// NOTES:
// pretty terrable solution but a solution nonetheless
