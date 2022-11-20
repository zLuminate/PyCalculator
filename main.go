package main

import (
	"math"
	"strconv"
	"strings"
)

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
func stringInSlice(a string, list []string) bool {
	for _, b := range list {
		if b == a {
			return true
		}
	}
	return false
}
func toFloat(str string) float64  { num, _ := strconv.ParseFloat(str, 64); return num }
func toString(num float64) string { return strconv.FormatFloat(num, 'f', -1, 64) }

func calculate(expression string) float64 {
	expression = strings.ReplaceAll(expression, " ", "")
	precedence := []string{"^", "*/", "+-"}
	tokenized_expression := toTokens(expression)

	for _, operator := range precedence {
		for stringInSlice(operator[0:1], tokenized_expression) || stringInSlice(operator[1:], tokenized_expression) {
			for c, token := range tokenized_expression {
				if strings.ContainsAny(operator, token) {
					println(token)
					num1 := toFloat(tokenized_expression[c-1])
					num2 := toFloat(tokenized_expression[c+1])
					tokenized_expression[c-1] = toString(operate(num1, num2, token))
					tokenized_expression = append(tokenized_expression[:c], tokenized_expression[c+2:]...)
				}
			}
		}
	}

	return toFloat(tokenized_expression[0])
}

func main() {
	println(
		calculate("2^3^4+1.5*4"),
	)
}
