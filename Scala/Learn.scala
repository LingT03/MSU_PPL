object CubeIT{
  def MATHIT(number: Int, operation: Int => Int): Int = {
    operation(number)
  }

  def main(args: Array[String]): Unit = {
    def double(num: Int): Int = num * 2

    def square(num: Int): Int = num * num

    val numberToCube: Int = 3
    val resultDouble: Int = MATHIT(numberToCube, double)
    val resultSquare: Int = MATHIT(numberToCube, square)

    println(s"The double of $numberToCube is $resultDouble")
    println(s"The square of $numberToCube is $resultSquare")
  }
}