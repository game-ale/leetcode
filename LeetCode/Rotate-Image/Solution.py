def rotate(matrix)
  matrix.replace(matrix.reverse.transpose)
end