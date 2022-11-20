package main

import (
	"math"
	"strconv"
	"strings"
)

func operate(num1 float64, num2 float64, op string) float64 {
	switch op {
	case "+":
		return num1 + num2
	case "-":
		return num1 - num2
	case "*":
		return num1 * num2
	case "/":
		return num1 / num2
	case "^":
		return math.Pow(num1, num2)
	default:
		return 0
	}
}

func theSmallerOf(num1 float64, num2 float64) float64 {
	if num1 < num2 {
		return num1
	} else {
		return num2
	}
}

func toTokens(expression string) []string {
	tokens := []string{}

	// split at ^, +, -, *, /
	j := 0
	for i := 0; i < len(expression); i++ {
		if expression[i] == '^' || expression[i] == '+' || expression[i] == '-' || expression[i] == '*' || expression[i] == '/' {
			tokens = append(tokens, expression[j:i])
			tokens = append(tokens, string(expression[i]))
			j = i + 1
		} else if i == len(expression)-1 {
			tokens = append(tokens, expression[j:i+1])
		}
	}

	return tokens
}

func stringInSlice(a string, list []string) bool {
	for _, b := range list {
		if b == a {
			return true
		}
	}
	return false
}

func toFloat(str string) float64 {
	num, _ := strconv.ParseFloat(str, 64)
	return num
}

func toString(num float64) string {
	return strconv.FormatFloat(num, 'f', -1, 64)
}

func calculate(expression string) float64 {
	expression = strings.ReplaceAll(expression, " ", "")
	// tokens := toTokens(expression)
	precedence := []string{"^", "*", "/", "+", "-"}
	tokenized_expression := toTokens(expression)

	for _, operator := range precedence {
		// repeat until no more precedence operator in expression
		for stringInSlice(operator, tokenized_expression) {
			for i, token := range tokenized_expression {
				if stringInSlice(token, strings.Split(operator, "")) {

					println(strings.Join(tokenized_expression, ", "))

					num1 := tokenized_expression[i-1]
					num2 := tokenized_expression[i+1]
					op := tokenized_expression[i]
					result := operate(toFloat(num1), toFloat(num2), op)
					tokenized_expression = append(tokenized_expression[:i-1], append([]string{toString(result)}, tokenized_expression[i+2:]...)...)
				}
			}
		}
	}

	return toFloat(tokenized_expression[0])
}

func main() {
	println(
		// strings.Join(toTokens("2^3^4+1.5*1.2"), ", "),
		calculate("2^3^4+1.5*4"),
	)
}
