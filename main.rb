require 'anystyle'
require 'json'

# dict = AnyStyle.parse 'Derrida, J. (1967). L\U+FFE2\U+FFC3\U+FFA9criture et la diff\U+FFC3\U+FFA9rence (1 \U+FFC3\U+FFA9d.). Paris: \U+FFC3ditions du Seuil.'
# pp(dict)

puts ARGV[0]

file = File.open("reference.txt")

file_data = file.read

pp(file_data)

dict = AnyStyle.parse file_data
# pp(dict)

# pp(dict.class)

# dict.each do |item|
#     puts item
#     puts item.class
#     puts "\n"

#     item.each do |item2|
#         puts item2
#         puts item2.class
#         puts "\n"
#     end
# end

# puts dict.to_json

File.open("temp.json","w") do |f|
    f.write(dict.to_json)
end