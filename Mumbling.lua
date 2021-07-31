-- https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/lua
local solution = {}

function solution.accum(s)
  local result = ""
  s = string.lower(s)
  local count=0
  for i = 1, #s do
    local char = string.sub(s,i,i)
    result = result .. string.upper(char)
    result = result .. string.rep(char,count)
    result = result .. "-"
    count = count + 1
  end
  return string.sub(result,1,-2)
end
return solution
