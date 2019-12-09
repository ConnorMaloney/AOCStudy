arr = []
File.open("input.txt").each do |line|
    num = line.to_i
    num = (num / 3) - 2
    def recur_fuel(num)
        if num <= 7
            num
        else
            num = num + recur_fuel(num/3 - 2)
        end
    end
    num = recur_fuel(num)
            
    arr.push(num)
end
sum = arr.inject(0, :+)
puts sum 

