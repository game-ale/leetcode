  bool judgeSquareSum(int c) {
    assert(c >= 0);
    int i = std::floor(std::sqrt(c));
    if (i * i == c) {
      return true;
    } else {
      int j = 1;
      while (j <= i) {
        if (i * i + j * j == c) {
          return true;
        } else if (i * i + j * j < c) {
          j++;
        } else {
          i--;
        }
      }
    }

    return false;
  }