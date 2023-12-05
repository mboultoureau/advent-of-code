fn main() {
    let input = include_str!("./input1.txt");
    let output = part1(input);
    dbg!(output);
}

fn part1(input: &str) -> String {
    let mut sum = 0;
    for line in input.lines() {
        let mut number = 0;
        for c in line.chars() {
            if c >= '0' && c <= '9' {
                number = 10 * c.to_digit(10).unwrap();
                break;
            }
        }

        for c in line.chars().rev() {
            if c >= '0' && c <= '9' {
                number += c.to_digit(10).unwrap();
                break;
            }
        }

        sum += number;
    }
    sum.to_string()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = part1(
            "1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"
        );
        assert_eq!(result, "142".to_string());
    }
}