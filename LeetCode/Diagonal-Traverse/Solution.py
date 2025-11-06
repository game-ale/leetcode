var findDiagonalOrder = function (matrix) {
  if (matrix.length ===0) return [];
  
  let arrayMap = new Map();
  let result = [];
  
  // Storing all the diagonal value in the Map with i+j as a key
  for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < matrix[0].length; j++) {
      if (!arrayMap.has(i + j)) {
        arrayMap.set(i + j, [matrix[i][j]]);
      } else {
        arrayMap.set(i + j, [...arrayMap.get(i + j), matrix[i][j]]);
      }
    }
  }


  let isDown = false;

  arrayMap.forEach((x) => {
    if (isDown) {
      result.push(...x);
    } else {
      result.push(...x.reverse());
    }
    isDown = !isDown;
  });

  return result;
};