class Calculator

    def sum(*numbers)
        return numbers.reduce(:+)
    end

    def subtract(*numbers)
        return numbers.reduce(:-)
    end

    def multiply(*numbers)
        return numbers.reduce(:*)
    end

    def divide(*numbers)
        return numbers.reduce(:/)
        rescue ZeroDivisionError => e
            puts "#{e}"
    end

end

calc = Calculator.new

puts calc.sum(1, 2, 5)
puts calc.subtract(5, 3, 10)
puts calc.multiply(2, 5, 10)
puts calc.divide(100, 5, 0)