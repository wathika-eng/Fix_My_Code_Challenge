###
#
#  Sort integer arguments (ascending)
#
###

result = []
ARGV.each do |arg|
    # skip if not integer
    next if arg !~ /^-?[0-9]+$/

    # convert to integer
    i_arg = arg.to_i

    if result.empty? || i_arg  > result.last
      result << i_arg
    else
      result.each_with_index do |mm, index|
        if i_arg < mm
          result.insert(index, i_arg)
          break
        end
      end
    end
  end
puts result