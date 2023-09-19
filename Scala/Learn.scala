object Main {
  def main(args: Array[String]): Unit = {
    for (i <- 1 to 3; j <- 1 to 3) println(i + " and " + j + " = " + f"${10 * i + j}")
  }
}
