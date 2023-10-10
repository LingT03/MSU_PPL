// Referenced W3Schools for Scala Syntax

object TakeHome {
  def main(args: Array[String]): Unit = {
    // Define a list of numbers
    val numbers = List(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    // Function to add 1 to all even numbers in the list
    def adder(numList: List[Int]): List[Int] = {
      numList.map {
        case x if x % 2 == 0 => x + 1
        case x => x
      }
    }

    // Function to multiply odd numbers by 2 in the list
    def multiplier(numList: List[Int]): List[Int] = {
      numList.map {
        case x if x % 2 != 0 => x * 2
        case x => x
      }
    }

    // Higher Order Function
    def higherOrder(numList: List[Int], operationFunc: List[Int] => List[Int]): List[Int] = {
      operationFunc(numList)
    }

    // Display the original list
    println("Original List: " + numbers + "\n")

    // Display the results of all possible function calls
    val result1 = higherOrder(numbers, adder)
    println("Add 1 to Even Numbers: " + result1 + "\n")

    val result2 = higherOrder(numbers, multiplier)
    println("Multiply Odd Numbers by 2: " + result2 + "\n")

    val result3 = higherOrder(result1, multiplier)
    println("Add 1 to Even Then Multiply Odd by 2: " + result3 + "\n")

    val result4 = higherOrder(result2, adder)
    println("Multiply Odd by 2 Then Add 1 to Even: " + result4)
  }
}
