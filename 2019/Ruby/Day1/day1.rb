arr = []
File.open("input.txt").each do |line|
    num = line.to_i 
    num = (num / 3) - 2 
    arr.push(num)
end
sum = arr.inject(0, :+)
puts sum 

